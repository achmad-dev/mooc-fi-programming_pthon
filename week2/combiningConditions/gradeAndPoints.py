# Write your solution here
Grade = int(input('How many points [0-100]:'))
if Grade < 0 or Grade > 100:
    print('Grade: impossible!')
elif Grade < 50:
    print('Grade: fail')
elif Grade >= 50 and Grade < 60:
    print('Grade: 1')
elif Grade >= 60 and Grade < 70:
    print('Grade: 2')
elif Grade >= 70 and Grade < 80:
    print('Grade: 3')
elif Grade >= 80 and Grade < 90:
    print('Grade: 4')
elif Grade >= 90:
    print('Grade: 5')
