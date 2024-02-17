a=[]
def add():
    n=int(input("enter how many pairs : "))
    for i in range(n):
        b={}
        name=input("enter your name : ")
        for i in a:
            if name in i['name']:
                print(f"{name} is exists")
        else:
                c={}
                for z in ['maths','science','english']:
                    s=int(input(f"enter  {z} for  {name} : "))
                    c[z]=s
                b['name']=name
                b['subject']=c
                a.append(b)
                print(a)
def display():
    def dis(subjects):
        for i in a:
            print(f"{i['name']} {i['subject'] [subjects]}")
    while True:
   
        print("1:display maths score \n"
            "2:display science score \n"
            "3:display english score \n"
            "4:exit\n")
        y=int(input("enter your choice: "))
        if y==4:
            break
        elif y==1:
            dis('maths')
        elif y==2:
            dis('science')
        elif y==3:
            dis('english')
            
     
while True:
    print(
    "1:Add  \n"
    "2:Display\n"
    "3:exit\n") 
    y=int(input("enter your choice: "))
    if y==3:
        break
    elif y==1:
        add()
    elif y==2:
        display()
        
        
    