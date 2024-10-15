#Author Anjana Krishna
# date 14 oct 2024
# program to write sum of digit of a number
num=int(input("Enter a number:"))
sum=0
while num>0:
    r=num%10
    num=num//10
    sum=sum+r
print("Sum of digits:",sum)
