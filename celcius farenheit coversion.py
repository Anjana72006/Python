#Author Anjana Krishna
#Date 22-10-2024
#program to convert celcius to farenheit and vice versa
temp=int(input("Enter  temperature:"))
T=(input("Is this in (C)elsius or in (F)arenheit? "))
if T=='C':
    f=9/5*temp+32
    print(temp ," celcius is ",f,"farenheit")
else:
    c=5/9*(temp-32)
    print(temp,"farenheit is",c,"celcius")
