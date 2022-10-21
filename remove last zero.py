def num(a):
    i=0   
    b=[]
    while i<len(a):
        while a[i]>0 or a[i]<0:
            if a[i]%10!=0:
                b.append(a[i])
                break
            else:
                a[i]=a[i]//10
        i=i+1
    print(b)
num([1450,960000,1050,-1050])