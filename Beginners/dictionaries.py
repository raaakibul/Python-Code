student = {
    "101": "Test1",
    "102": "Test2",
    "103": "Test3",
    "104": "Test4",
}
print(student["101"])
print(student)
print(student.get("104"))
print(student.get("106", "Not a valid key"))