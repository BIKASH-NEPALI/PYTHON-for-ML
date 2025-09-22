
Task=[]
def add_task():
    task=input("Enter task you want to add\n").lower().strip()
    Task.append(task)
    print("Task added succesfully!")
def view_task():
    print("Your tasks are :")
    for el in Task:
        print(el)
    
def remove_task():
    rmv=input("Enter task your wanna remove in list\n").lower().strip()
    if rmv==Task:
        Task.remove(rmv)
    else:
        print("Task is not in the list ")
        
    
print("Welcome to task Manager!\n")

while True:
    user_input=input("enter commmand (view task,add task,remove task)\n").lower().strip()
    if user_input=="view task":
        view_task()
    elif user_input=="remove task":
        remove_task()
    elif user_input=="add task":
        add_task()
    elif user_input=="exit":
        print("Have a nice day,sir!\n")
        break
    else:
        print("Invalid Error!")
    
    
        