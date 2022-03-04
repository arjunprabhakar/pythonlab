yeara = 2021
yearb= int(input("Enter the limit:"))
print("list of year")
for year in range(yeara, yearb):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print(year)
