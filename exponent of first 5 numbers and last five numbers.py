def list():
    i=1
    b=[]
    c=[]
    while i<=30:
        if i<=5:
            a=i**2
            b.append(a)
        elif i>=25:
            d=i**2
            c.append(d)
        i+=1
    print(b,"(",c,")")
list()