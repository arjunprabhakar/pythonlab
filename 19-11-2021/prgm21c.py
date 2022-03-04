#C-Form a list of vowels selected from a given word

n = input("Enter a word:")
nlist = [i for i in n if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U"]

print(nlist)