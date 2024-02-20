a=int (input("enter your number : "))
b=int(input("enter your number : "))
print("before swap")
print(f"a = :{a}")

print(f"b = :{b}")
a=a+b 
b=a-b
a=a-b
print("after swap")

print(f"a = :{a}")
print(f"b = :{b}")