# 26. Create a list of colors from comma-separated color names entered by user. Display first and last colors.
a = input("Enter the colors separated with commas")
b = a.split(",")
print("1st element", b[0])
print("last element", b[-1])

