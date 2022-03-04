#D-List ordinal value of each element of a word (Hint:use ord() to get ordinal values)

word = (input("Enter a word:"))
nlist = [ord(i) for i in word]
print(nlist)