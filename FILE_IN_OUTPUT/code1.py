# a,w mode .if file doesn't exist it make a new one
f=open("auto_file.txt","w")
write=f.write("Hello this is a new file created by w mode")
f.close()