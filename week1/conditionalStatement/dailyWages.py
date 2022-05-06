# Write your solution here
a = float(input("Hourly wage: "))
b = int(input("Hours worked: "))
day = input("Day of the week: ")
Sunday = a * 2
if day == 'Sunday':
    print(f"Daily wages: {Sunday * b} euros")
else:
    print(f"Daily wages: {a * b} euros")
