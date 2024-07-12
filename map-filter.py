# map-- especially for using list 
def square(x):
    return x*x
number = [1,2,3,4,5,6,7,8,9,10]

result = list(map(square,number))
print(result)

# filter 
# number = [1,2,3,4,5,6,7,8,9,10]
res =  list(filter(lambda x:x%2==0,number))
print(res)