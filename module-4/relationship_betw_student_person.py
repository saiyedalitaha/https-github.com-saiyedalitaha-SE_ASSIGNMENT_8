# Define the Person class (base class)
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

# Define the Student class (derived class)
class Student(Person):
    def __init__(self, name, age, gender, student_id, major):
        # Call the constructor of the parent (Person) class
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.major = major

    def display_student_info(self):
        # Display student-specific info
        self.display_info()  # Call the parent class method
        print(f"Student ID: {self.student_id}, Major: {self.major}")

# Create an instance of Student
student_1 = Student("Alice", 20, "Female", "S12345", "Computer Science")

# Display student's information
student_1.display_student_info()
