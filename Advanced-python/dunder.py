# dunder or magic method 
# dunder -> __double underscore 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
    def __del__(self):
        print("Object is deleted")

p = Person("Mike", 24)

    