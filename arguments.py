# xargs , xxargs
def student(id, name):
    print(id,name)
    
student(101, "Rakibul")

# xargs 
def person(*details):
    print(details)

person(101, "A")
person(102, "B", "Rakibul")

def add(*numbers):
    sum =0
    for num in numbers:
        sum += num
    print(sum)
    
add(101, 120)
add(100,1001,10001)

def students(**details):
    print(details)
    
students(id=101,name="Student")