class Acq:
    def __init__(self,r):
        self.r=r
    def circle(self):
        print(f"Area of a circle : {3.14*self.r**2}")
        print(f"circumference of a circle  : {2*3.14*self.r}")    
class Acw:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    
    def  display(self):
        print(f"{self.name}\n{self.age}\n{self.address}")
class Acr:
    def __init__(self,title,auther,published,):
        self .title=title
        self .auther=auther
        self.published=published
    def  display(self):
        print(f"{self.title}\n{self.auther}\n{self.published}") 
     
             
while True:
        print("1:calculate the circle \n"
              "2:Display  person details \n"
              "3:display book information \n"
              "4:Exit \n")
        x=int(input("Enter your choice : "))
        if x==4:
            break
        elif x==1:
        
            r=int(input("enter your radius :  "))
            a=Acq(r)
            a.circle()
        elif x==2: 
            name=input("enter person's name : ")
            age=int(input("enter person's age : "))
            address=(input("enter person's address : "))
            a=Acw(name,age,address)
            a.display()
        elif x==3: 
            title=(input("enter the book's title : "  ))
            auther=(input("enter the book's auther : "  ))
            published=int(input("enter the book's published year : "  ))
            a=Acr(title,auther,published)
            a.display()
    