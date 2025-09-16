#Search for a number x in this tuple using loop:
elements=(23,56,78,35,86,25,77,89)
num=int(input("Enter elemtent you wants to search "))
i=0
while i<len(elements):
    if num==elements[i]:
        print("Element is found")
        break
    else:
        print("Element is not found")
        break
    i+=1
    #Error in this code.