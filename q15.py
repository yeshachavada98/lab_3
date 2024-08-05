# Base class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Base class 2
class Worker:
    def __init__(self, job_title, salary):
        self.job_title = job_title
        self.salary = salary

    def display_worker_info(self):
        print(f"Job Title: {self.job_title}")
        print(f"Salary: ${self.salary}")

# Base class 3
class Student:
    def __init__(self, student_id, major):
        self.student_id = student_id
        self.major = major

    def display_student_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")

# Derived class using multiple inheritance
class WorkingStudent(Person, Worker, Student):
    def __init__(self, name, age, job_title, salary, student_id, major):
        # Initialize the base classes
        Person.__init__(self, name, age)
        Worker.__init__(self, job_title, salary)
        Student.__init__(self, student_id, major)

    def display_all_info(self):
        self.display_person_info()
        self.display_worker_info()
        self.display_student_info()

# Create an instance of the WorkingStudent class
working_student = WorkingStudent("John Doe", 22, "Intern", 30000, "S12345", "Computer Science")

# Display all information
working_student.display_all_info()
