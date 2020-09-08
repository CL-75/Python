class School:
    def __init__(name, email, password, phone):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone


class Teacher(School):
    base_pay = ""
    subject = ""
    year_hired = ""

class Student(School):
    age = ""
    gpa = ""
    year_enrolled = ""
    address = ""
