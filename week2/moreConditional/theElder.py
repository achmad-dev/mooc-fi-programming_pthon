# Write your solution here
print('Person 1:')
name1 = input('Name:')
agePerson1 = int(input('Age:'))
print('Person 2:')
name2 = input('Name:')
agePerson2 = int(input('Age:'))
if agePerson1 > agePerson2:
    print(f'The elder is {name1}')
elif agePerson2 > agePerson1:
    print(f'The elder is {name2}')
else:
    print(f'{name1} and {name2} are the same age')
