# list is the object of python
subjects = ["C", "C++", "Python", "Java", "JavaScript"]

print(subjects)
print(subjects[0])
print(subjects[2:])
print(subjects[-1])

print("Python" in subjects)
print("c--" in subjects)
print(len(subjects))

subjects.append("Toc")
print(subjects)

n = input("Enter the list of numbers:")
list = n.split()
sum =0
for n in list:
    sum = sum + int(n)
print(sum)