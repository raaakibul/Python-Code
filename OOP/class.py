# class -- template 
class Student:
    roll = ""
    gpa = ""

s1 = Student()
s2 = Student()
print(isinstance(s1, Student))

s1.roll = "123456"
s1.gpa ="3.60"
s2.roll = "123457"
s2.gpa = "3.70"
print(f"Roll: {s1.roll}, GPA: {s1.gpa}")
print(f"Roll: {s2.roll}, GPA: {s2.gpa}")