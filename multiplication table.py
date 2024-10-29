#AuthOR Anjana Krishna
#Date 29 oct 2024
#program to print multiplication table of a number upto 12
number=int(input("Enter a number:"))
limit=int(input ("Enter your limit:"))
for i in range(1,limit+1):
    print(f"{number}* {i}\t={number*i}")
