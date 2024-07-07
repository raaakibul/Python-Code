# pop and push
books = []
books.append("C")
books.append("Java")
books.append("Javascript")
print(books)

books.pop()
print("Now the top book is : ", books[-1])


# queue
from collections import deque

bank = deque(["C", "Java", "Javascript"])
print(bank)
bank.popleft()
print(bank)

