# 40.count the number of characters in a string

a = input("Enter the string:")
count = 0
for i in range(0, len(a)):
    if (a[i] != ' '):
        count = count + 1
print("Total number of characters in a string: " + str(count))
