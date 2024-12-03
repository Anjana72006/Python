''' Author Anjana Krishna
 Date 30 Nov 2024
 Program to check given number is a valid mobile number'''
def is_mobile_number(n):
    n=input("Enter a number:")
    if len(n)==10 and n[0] in "7,8,9":
        print("The given number is a valid mobile number")

    else:
        print("The given number is not a valid mobile number")
is_mobile_number('n')

