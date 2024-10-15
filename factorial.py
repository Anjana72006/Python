#Author Anjana Krishna
#Date 14 oct 2024
#program to determine entry fare
age=int(input("Enter your age:"))
if age<10:
    print("fare is 2")
elif age>=10 and age<60:
    print("fare is 10")
else:
    print("fare is 5")
