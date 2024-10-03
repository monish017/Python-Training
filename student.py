class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def __repr__(self):
        return f'name: "{self.name}", age: {self.age}, grades: {self.grades}'

# Example Test Case
student = Student(name="Alice", age=20, grades=[90, 85, 88])
print(student)  # Output: name: "Alice", age: 20, grades: [90, 85, 88]
