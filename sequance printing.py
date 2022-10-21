def myfun(numbers):
    i=1
    while i<=numbers:
        j=0
        while j<=i:
            d=2*j
            print("2","*",j,"=",d)
            j+=1
        print()
        i+=1
myfun(int(input("enter : ")))