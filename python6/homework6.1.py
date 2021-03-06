import sys,os
filename = input("name of the file:")
while os.path.exists(filename) == True:
    print("True")
else:
    print("False")