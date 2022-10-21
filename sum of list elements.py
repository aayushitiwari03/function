def myfun(num):
    i=0
    c=[]
    while i<len(num):
        b=str(num[i])
        sum=0
        j=0
        while j<len(b):
            sum=sum+(int(b[j]))
            j+=1
        c.append((sum))
        i+=1
    print(c)
myfun([15, 81, 11, 234])

