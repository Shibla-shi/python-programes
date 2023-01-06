class Calculator():
    def add(self):
        self.a=int(input("enter a:"))
        self.b=int(input("enter b:"))
        self.sum=self.a+self.b
        print("sum is :",self.sum)

    def dif(self):
        
        self.a=int(input("enter a:"))
        self.b=int(input("enter b:"))
        self.min=self.a-self.b
        print("difference is :",self.min)

    def mul(self):
        
        self.a=int(input("enter a:"))
        self.b=int(input("enter b:"))
        self.prod=self.a*self.b
        print("product is :",self.prod)

    def div(self):
        self.a=int(input("enter a:"))
        self.b=int(input("enter b:"))
        self.rem=self.a/self.b
        print("reminder is :",self.rem)

    def mod(self):
        self.a=int(input("enter a:"))
        self.b=int(input("enter b:"))
        self.md=self.a%self.b
        print("modulus is :",self.md)

cal=Calculator()
print("1.SUM\n2.DIFFERENCE\n3.PRODUCT\n4.REMINDER\n5.MODULUS ")
ch=int(input("enter your choice:"))
if ch==1:
    cal.add()
elif ch==2:
    cal.dif()
elif ch==3:
    cal.mul()
elif ch==4:
    cal.div()
elif ch==5:
    cal.mod()
else:
    print("Wrong Choice!!!")
