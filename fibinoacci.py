'''Author Anjana Krishna
Date 3 Dec 2024
program to print n fibinoacci numbers'''
def generate_fibinoacci(n):
    sequence=[]
    first_number,second_number=0,1
    for _ in range(n):

        sequence.append(first_number)
        first_number,second_number=second_number,first_number+second_number
    return sequence
print(generate_fibinoacci(10))
