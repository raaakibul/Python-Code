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
    