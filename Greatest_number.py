x1=int(input("enter first number"))
x2=int(input("enter second number"))
x3=int(input("enter third number"))
if x1>x2 and x1>x3:
    print(str(x1)+" is grteatest number")
elif x2>x3 and x2>x1:
    print(str(x2)+" is greatest number")
else:
    print(str(x3)+" is greatest number")
