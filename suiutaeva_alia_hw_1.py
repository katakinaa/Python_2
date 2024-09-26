class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Fullname: {self.fullname} Age: {self.age} Is_married: {self.is_married}')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_marks(self):
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks)


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    base_salary = 30000

    def calculate_salary(self):
        bonus_percentage = max(0, (self.experience - 3) * 0.05)
        return self.base_salary * (1 + bonus_percentage)


teacher = Teacher("Mr. Jones", 35, True, 10)

teacher.introduce_myself()
print(f"Experience: {teacher.experience} years")
salary = teacher.calculate_salary()
print(f"Salary: {salary:.2f}\n")


def create_students():
    students_list = []

    student1 = Student("Betty Cooper", 16, False, {'Math': 85, 'Science': 68, 'History': 92})
    student2 = Student("Archie Andrews", 17, False, {'Math': 79, 'Science': 88, 'History': 65})
    student3 = Student("Veronica Lodge", 16, False, {'Math': 90, 'Science': 91, 'History': 87})

    students_list.append(student1)
    students_list.append(student2)
    students_list.append(student3)

    return students_list


students = create_students()


for student in students:
    student.introduce_myself()
    print("Marks:")
    for subject, mark in student.marks.items():
        print(f"{subject} - {mark}")
    avg_mark = student.average_marks()
    print(f"Average Mark: {avg_mark:.2f}\n")
