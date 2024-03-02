class Shop:
    def __init__ (self,id,quantityitem ,priceitem):
        self.id=id
        self.quantityitem=quantityitem
        self.priceitem=priceitem
 
    def gold(self):
        total=priceitem*quantityitem
        discount = total* 0.2
        finalprice=total-discount
        print(f"Price of a item : {total}")
        print (f"Discode for gold customer : {discount}")
        print (f" After discode  : {finalprice}")
    def silver(self):
        total=priceitem*quantityitem
        discount = total* 0.1
        finalprice=total-discount
        print(f"Price of a item : {total}")
        print (f"Discode for gold customer : {discount}")
        print (f" After discode  : {finalprice}")
    def exit(self):
        print("Thank you for using the Billing System. Goodbye!")
        exit()   
    

    

while True:
        id=int(input("enter your id : "))
        quantityitem=int(input("enter quantity iteam :"))
        priceitem=int(input("enter price iteam : "))
        print("Welcome to the Billing System")
        print("1:gold\n"
              "2:silver \n"
              "3:exit \n")
        x=int(input("Choose your customer type : "))
        if x==3:
            print("Thank you for using the Billing System. Goodbye!")
            break
        elif x==1:
            a=Shop(id, quantityitem, priceitem)
            a.gold()
            while True:
                print("1:yes\n"
                    "2:no \n")
                x=int(input("Do you want to continue? : "))
                if x==2:
                    
                    a.exit()
                elif x==1:
                    break
                
        elif x==2:
            a=Shop(id, quantityitem, priceitem)
            a.silver()
            while True:
                print("1:yes\n"
                    "2:no \n")
                x=int(input("Enter your choice : "))
                if x==2:
                    a.exit()      
                elif x==1:
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
    


