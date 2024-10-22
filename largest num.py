'''
Author:Indhu Subash
Date:15-10-2024
'''
purchase_amount=int(input("Enter the purchase amount:"))
if(purchase_amount>500):
    discount=purchase_amount*0.20
    final_amount=purchase_amount-discount
    print("Final amount",final_amount)
elif(purchase_amount>=200 and purchase_amount<=500):
    discount=purchase_amount*0.10
    final_amount=purchase_amount-discount
    print("Final amount:",final_amount)
else:
    final_amount=purchase_amount
    print("Final amount:",final_amount)