def bodymassindex(height,weight):
    return round(weight/height)

h=float(input("enter height in meters : "))
w=float(input("enter weight in KG : "))

print("welcome to BMI calculater")

bmi=bodymassindex(h,w)
print("your BMI is : ",bmi)
if bmi<=18.5:
    print("your weight is underweight")
elif 18.5< bmi <=24.9:
    print("your weight is overweight")
elif 24.9< bmi <=29.29:
    print("your weight is normal")
else:
    print("you are obese")

