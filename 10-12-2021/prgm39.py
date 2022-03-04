# 39. Write lambda functions to find area of square, rectangle and triangle

t_area = lambda b,h : 0.5 * (b * h)
r_area = lambda len, ht : len*ht
s_area = lambda leng : leng * leng
print("Area of Triangle is:", t_area(10,20))
print("Area of Rectangle is:", r_area(30,20))
print("Area of Square is:", s_area(15))