import json

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Invalid grade! Must be between 0 and 100.")

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Student: {self.name}, Average Grade: {self.get_average():.2f}"

    def to_dict(self):
        return {'name': self.name, 'grades': self.grades}

    @staticmethod
    def from_dict(data):
        student = Student(data['name'])
        student.grades = data['grades']
        return student


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(Student(name))
        print(f"Student {name} has been added.")

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def add_grade_to_student(self, name, grade):
        student = self.find_student(name)
        if student:
            student.add_grade(grade)
            print(f"Grade {grade} added to {name}.")
        else:
            print(f"Student {name} not found.")

    def view_student_average(self, name):
        student = self.find_student(name)
        if student:
            print(f"{name}'s average grade is {student.get_average():.2f}.")
        else:
            print(f"Student {name} not found.")

    def save_to_file(self, filename):
        data = [student.to_dict() for student in self.students]
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Data saved to {filename}.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.students = [Student.from_dict(item) for item in data]
            print(f"Data loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found.")


# Example of how the system works:
def main():
    system = StudentManagementSystem()

    # Add students
    system.add_student("Alice")
    system.add_student("Bob")

    # Assign grades
    system.add_grade_to_student("Alice", 85)
    system.add_grade_to_student("Alice", 92)
    system.add_grade_to_student("Bob", 76)

    # View student averages
    system.view_student_average("Alice")
    system.view_student_average("Bob")

    # Save and load data
    system.save_to_file("students.json")
    system.load_from_file("students.json")

    # Check data after loading
    system.view_student_average("Alice")
    system.view_student_average("Bob")


if __name__ == "__main__":
    main()
