n=int(input("Enter any value:"))
def factorial(n):
    fact=1
    
    for i in range(1,n+1):
        fact*=i
    print(fact)
factorial(n)
factorial(1234)