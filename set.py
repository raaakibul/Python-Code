number = {1,2,3,4,5,6,7,8,9,10}
print(number)
number2 = set([4,5,6])
number2.add(1)
print(number2)
number2.remove(1)
print(number2)
print(4 in number2)
print(5 not in number2)

print(number | number2)
print(number & number2)
print(number - number2)
