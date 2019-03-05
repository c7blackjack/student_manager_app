students = []

class Student:

    school_name = "Petsworth Elementary"

    def __init__(self, name, student_id = 332):
        self.name = name
        self.student_id = student_id
        students.append(self)


    def __str__(self):
        return "Student"


    def get_name_capitalize(self):
        return self.name.capitalize()


    def get_school_name(self):
        return self.school_name










