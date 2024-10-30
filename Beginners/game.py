from random import randint

guessNumber = int(input("Enter the number between 1 to 5:"))
randomNumber = randint(1, 5)

if guessNumber == randomNumber:
    print("Won")
else:
    print("Failed")