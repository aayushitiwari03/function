def check(age):
    if age<14:
        print("Kids drink toddy")
    elif age<18 and age>14:
        print("Teens drink coke")
    elif age>18 and age<21:
        print("Young adults drink beer")
    elif age>21 :
        print("Adults drink whisky")
check(int(input("enter : ")))