# Write your solution here
a = int(input("Number 1: "))
b = int(input("Number 2: "))
operator = input("Operation: ")
if operator == 'add':
    print(f"{a} + {b} = {a + b}")
elif operator == 'multiply':
    print(f"{a} * {b} = {a * b}")
elif operator == 'subtract':
    print(f"{a} - {b} = {a - b}")
