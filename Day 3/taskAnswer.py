# =============================================================================

# Write a Python program that asks the user to enter a number and 
# tells him whether it is an even or odd number.

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")
# =============================================================================

# Write a Python program to check if a triangle is equilateral, isosceles or scalene.
# Note: 
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# Expected Output:
# Input lengths of the triangle sides:                                    
# X: 6                                                                    
# Y: 8                                                                    
# Z: 12                                                                   
# Scalene triangle

# x = float(input("X: "))
# y = float(input("Y: "))
# z = float(input("Z: "))

# if x + y > z and x + z > y and y + z > x:
#     if x == y == z:
#         print("Equilateral triangle")
#     elif x == y or y == z or x == z:
#         print("Isosceles triangle")
#     else:
#         print("Scalene triangle")
# else:
#     print("The given lengths do not form a triangle.")
# =============================================================================

# Write a Python program to find the median of three values.
# Expected Output:
# Input first number: 10                                                  
# Input second number: 5                                                
# Input third number: 7                                                 
# The median is 7 

# a = float(input("Input first number: "))
# b = float(input("Input second number: "))
# c = float(input("Input third number: "))
# numbers = [a, b, c]
# numbers.sort()
# print("The median is", numbers[1])
# =============================================================================

# Write a Python program to create the multiplication table (from 1 to 10) of a number.
# Expected Output:
# Input a number: 6                                                       
# 6 x 1 = 6                                                               
# 6 x 2 = 12                                                              
# 6 x 3 = 18                                                              
# 6 x 4 = 24                                                              
# 6 x 5 = 30                                                              
# 6 x 6 = 36                                                              
# 6 x 7 = 42                                                              
# 6 x 8 = 48                                                              
# 6 x 9 = 54          

# num = int(input("Input a number: "))

# print(f"{num} x 1 = {num * 1}")
# print(f"{num} x 2 = {num * 2}")
# print(f"{num} x 3 = {num * 3}")
# print(f"{num} x 4 = {num * 4}")
# print(f"{num} x 5 = {num * 5}")
# print(f"{num} x 6 = {num * 6}")
# print(f"{num} x 7 = {num * 7}")
# print(f"{num} x 8 = {num * 8}")
# print(f"{num} x 9 = {num * 9}")
# print(f"{num} x 10 = {num * 10}")
# =============================================================================
