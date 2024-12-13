'''Author Anjana Krishna
 program for stick game'''
def game():
    print("Rules: A player can only pick 1,2 or 3 sticks.")
    print("Game Started!")
    player1=input("Enter the name of first player:")
    player2=input("Enter the name of second player:")
    sticks=16
    while sticks>0:
        print(player1,",Your Turn")
        print("Sticks remaining:",sticks)
        n=int(input("Pick 1,2 or 3 sticks:"))
        sticks-=n
        print()

        if sticks==0:
            print(player2,"wins and",player1,"loses")
            break

        print(player2, ",Your Turn")
        print("Sticks remaining:", sticks)
        n=int(input("Pick 1,2 or 3 sticks:"))
        sticks-=n
        print()

        if sticks==0:
            print(player1,"wins and",player2,"loses")
            break
game()