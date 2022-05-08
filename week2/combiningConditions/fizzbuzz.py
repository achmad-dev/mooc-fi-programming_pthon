# Write your solution here
Number = int(input('Number:'))
if Number % 3 == 0 and Number % 5 == 0:
    print('FizzBuzz')
elif Number % 3 == 0:
    print('Fizz')
elif Number % 5 == 0:
    print('Buzz')
