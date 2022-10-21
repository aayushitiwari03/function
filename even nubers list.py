def even(num):
    i=0
    even=[]
    while i<len(num):
        if num[i]%2==0:
            even.append(num[i])
        i+=1
    print(even)
even([1, 2, 3, 4, 5, 6, 7, 8, 9])