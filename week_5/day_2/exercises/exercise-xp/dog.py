class Dog():
    def __init__(self,name,age,weight):
        self.name, self.age, self.weight = name,age,weight

    def bark(self):
        return f"{self.name} is barking!"

    def run_speed(self):
        return (self.weight / (self.age * 10))

    def fight(self, other_dog):
        return \
            self.name \
            if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight\
            else other_dog.name
    