def list(num):
    i=0
    max=0
    while i<3:
        a=int(input("enter :"))
        num.append(a)
        if num[i]>max:
            max=num[i]
        i+=1
    print("max number is ",max)
list([])
