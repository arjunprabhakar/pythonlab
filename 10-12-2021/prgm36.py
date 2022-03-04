# 36. Generate all factors of a number. (Use user defined function)

a = int(input("Enter a number:"))
def factor(num):
    for i in range(1, num+1):
        if num % i == 0:
            print(i)
factor(a)
