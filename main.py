import json
from datetime import datetime

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.attendance = []

    def add_grade(self, subject, grade):
        self.grades.append({"subject":subject, "grade":grade})

    def add_attendance(self, date = datetime.now().strftime("%Y-%m-%d")):
        self.attendance.append({"date": date, "status": "Keldi"})


    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grades": self.grades,
            "attendance": self.attendance
        }

class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []


    def add_student(self, student):
        self.students.append(student)


    def save_to_json(self, filename):
        data = [student.to_dict() for student in self.students]
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            return data

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

c = Classroom("Programming")
student1 = Student(1, "Ali")
student1.add_grade("Matematika", 85)
student1.add_attendance()

student2 = Student(2, "Vali")
student2.add_grade("Fizika", 90)
student2.add_attendance()

c.add_student(student1)
c.add_student(student2)

c.save_to_json("students.json")

new_c = Classroom("Coding")
new_c.load_from_json("students.json")

c.add_student(student1)
c.find_student(student1.student_id)

student = new_c.find_student(1)
if student:
    print(f"O'quvchi: {student.name}, Baholar: {student.grades}")
