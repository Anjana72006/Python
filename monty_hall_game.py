'''Author Anjana Krishna
 Program for Monty Hall'''
import random
print("Welcome to the Monty Hall Game!")
n=int(input("Choose a door (1,2,3):"))
car=random.randrange(1,4)
while car==3:
    if n==1:
        print("The Host opens door 2,revealing a goat.")
        choice=input("Do you want to switch your choice? (yes/no):")
        if choice=="yes":
            print("Congratulations! You won the car.\nThe car was behind door 3.")
        elif choice=="no":
            print("You got a Goat.\nThe car was behind door 3.")
    elif n==2:
        print("The Host opens door 1,revealing a goat.")
        choice = input("Do you want to switch your choice? (yes/no):")
        if choice == "yes":
            print("Congratulations! You won the car.\nThe car was behind door 3.")
        elif choice == "no":
            print("You got a Goat.\nThe car was behind door 3.")
    else:
        print("The Host opens door 1,revealing a goat.")
        choice = input("Do you want to switch your choice? (yes/no):")
        if choice == "yes":
            print("You got a Goat.\nThe car was behind door 3.")
        elif choice == "no":
            print("Congratulations! You won the car.\nThe car was behind door 3.")
    break
while car==2:
    if n==1:
        print("The Host opens door 3,revealing a goat.")
        choice=input("Do you want to switch your choice? (yes/no):")
        if choice=="yes":
            print("Congratulations! You won the car.\nThe car was behind door 3.")
        elif choice=="no":
            print("You got a Goat.\nThe car was behind door 3.")
    elif n==2:
        print("The Host opens door 1,revealing a goat.")
        choice = input("Do you want to switch your choice? (yes/no):")
        if choice == "yes":
            print("You got a Goat.\nThe car was behind door 2.")
        elif choice == "no":
            print("Congratulations! You won the car.\nThe car was behind door 2.")
    else:
        print("The Host opens door 1,revealing a goat.")
        choice = input("Do you want to switch your choice? (yes/no):")
        if choice == "yes":
            print("Congratulations! You won the car.\nThe car was behind door 2.")
        elif choice == "no":
            print("You got a Goat.\nThe car was behind door 2.")
    break
while car==1:
    if n==1:
        print("The Host opens door 2,revealing a goat.")
        choice=input("Do you want to switch your choice? (yes/no):")
        if choice=="yes":
            print("You got a Goat.\nThe car was behind door 1.")
        elif choice=="no":
            print("Congratulations! You won the car.\nThe car was behind door 1.")
    elif n==2:
        print("The Host opens door 3,revealing a goat.")
        choice = input("Do you want to switch your choice? (yes/no):")
        if choice == "yes":
            print("Congratulations! You won the car.\nThe car was behind door 1.")
        elif choice == "no":
            print("You got a Goat.\nThe car was behind door 1.")
    else:
        print("The Host opens door 2,revealing a goat.")
        choice = input("Do you want to switch your choice? (yes/no):")
        if choice == "yes":
            print("Congratulations! You won the car.\nThe car was behind door 1.")
        elif choice == "no":
            print("You got a Goat.\nThe car was behind door 1.")
    break


