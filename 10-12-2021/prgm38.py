# 38. Generate a list of four-digit numbers in a given range with all
# their digits even and the number is a perfect square.

def perfectSquares(l, r):

    for i in range(l, r+1):

        if (i ** (.5) == int(i ** (.5))) and (i % 2 == 0):
            print(i, end=" ")

l = int(input ("Enter a 4 digit lower limit:"))
r = int(input ("Enter a 4 digit upper limit:"))

perfectSquares(l, r)

