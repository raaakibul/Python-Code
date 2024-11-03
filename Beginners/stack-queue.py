books = []
books.append("C")
books.append("C++")
books.append("Python")
print(books)

books.pop()
print(" now the top book is:" ,books[-1])

books.pop()
print(" now the top book is:" ,books[-1])

books.pop()
if not books:
    print(" no books")

# Queue 

from collections import deque

bank = deque(["A", "B", "C", "D"])
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()

if not bank:
    print(" no bank")