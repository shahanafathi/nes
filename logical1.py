a=[]
n=int(input("enter number"))
for i in range(n):
    x=int(input("enter your number"))
    a.append(x)
    print(a)
    # b=(len(a))
    # print(b)
    a.sort()
b=len(a)
c=b//2
f1=a[:c]
f2=a[c:]
f2.reverse()
print(f1+f2)   
    