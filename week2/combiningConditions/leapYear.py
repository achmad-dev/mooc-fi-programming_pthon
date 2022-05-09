# Write your solution here
years = int(input('Please type in a year:'))
if years % 4 == 0:
    if years % 100 == 0:
        if years % 400 == 0:
            print('That year is a leap year')
        else:
            print('That year is not a leap year')
    else:
        print('That year is a leap year')
else:
    print('That year is not a leap year')
