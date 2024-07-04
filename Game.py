from random import randint
guessNumber = int(input("Enter the number 1-5:"))
randomNumber = randint(1, 5)

if guessNumber == randomNumber:
    print("Won")
else:
    print("Failed", randomNumber)