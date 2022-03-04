# 34. Program to find the factorial of a given number using user-defined function.

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact
number = int(input("Enter the range:"))
result = factorial(number)
print("fact=", result)
