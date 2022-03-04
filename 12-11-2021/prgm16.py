a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
x = ("+","_","*","/")
print(x)
ch = input("Enter the operator:")
if(ch=='/'):
    if(a==0):
        print("Division not possible")
    else:
        print("division answer=",a/b)
elif(ch=='+'):
        print("addition answer=",a+b)
elif (ch=='-'):
        print("subtraction answer=",abs(a-b))
elif (ch=='*'):
        print("multiplication answer=",a*b)
