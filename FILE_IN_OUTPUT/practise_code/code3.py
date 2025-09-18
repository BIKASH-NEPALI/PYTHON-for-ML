with("C:\BIKASH NEPALI\PYTHON-for-ML\FILE_IN_OUTPUT\practise_code\demo.txt","r")as  f:
    data=f.read()
    if(data.find("learning")!=-1):
        print("found")
    else:
        print("not found")