# Write your solution here
a = int(input("Please type in a temperature (F): "))
b = (a - 32) / 1.8
if (b < 0):
    print(f"{a} degrees Fahrenheit equals {b} degrees Celsius")
    print("Brr! It's cold in here!")
else:
    print(f"{a} degrees Fahrenheit equals {b} degrees Celsius")
