def rev(list):
    i=0
    while i<len(list):
        a=list[i]
        b=len(a)
        c=" "
        j=b-1
        while j>-1:
            c=c+a[j]
            j-=1
        print(c)
        i+=1
rev(["1234abcd"])