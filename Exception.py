# number = int(input("Enter number: "))

# result = 20/ number
# print(result)

try:
    list = [20,0,30]
    result = list[0]/list[1]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Division by zero is not possible")
        