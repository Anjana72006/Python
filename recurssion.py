#factorial
def factorial(n):
    if n==0:
        return 1
    else:
       return n*factorial(n-1)
print(factorial(5))


#sum of two numbers
def add_numbers(x,y):
    if y==0:
        return x
    else:
        return add_numbers(x+1,y-1)
print(add_numbers(5,4))



#product of two numbers
def product_numbers(a,b):
    if b==1:
        return a
    else:
        return a+product_numbers(a,b-1)
print(product_numbers(5,4))



#gdc of two numbers
def gdc(n1,n2):
    if n1%n2==0:
        return n2
    else:
      return gdc(n2,n1%n2)
print(gdc(400,2))
