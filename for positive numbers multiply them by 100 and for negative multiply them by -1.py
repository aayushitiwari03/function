def myfun(mul):
    i=0
    d=[]
    while i<4:
        a=int(input("enter : "))
        mul.append(a)
        if mul[i]%2==0:
            b=mul[i]*100
            d.append(b)
        else:
            c=mul[i]*-1
            d.append(c)
        i+=1
    print(d)
myfun([])