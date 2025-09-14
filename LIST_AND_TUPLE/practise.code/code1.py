# WAP to ask the user to enter name of their 3 favourite movies and store them in a list.
print("Enter your favourite movies\n")
movie1=input("Enter your first favourite movie name\n")
movie2=input("Enter your second favourite movie name\n")
movie3=input("Enter your Third favourite movie name\n")
movies_list=[movie1, movie2, movie3]
print("Your favourite movies list are:", movies_list)
additional=input("Do you have any other movie?")
movies_list.append(additional)
print(movies_list)