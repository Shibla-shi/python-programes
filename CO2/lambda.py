sqr=lambda x:x*x
rect=lambda l,br:l*br
tri=lambda b,h:0.5*b*h

x=int(input("enter side of square: "))
print("Area of square is :",x,"*",x,"=",sqr(x))
l=int(input("enter length of rectangle: "))
br=int(input("enter breadth of rectangle: "))
print("Area of rectangle is :",l,"*",br,"=",rect(l,br))
b=int(input("enter base of triangle: "))
h=int(input("enter height of triangle: "))
print("Area of triangle is :",b, "*",h,"=",tri(b,h))
