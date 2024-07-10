# xargs , xxargs
def student(id, name):
    print(id,name)
    
student(101, "Rakibul")

# xargs 
def person(*details):
    print(details)

person(101, "A")
person(102, "B", "Rakibul")