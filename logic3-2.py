a= []
b = []

n = int(input("Enter your range: "))
for i in range(n):
    f = int(input("Enter your number: "))
    a.append(f)
a.sort()
l = max(a)
for i in range(1, l):
    if i>0:  
        if i not in a:
            b.append(i)
            v=min(b)
    # print(f"first missing num:{v}")
    # break        
            print(f" missing num:{v}")
            break
   
    else:
        print("negative num")
