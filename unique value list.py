def unique(list):
    i=0
    dif=[]
    while i<len(list):
        if list[i] not in dif:
            dif.append(list[i])
        i+=1
    print(dif)
unique([1,2,3,3,3,3,4,5])

