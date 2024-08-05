# Superclass
class Company:
    def __init__(self, name, city, mobile_no):
        self.name = name
        self.city = city
        self.mobile_no = mobile_no

    def display_company_info(self):
        print("Company Name:", self.name)
        print("City:", self.city)
        print("Mobile No:", self.mobile_no)

# Subclass
class Employee(Company):
    def __init__(self, name, city, mobile_no, emp_name, designation, salary):
        # Call the superclass (Company) __init__ method
        super().__init__(name, city, mobile_no)
        self.emp_name = emp_name
        self.designation = designation
        self.salary = salary

    def display_employee_info(self):
        # Display company info by calling the superclass method
        self.display_company_info()
        print("Employee Name:", self.emp_name)
        print("Designation:", self.designation)
        print("Salary: $", self.salary)

# Create an instance of the Employee class
employee1 = Employee("Tech Innovations Inc.", "New York", "123-456-7890", "Alice Smith", "Software Engineer", 85000)

# Display the employee's and company's information
employee1.display_employee_info()
