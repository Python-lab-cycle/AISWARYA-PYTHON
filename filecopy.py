file1=input("Enter the sourse file to be copied: ")
file2=input("Enter the destination file name: ")
f1=open(file1,"r")
f2=open(file2,"w")
for line in f1.readline():
    f2.write(line)
f1.close()
f1=open(file1,"r")
line=f1.read()
print("Line= ",line)

    
