y=0
n = int(input("Enter your range: "))
for i in range(n):
    x = int(input("Enter your numbers: "))  
    if x % 2 != 0:  
        y+=x
print(y)