#Author Anjana Krishna
#Date 29 oct 2024
#program to print no of vowels in a string
string_input=input("Enter a String")
vowels="aeiouAEIOU"
vowels_count=0
for char in string_input:
    if char in vowels:
        vowels_count+=1
print(f"The number of vowels in given string is:{vowels_count}")

