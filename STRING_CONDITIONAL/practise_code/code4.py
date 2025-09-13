#WAP  a program to find greatest of threee numbers
a=int(input("Enter first number\n"))
b=int(input("Enter second number\n"))
c=int(input("Enter third number\n"))
if(a>b):
    if(a>c):
        print("A is greatest")
elif(b>a and b>c):
    print("B ia greatest")
else:
    print("C is greatest")
       