class rectangle() :
    def __init__(self,breadth,length) :
        self.breadth=breadth
        self.length=length
    def area(self) :
        return self.breadth*self.length
    def peri(self) :
        return 2*(self.breadth+self.length)
a=int(input("enter the length of rectangle:"))
b=int(input("enter the breadth of rectangle:"))
obj=rectangle(a,b)
obj1=rectangle(a,b)
print("area of rectangle:",obj.area())
print("perimeter of rectangle:",obj1.peri())
