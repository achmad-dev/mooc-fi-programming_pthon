# Write your solution here
weeks = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
sum_weeks = float(input("How much money do you spend on groceries in a week?"))
a = (weeks * price) + sum_weeks
print("Average food expenditure:")
print(f"Daily: {a/7} euros")
print(f"Weekly: {a} euros")
