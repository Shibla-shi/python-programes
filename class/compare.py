class rectangle :
             width1=0
             length1=0
             area1=0
             perimeter=0
             def __init__(self,length,width):
                    self.length1=length
                    self.width1=width
             def cal_area(self) :
                    self.area1=self.length1*self.width1
                    print("area is :",self.area1)
                    return self.area1
             def cal_perimeter(self) :
                    self.perimeter1=2*(self.length1+self.width1)
                    print("perimeter is :",self.perimeter1)
def compare(a,b) :
        if a1==a2 :
            print("areas are equal")
        elif a1>a2 :
            print("area1 is greatest")
        else:
            print("area2 is greatest")
lengthf=int(input("enter the length of 1st rectangle:"))
widthf=int(input("enter the breadth of 1st rectangle:"))
lengths=int(input("enter the length of 2nd rectangle:"))
widths=int(input("enter the breadth of 2nd rectangle:"))
obj1=rectangle(lengthf,widthf)
a1=obj1.cal_area()
obj1.cal_perimeter()
obj2=rectangle(lengths,widths)
a2=obj2.cal_area()
obj2.cal_perimeter()
compare(a1,a2)
