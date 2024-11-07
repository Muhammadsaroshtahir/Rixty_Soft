a= int(input("enter no 1:"))
b= int(input("enter no 2:"))
c= int(input("enter no 3:"))
if b>a:
    print("b is greater than a")
elif a==b:
    print("both a same")
else : 
    print("a is greater than b")

if a>b and c>a:
    print("both conditions are True")

if a>b or c>a:
    print("at least one is condition is True")

if not a>b:
    print("a is not greater than b")

if b>a:
    pass