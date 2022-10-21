def shownumbers(limit):
    i=0
    while i<=limit:
        if i%2==0:
            print(i, "even")
        else:
            print(i,"odd")
        i+=1
shownumbers(int(input("enter the limit : ")))