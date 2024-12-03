'''Author Anjana Krishna
Date 30 Nov 2024
program to find a right triangle'''
def is_right_angle_triangle(first_side,second_side,third_side):
   sides=[first_side,second_side,third_side]
   sides.sort()
   if sides[2]**2==sides[0]**2+sides[1]**2:
       return True
       return False
first_side=int(input("Enter the first side:"))
second_side=int(input("Enter the second side:"))
third_side=int(input("Enter the third side:"))
if is_right_angle_triangle(first_side,second_side,third_side):
    print(f"The given sides are part of a  right angle triangle")
else:
    print(f"The the sides are not part of a right angle triangle")