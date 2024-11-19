
list1=[]
list2=[]
#know the list size and input both list from user
size_list1=int(input("Enter the size of list 1:"))
print("Enter the elements of list1:")
for i in range (size_list1):
    list1.append(int(input()))
size_list2=int(input("Enter the size of list 2:"))
print("Enter the elements of list 2:")
for i in range (size_list2):
    list2.append(int(input()))
print(list1,list2)
#combine both list (concatenate)
combined_list=list1+list2
print("Combined list=",combined_list)

even_list=[]
odd_list=[]
for i in combined_list:

    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list,odd_list)
even_list.sort()
odd_list.sort()
merged_list=(even_list+odd_list)
print(merged_list)


