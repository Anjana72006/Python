#Author Anjana Krishna
# date 14 oct 2024
# program to write odd numbers up to n
limit=int(input("Enter the limit:"))
odd_number=1

while odd_number<=limit:
    print(odd_number,"\t",end="")
    odd_number+=2