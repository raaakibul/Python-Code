# classes and objects

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        print("Name:" ,name)
        print("Age:" ,age)
        print("Height:", height)
        print("\n")
        

p1 = Person("Mike", 23, 180)
p2 = Person("Bob",34,145)
p3 = Person("Trot", 45,156)