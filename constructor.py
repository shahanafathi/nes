# Parameterized Constructor



class Emp:

    def __init__(self,name,id,contact,salary):
        self.name=name
        self.id=id
        self.contact=contact
        self.salary=salary



    def display(self):
    
    
            print(f"name:{self.name}\nid: {self.id}\ncontact: {self.contact}\nsalary: {self.salary}")
name=(input("enter your name : "))


id=int(input("enter your id : "))
contact=(input("enter your contact no:") )

a=len(contact)
if a<=10 or a>=10:
    b=contact
else:
    print("its not have 10 numbers")
salary=int(input("enter your salary :"))       
a=Emp(name,id,b,salary)
a.display()

#  Non-Parameterized Constructor 

class Emp:  
   
    def __init__(self):  
        print(" non parametrized ")          
    def dis(self, name,id,b,salary):  
        print( name,id,b,salary)  
c=Emp()
name=(input("enter your name : "))
id=int(input("enter your id : "))
contact=(input("enter your contact no:") )
a=len(contact)
if a<=10 or a>=10:
    b=contact
else:
    print("its not have 10 numbers")
salary=int(input("enter your salary :"))     
c.dis(name,id,b,salary)


# Default Constructor

class Emp:
    
    name=(input("enter your name : "))
    id=int(input("enter your id : "))
    contact=(input("enter your contact no:") )
    salary=int(input("enter your salary :")) 
    
    def display(self):
        print(self.name,self.id,self.contact,self.salary)
        

a=Emp()     
a.display()







