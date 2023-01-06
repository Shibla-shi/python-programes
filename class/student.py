class Student() :
    
    def display(self) :
        
       
        print("NAME :",self.name)
        print("ROLL_NO :",self.roll)
        print("COURSE :",self.course)
    def read(self):
        
        self.name=input("Enter the name : ")
        self.roll =input("Enter the roll number : ")
        self.course=input("Enter the course :")
obj1=Student()
obj2=Student()
obj1.read()
obj2.read()
obj1.display()
obj2.display()

