def myfunction(num):
    i=0
    while i<len(num):
        square= num[i]**2
        print(square,end="")
        i+=1
myfunction([9,1,1,9])