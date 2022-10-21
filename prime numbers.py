def check(num):
    a=1
    while a<=num:
        count=0
        i=1
        while i<=a:
            if a%i==0:
                count=count+1
            i+=1
        if count==2:
                print(a)
        a+=1
check(int(input("enter the number : ")))

