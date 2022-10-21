def str(num):
    i=0
    uc=0
    lc=0
    while i<len(num):
        b=num[i]
        j=0
        while j<len(b):
            if b[j]>="A" and b[j]<="Z":
                uc+=1
            elif b[j]>="a" and b[j]<="z":
                lc+=1
            j+=1
        i+=1
    print("upeercase letter is",uc)
    print("lowercase letter is",lc)
str(["The quick Brow Fox"])
