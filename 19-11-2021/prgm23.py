#Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.
list1 = []
n = int(input("Enter a limit:"))
print("Enter the list of integers:")
for i in range(n):
    ele = int(input())
    if ele > 100:
        list1.append('d')
    else:
        list1.append(ele)
print(list1)
