#WAP to print the elements of a list in a single line.(list is the parameter)
cities=["kathmandu","butwal","chitwan","lalitpur","dhangadi"]
Marvel=("Iron-man","Captain America","Thor ","Bucky")
def print_element(obj):
    for i in obj:
        print(i,end=" ")
print_element(cities)
print_element(Marvel)