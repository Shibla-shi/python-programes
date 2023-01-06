print("enter 3 numbers")
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a>b and a>c :
    print(a,"is largest")
elif b>a and a>c :
    print(b,"is greatest")
else :
    print(c,"is greatest")
