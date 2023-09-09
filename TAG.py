output = []
stack = []
stack_for_Ev = []
ThreeAddressCode = {}
ThreeAddressCodeCount = 1
remove_space = ''
operator = {'^': 1, '*': 2, '/': 2, '%': 3, '+': 4, '-': 4}
small_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
inString = input("Enter Input: ")
for i in inString:
    if i != " ":
        remove_space += i
remove_space
final_assign, equation = remove_space.split("=")
final_assign
equation
equation = equation[::-1]
equation
def stackPopingForParenthesis():
    for i in range(len(stack)):
        if stack[-1] != ')':
            output.append(stack.pop())

        else:
            stack.pop()
            return
for i in equation:
    if (i in capital_letter) or (i in small_letter) or ('0' < i < '9'):
        output.append(i)
    elif len(stack) == 0 and (i == '^' or i == '*' or i == '/' or i == '%' or i == '-' or i == '+'):
        stack.append(i)
    elif i == ')':
        stack.append(i)
    elif i == '(':
        stackPopingForParenthesis()
    elif i == '^' or i == '*' or i == '/' or i == '%' or i == '-' or i == '+':
        if stack[-1] == ')':
            stack.append(i)
        elif operator[i] <= operator[stack[-1]]:
            stack.append(i)
        else:
            output.append(stack.pop())
            stack.append(i)
output
stack
if len(stack):
    for i in range(len(stack)):
        output.append(stack.pop())
output
stack
prefix = output

for i in prefix:
    if (i in capital_letter) or (i in small_letter) or ('0' < i < '9'):
        stack_for_Ev.append(i)
    elif i == '^' or i == '*' or i == '/' or i == '-' or i == '+':
        v1 = stack_for_Ev.pop()
        v2 = stack_for_Ev.pop()
        ThreeAddressCode['T' + str(ThreeAddressCodeCount)] = v1 + i + v2
        stack_for_Ev.append(
            'T' + str(ThreeAddressCodeCount))
        ThreeAddressCodeCount += 1
print("Three Address code: ")
last_t = ''
for i, j in ThreeAddressCode.items():
    print(i, " = ", j)
    last_t = i

print(final_assign, " = ", last_t)