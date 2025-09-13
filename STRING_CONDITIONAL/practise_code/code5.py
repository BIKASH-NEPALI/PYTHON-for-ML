num1=int(input("Enter 1st number:\n"))
num2=int(input("Enter 2nd number:\n"))
num3=int(input("Enter 3rd number:\n"))
num4=int(input("Enter 4th number:\n"))
if(num1>num2 and num1>num3 and num1>num4):
    print("A is greatest")
elif(num2>num1 and num3 and num4):
    print("B is greatest")
elif(num3>num1 and num3>num2 and num3>num4):
    print("C is greatest")
else:
    print("D is greatest ")
    # more efficent way 
if(num1>num2 and num1>num3 and num1>num4):
    print("1st number is greater")
elif(num2>num3 and num2>num4):
    print("2nd number is greatest")
elif(num3>num4):
    print("3rd number is greatest")
else:
    print("4th number is greatest")