'''Author Anjana Krishna
 Date 19 Nov 2024
 Program to remove duplicate elements from a list using a loop or set'''
list=[11,10,11,10,22,21]
unique_list=[]
for number in list:
    if number not in unique_list:
        unique_list.append(number)
print(unique_list)

