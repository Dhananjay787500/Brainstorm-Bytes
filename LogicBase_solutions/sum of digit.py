# Find the sum of the digits of an integer.

num = int(input('Enter number:'))
sum_of_digit = 0

while num > 0:
    sum_of_digit += num%10
    num //= 10
print(f'Sum of Digit: {sum_of_digit}')
