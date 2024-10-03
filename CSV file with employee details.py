import csv

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def __repr__(self):
        return f'Employee(name="{self.name}", position="{self.position}", salary={self.salary})'

# Example Test Case
employee_data = [["John Doe", "Manager", 75000], ["Jane Smith", "Engineer", 80000]]
employees = [Employee(*data) for data in employee_data]
for emp in employees:
    print(emp)
# Output:
# Employee(name="John Doe", position="Manager", salary=75000)
# Employee(name="Jane Smith", position="Engineer", salary=80000)
