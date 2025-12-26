# Swap two numbers without temporary variable (arithmetic operators)

a = int(input('Enter 1st Swap no:'))
b = int(input('Enter 2nd Swap no:'))

print("Before Swap --> a =", a, ", b = ", b)

a = a + b
b = a - b
a = a - b

print("After Swap --> a =", a, ", b = ", b)
