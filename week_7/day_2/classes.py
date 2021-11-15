import faker
from dotenv import dotenv_values
import os
from datetime import datetime
import json
import psycopg2

def get_env_db_info_dict():
    config = dotenv_values(os.path.join(os.path.dirname(__file__), '.env'))
    return config

pg_env_details = get_env_db_info_dict()


pg_details = {'host': pg_env_details.get('db_host'), 'user':pg_env_details.get('db_user'),
 'password': pg_env_details.get('db_pass'), 'dbname':pg_env_details.get('db_name')}
def run_query(query, mode='w'):
    connection = psycopg2.connect(**pg_details)
    cursor = connection.cursor()
    cursor.execute(query)
    if mode == 'ra':
        results = cursor.fetchall()
    if mode == 'r1':
        results = cursor.fetchone()
    connection.commit()
    connection.close()
    if 'r' in mode :
        return results
    print('db update successfully')


f = faker.Faker()
# text, int/numbers, bool, list, dictionary/object

class Absence:
    format_code = '%Y/%m/%d'
    def __init__(self,student, date=None, absence_id=None):
        self.id = absence_id
        self.student = student
        if not date:
            self.date = datetime.today()
        elif isinstance(date, datetime):
            self.date = date
        elif isinstance(date, str):
            self.date = datetime.strptime(date, self.format_code)
        if not absence_id:
            self.save()


    def date_str(self):
        return self.date.strftime(self.format_code)

    def save(self):
        query = f"INSERT INTO absence (student_id, date) VALUES ('{self.student.id}', '{self.date_str()}')"
        run_query(query)

    def __str__(self):
        return f'{self.student.full_name()} missed class on {self.date_str()}'

    def __repr__(self):
        return self.__str__()




class Student:
    def __init__(self, first_name, last_name, classroom, student_id=None):
        self.id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.classroom = classroom
        self.grades = {}
        self.absences = []
        if not student_id:
            self.save()
        else:
            query = f"SELECT *  FROM absence WHERE student_id='{self.id}'"
            absence_data = run_query(query, 'ra')
            for data in absence_data:
                self.absences.append(Absence(student=self, date=data[1], absence_id=data[0]))



    def save(self):
        query = f"INSERT INTO student (first_name, last_name, class_id) VALUES ('{self.first_name}', '{self.last_name}', '{self.classroom.id}')"
        run_query(query)

    def to_json(self, format_code):
        data = {
            'first_name':self.first_name,
            'last_name': self.last_name,
            'grades': self.grades,
            'absences': [absence.strftime(format_code) for absence in self.absences]
            }
        return data

    def save(self):
        query = f"INSERT INTO student (first_name, last_name, class_id) VALUES ('{self.first_name}', '{self.last_name}', '{self.classroom.id}')"
        run_query(query)



    @classmethod
    def from_json(cls, data, format_code):
        student = cls(data['first_name'], data['last_name'])
        student.grades = data['grades']
        student.absences = [datetime.strptime(absence, format_code) for absence in data['absences']]
        return student

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'Student object: {self.full_name()}'

    def __str__(self):
        return f'Student object: {self.full_name()}'


class ClassRoom:
    format_code = '%Y/%m/%d'
    def __init__(self, subject, teacher_name, id=None):
        self.id = id
        self.subject = subject
        self.teacher = teacher_name
        self.attendace_list = []
        self.students = []
        if not self.id: # new object, save to db
            self.save()
            query = f"SELECT *  FROM singleclass WHERE subject='{self.subject}' AND  teacher='{self.teacher}'"
            result = run_query(query, 'r1')
            self.id = result[0]
        else: #loading classroom and students from db
            query = f"SELECT *  FROM student WHERE class_id='{self.id}'"
            student_data = run_query(query, 'ra')
            for data in student_data:

                self.students.append(Student(data[1], data[2], self, data[0]))


    @classmethod
    def load_by_id(cls, class_id):
        query = f"SELECT *  FROM singleclass WHERE class_id='{class_id}'"
        result = run_query(query, 'r1')
        return cls(id=result[0], subject=result[1], teacher_name=result[2])


    def save(self):
        query = f"INSERT INTO singleclass (subject, teacher) VALUES ('{self.subject}', '{self.teacher}')"
        run_query(query)

    def to_json(self, file_name):
        attendance_copy = self.attendace_list
        print(self.attendace_list)
        for attendance in attendance_copy:
            print(attendance['date'])
            if isinstance(attendance['date'], datetime):

                attendance['date'] = attendance['date'].strftime(self.format_code)

        data = {
            'subject': self.subject,
            'teacher': self.teacher,
            'students':[stu.to_json(self.format_code) for stu in self.students],
            'attendance_list': attendance_copy
        }

        print(data)
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=2)
        print(f'file {file_name} was created successfully')

    @classmethod
    def from_json(cls, file_name):
        with open(file_name) as f:
            data = json.load(f)

        instance = cls(data['subject'], data['teacher'])
        instance.attendace_list = data['attendance_list']
        instance.students = [Student.from_json(stu, cls.format_code) for stu in data['students']]
        for attendance in instance.attendace_list:
            attendance['date'] = datetime.strptime(attendance['date'], cls.format_code)
        print(instance.attendace_list)
        return instance



    def take_student_name_input(self):
        full_name = input('What\'s the students full name? (seperated by spaces)').lower().split()
        return ' '.join(full_name[0:-1]), full_name[-1]


    def add_student(self):
        self.students.append(Student(*self.take_student_name_input(), classroom=self))


    def populate_class(self, num):
        for _ in range(num):
            self.students.append(Student(f.first_name(), f.last_name(), classroom=self))


    def remove_student(self):
        fname, lname = self.take_student_name_input()
        for student in self.students:
            if fname == student.first_name and lname == student.last_name:
                idx = self.students.index(student)
                print('student removed successfully', student.full_name())
                del self.students[idx]
                return


        print('that student doesnt exist')


    def take_attendance(self):
        today = datetime.today()
        attendance = {
            'date': today,
            'attendees': []
        }
        for student in self.students:
            while True:
                user_input = input(f'is {student.full_name()} present? Y/N:')
                if user_input in ['y','n','Y','N']:
                    break

            if user_input in 'Yy':
                attendance['attendees'].append(student.full_name())
            else:
                print(type(today))
                student.absences.append(Absence(student))
        self.attendace_list.append(attendance)

    def show_students(self):
        for student in self.students:
            print(f'{student.full_name()}, learning {self.subject}, has {len(student.absences)} absences')


    def __repr__(self):
        return f'Classroom object by {self.teacher}'

    def __str__(self):
        return f'Class by {self.teacher}: {self.subject}, ? students registered'