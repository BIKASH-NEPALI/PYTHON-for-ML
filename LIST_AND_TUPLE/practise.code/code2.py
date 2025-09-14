#WAP  to check if a list of a palindrome of elements.
list1=['sammy', 'prabin','prabin','sammy'
]
list2=['arjun','deepika','ram','prabin']
cpy_ls1=list1.copy()
cpy_ls1.reverse()
cpy_ls2=list2.copy()
cpy_ls2.reverse()
if(list1==cpy_ls1):
    print("This is a palindrome")
else:
    print("This is not a palindrome")
if(list2==cpy_ls2):
    print("this is palindrome")
else:
    print("This is not a palindrome")


