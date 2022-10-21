def myfun(count):
    i=0
    neg=0
    pos=0
    while i<len(count):
        if count[i]<0:
            neg+=1
        else:
            pos+=1
        i+=1
    print("negative numbers is",neg)
    print("positive numbers is",pos)
myfun( [2, -7, 5, -64, -14])

