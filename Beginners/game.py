from random import randint

for x in range(1,6):
    guessNumber = int(input("Enter the number between 1 to 5:"))
    randomNumber = randint(1, 5)
    
    if guessNumber == randomNumber:
        print("Won")
    else:
        print("Failed")
        print("Number was : ", randomNumber)