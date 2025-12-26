# 1. Calculate the simple interest given principal, rate, and time.
principal = float(input('Enter principal:'))
rate = float(input('Enter Rate:'))
time = float(input('Enter time:'))

simple_interest = (principal * rate * time)/100

print(f'Simple Interest is: {simple_interest}')
