# class -- template 
class Student:
    roll = ""
    gpa = ""

s1 = Student()
print(isinstance(s1, Student))

s1.roll = "123456"
s1.gpa ="3.60"
print(f"Roll: {s1.roll}, GPA: {s1.gpa}")