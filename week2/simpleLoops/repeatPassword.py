# Write your solution here
password = input('Password:')
while True:
    repeat = input('Repeat password:')
    if password == repeat:
        break
    print('They do not match!')
print('User account created!')
