class Employee() :
    
    def display(self) :
        
       
        print("salary is :",self.salary)
        print("grade is :",self.grade)
        print("department is :",self.department)
    def read(self):
        
        self.salary=int(input("Salary : "))
        self.grade=input("Grade : ")
        self.department=input("Department :")
obj1=Employee()
obj2=Employee()
obj3=Employee()
obj1.read()
obj2.read()
obj3.read()
obj1.display()
obj2.display()
obj3.display()
