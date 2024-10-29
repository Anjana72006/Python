#Authhor Anjana Krishna
#date 29 ot 2024
#program to print a prime number
number= int (input("Enter a number:"))
isPrime =True
for i in range(2, number//2+1):
    if number%i==0:
        isPrime = False
        break
if isPrime:
    print(f"The given number {number} is prime")
else:
    print(f"The given number {number} not Prime")