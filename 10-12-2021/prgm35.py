# 35. Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add‘ly’.
# (Use user defined function)

a = input("Enter a string:")
def lying(str1):
    if a[-3:] != 'ing':
        print(a + "ing")
    else:
        print(a + "ly")
lying(a)
