def add(l):
    i=0
    m=0
    s=0
    while i<len(l):
        if (l[i])>m:
            s=m
            m=l[i]
        i+=1
    print(m,"+",s,"=",m+s)
add([50,40,23,56,70,12,5,10,7])







