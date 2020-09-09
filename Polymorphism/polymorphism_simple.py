class School:
    def __init__(self, name, username, password)
        self.name = name
        self.username = username
        self.password = password

        def system_login():
            sys_name = input("Enter Your Name: ")
            sys_username = input("Enter Your Username: ")
            sys_password = input("Enter Your Password: ")
                if (sys_username == self.username and sys_password == self.password):
                    print("Welcome Back {}!".format(sys_name))
                else if (sys_username != self.username and sys_password == self.password):
                    print("Username is incorrect.")
                else if (sys_username == self.username and sys_password != self.password):
                    print("Password is incorrect.")
                else 
                    print("Username and Password are Incorrect.")



class Teacher(School):
    base_pay = ""
    subject = ""
    teacherID = ""

        def system_login(self):
            sys_name = input("Enter Your Name: ")
            sys_username = input("Enter Your Username: ")
            sys_teacherID= input("Enter Your Teacher ID: ")
            if (sys_username == self.username and sys_teacherID == self.teacherID):
                    print("Welcome Back {}!".format(sys_name))
                else if (sys_username != self.username and sys_teacherID == self.teacherID):
                    print("Username is incorrect.")
                else if (sys_username == self.username and sys_teacherID != self.teacherID):
                    print("Teacher ID is incorrect.")
                else 
                    print("Teacher ID and Password are Incorrect.")
  

class Student(School):
    age = ""
    gpa = ""
    email = ""
    studentID = ""
    address = ""
    
    def system_login(self):
            sys_email = input("Enter Your Email: ")
            sys_teacherID= input("Enter Your Student ID: ")
            if (sys_email == self.email and sys_studentID == self.studentID):
                    print("Welcome Back {}!".format(sys_name))
                else if (sys_email != self.email and sys_studentID == self.studentID):
                    print("Email is incorrect.")
                else if (sys_email == self.email and sys_studentID != self.studentID):
                    print("Student ID is incorrect.")
                else 
                    print("Email and Student ID are Incorrect.")
  












    
