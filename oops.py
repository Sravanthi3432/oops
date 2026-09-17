'''1st Example of OOPS'''

# class Employee:
#     company_name = 'Techsol'
#     def __init__(self,name, employee_id, salary):
#         self.name = name
#         self.employee_id = employee_id
#         self.salary = salary
#     def display_details(self):
#         print("Name:",self.name)
#         print('Employee_id:',self.employee_id)
#         print('Salary:',self.salary)
#         print('Company Name:',self.company_name)

#     @classmethod
#     def change_company(cls,new_name):
#         cls.company_name = new_name

#     @staticmethod
#     def validate_salary(salary):
#         return salary > 0
        
# emp1 = Employee("Sravanthi", 101, 50000)

# emp1.display_details()

# Employee.change_company("XYZ Company")

# print("After changing company name:")
# emp1.display_details()

# print("Salary Valid:", Employee.validate_salary(emp1.salary))

''''''''''2nd Example of OOPS'''''''''''

# class Employee:
#     def __init__(self, name, employee_id, salary):
#         self.name = name
#         self.employee_id = employee_id
#         self.salary = salary

# class Developer(Employee):
#     def __init__(self, name, employee_id, salary, programming_language):
#         super().__init__(name, employee_id, salary)
#         self.programming_language = programming_language

#     def write_code(self):
#         print("Name:", self.name)
#         print("Employee ID:", self.employee_id)
#         print("Salary:", self.salary)
#         print("Programming Language:", self.programming_language)

# class ProjectManager(Employee):
#     def __init__(self, name, employee_id, salary, team_size):
#         super().__init__(name, employee_id, salary)
#         self.team_size = team_size

#     def assign_task(self,task_name):
#         self.task_name = task_name
#         print("Name:", self.name)
#         print("Employee ID:", self.employee_id)
#         print("Team Size:", self.team_size)
#         print(f"Assigning task '{task_name}' to the team.")

# d = Developer("Sravanthi", 101, 50000, "Python")
# d.write_code()

# pm = ProjectManager("Ravi", 102, 70000, 5)
# pm.assign_task("Create Login Page")

'''''''''3rd Example of OOPS'''''''''''

# def task_logger(func):
#     def wrapper(task_name):
#         print("Task execution started")
#         func(task_name)
#         print("Task execution completed")
#     return wrapper
# @task_logger
# def assign_task(task_name):
#     print("Task:", task_name)
# assign_task("Create Login Page")

'''''''''4th Example of OOPS'''''''''''

class Employee:
    company_name = "Techsol"

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print("Company Name:", self.company_name)

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def write_code(self):
        print("Name:", self.name)
        print("Programming Language:", self.programming_language)


class ProjectManager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def assign_task(self, task_name):
        print("Name:", self.name)
        print("Team Size:", self.team_size)
        print("Task:", task_name)


emp1 = Developer("Sravanthi", 101, 50000, "Python")
emp2 = Developer("Ravi", 102, 70000, "Python")

emp1.display_details()
emp2.display_details()

emp1.write_code()
emp2.write_code()

pm = ProjectManager("Kiran", 103, 80000, 5)
pm.assign_task("Create Login Page")

Employee.change_company("XYZ Company")

print("After changing company name:")

emp1.display_details()
emp2.display_details()
pm.display_details()

