# The Greatest Common Divisor (GCD), also known as the Highest Common Factor (HCF), is the largest positive integer that divides two or more numbers without leaving a remainder.


import math

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

gcd = math.gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is {gcd}.")