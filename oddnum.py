# Author Anjana Krishna
#date 14 oct 2024
# program to write n odd numbrs
limit=int(input("Enter the limit:"))
odd_number=1
count=0
while count<limit:
    print(odd_number,"\t",end="")
    count+=1
    odd_number+=2
