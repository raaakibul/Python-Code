numbers = [18,16,22,99,26,11,54]

# new_list = []

# for number in numbers:
#     if number % 2 ==0:
#         new_list.append(number)

# print(new_list)

# another way 

new_list = [x for x in numbers if x %2 ==0]
print(new_list)