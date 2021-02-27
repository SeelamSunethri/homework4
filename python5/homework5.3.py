import time
start =time.time()
def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
        #end=time.time()
        #print(start-end)
       
value = topten()
for i in value:
            
    print(i)
end=time.time()
print(end-start)