import faker
from datetime import datetime

f = faker.Faker()

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = {}
        self.absences = []

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'Student object: {self.full_name()}'

    def __str__(self):
        return f'Student object: {self.full_name()}'


class ClassRoom:
    def __init__(self, subject, teacher_name):
        self.subject = subject
        self.teacher = teacher_name
        self.students = []
        self.attendace_list = []


    def take_student_name_input(self):
        full_name = input('What\'s the students full name? (seperated by spaces)').lower().split()
        return ' '.join(full_name[0:-1]), full_name[-1]


    def add_student(self):
        self.students.append(Student(*self.take_student_name_input()))


    def populate_class(self, num):
        for _ in range(num):
            self.students.append(Student(f.first_name(), f.last_name()))


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
            attended = input(f'is {student.full_name()} present? Y/N:')
            if attended in 'Yy':
                attendance['attendees'].append(student.full_name())
            else:
                student.absences.append(today)
        self.attendace_list.append(attendance)

    def show_students(self):
        for student in self.students:
            print(f'{student.full_name()}, learning {self.subject}, has {len(student.absences)} absences')


    def __repr__(self):
        return f'Class by {self.teacher}: {self.subject}, {len(self.students)} students registered'

    def __str__(self):
        return f'Class by {self.teacher}: {self.subject}, {len(self.students)} students registered'