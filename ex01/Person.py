class Person:

    def __init__(self, name, address, age):
        self.address = address
        self.age = age
        self.name = name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return f"{self.name} ({self.age}) {self.address}"


class Student(Person):

    def __init__(self, name, address, age, student_id, major, gpa):
        super().__init__(name, address, age)
        self.student_id = student_id
        self.major = major
        self.gpa = gpa

    def set_gpa(self, gpa):
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa

    def set_major(self, major):
        self.major = major

    def get_major(self):
        return self.major

    def set_student_id(self, student_id):
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id

    def __str__(self):
        return f"{self.name} | ({self.age}) | Student ID:({self.student_id}) | {self.major} | {self.gpa}"


Adam = Student("Adam", "123 Hawaii Street", 19, 12429502, "Comp Sci", 3.93)
print(Adam)
