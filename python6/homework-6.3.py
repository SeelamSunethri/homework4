import os
path = input("please enter Path: ")
filename = input("name of the file: ")
full_path=[]
for r , d, f in os.walk(path):
    if filename in f:
        full_path.append(os.path.join(r,filename))
if full_path == []:
    print("FileisnotFound.")
else:
    print("Full Path File"+str(full_path[0])