class rect :
 
    def area(self,length,breadth,area) :
        self.length=length
        self.breadth=breadth
        self.area=length*breadth
        print(self.area)
r1=rect()
x=input("length is :")
y=input("breadth is : ")
z=input("area is :")
r1.area(x,y,z)
