file = open("e:\Programming-Hero-Code\Python-code\student.txt","r+")
text = file.read()

print(text)

size = len(text)
print("The length is = ",size)

file.close()