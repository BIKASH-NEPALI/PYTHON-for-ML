n=int(input("Enter number:"))
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
solution=factorial(n)
print(solution)