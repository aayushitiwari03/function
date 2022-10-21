def my(num):
    i=0
    max=0
    while i<len(num):
        j=0
        while j<len(num[i]):
            if len(num[i])>max:
                c=num[i]
                max=len(num[i])
            j+=1
        i+=1
    print("maximum lenght's list is",c,"and the lenght is ",max)
my([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])

