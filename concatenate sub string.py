#program to concatenate, and print a string and access a sub-string from a given string.
#date 8 october 2024
#Anjana Krishna
first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
full_name=first_name+" "+last_name
print(full_name)
length=len(first_name)
print(length)
extracted_last_name=full_name[length+1:]
print(extracted_last_name)
extracted_first_name=full_name[:length]
print(extracted_first_name)