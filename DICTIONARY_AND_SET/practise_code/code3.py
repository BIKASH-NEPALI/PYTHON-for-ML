# WAP to enter marks of 3 subjects from user tan store them in a dictionary
#start with an empty dictionary and add one by one. use subject name as key and marks as value.
dictionary={ }
Math=int(input("Enter marks obtained in math\n"))
pysics=int(input("Enter marks obtained in physics\n"))
Bio=int(input("Enter marks obtained in Bio\n"))
dictionary.update({"physics":pysics,"bio":Bio,"math":Math})
print(dictionary)