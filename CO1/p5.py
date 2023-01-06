def add(a,b):
    c=a+b
    print("sum is:",c)
def subtract(a,b):
    c=a-b
    print("difference is:",c)
def multiply(a,b):
    c=a*b
    print("product is:",c)
def divide(a,b):
    c=a/b
    print("quotient is:",c)
x=int(input("enter the first number : "))
y=int(input("enter the second number : "))
z=int(input("select the operation : "))
if(z=='+') :
    add(x,y)
elif(z=='-') :
   subtract(x,y)    
elif(z=='*') :
   multiply(x,y)
elif(z=='/') :
    divide(x,y)
    
