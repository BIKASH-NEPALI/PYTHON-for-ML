#RECURSIVE  function to print all elements in a list.
elements=["Hydrogen","Helium","lithium","brellium"]
def print_el(elements,n=0 ):
    if n==len(elements):
        return 0
    print(elements[n])
    print_el(elements,n+1)
print_el(elements)