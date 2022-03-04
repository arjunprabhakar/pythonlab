   #Find biggest of 3 numbers entered
a = int(input("Enter three numbers:"))
b = int(input())
c = int(input())
if a > b and a>c:
        greater = a
elif b>a and b>c:
        greater = b
else:
    greater = c
print("Greater: ", +greater)
