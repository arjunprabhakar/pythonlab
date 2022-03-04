# 30.From a list of integers, create a list removing even numbers
a = [1, 2, 3, 4, 5, 6, 7, 8]
print("list:", a)
b =[ i for i in range(0, 8) if a[i] % 2 == 0]
print(b)



