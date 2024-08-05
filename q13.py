class Employee:
    def __init__(self, name, date_of_joining, designation, salary):
        self.name = name
        self.date_of_joining = date_of_joining
        self.designation = designation
        self.salary = salary

    def display_info(self):
        print("Employee Name:", self.name)
        print("Date of Joining:", self.date_of_joining)
        print("Designation:", self.designation)
        print("Salary: $", self.salary)

# Create an instance of the Employee class
employee1 = Employee("John Doe", "2024-08-01", "Software Engineer", 75000)

# Display the employee's information
employee1.display_info()
