"""
A program designed to take the input of a user and calculate the surface area of the user's chosen shape.
The program then asks if the user wishes to know the formula used for the calculation.
"""
import math


def square_formula(length):
    "Function containing the formula for calculating area of a square"
    square_area = length * length
    return square_area


def rectangle_formula(width, height):
    "Function containing the formula for calculating area of a rectangle"
    rectangle_square = width * height
    return rectangle_square


def triangle_formula(base, height):
    "Function containing the formula for calculating area of a triangle"
    triangle_square = (base * 0.5) * height
    return triangle_square


def circle_formula(radius):
    "Function containing the formula for calculating area of a circle"
    circle_square = round((pi * radius * radius), 2)
    return circle_square


"Initialising variables"
user_shape = input("Which shape would you like to calculate the area of?")
pi = math.pi
exponent = "cm\u00b2"
square_value = True
rectangle_value = True
triangle_value = True
circle_value = True

"Initialising all formulas to a variable as output for the user"
square_form = "a\u00b2, where 'a' is the length of one side of the square"
rectangle_form = "W x H, where 'W' is the width and 'H' is the height"
triangle_form = "1/2B x H, where 'B' is the length of the base and 'H' is the height"
circle_form = "\u03C0r\u00b2, where 'r' is the radius of the circle"


"If user chooses square, the following code will run. Code will repeat if invalid number is given"
if user_shape == "square":
    while square_value == True:
        user_length = float(input("What length is your square?"))
        if user_length > 0:
            area = square_formula(user_length)
            print(f"The area of your {user_shape} is {area}{exponent}")
            square_value = False
        else:
            print("Enter a value greater than 0")
    ans = input("Would you like to know the formula?")
    if ans == "yes":
        print(f"The formula is {square_form}.")


"If user chooses rectangle, the following code will run. Code will repeat if invalid number is given"
if user_shape == "rectangle":
    while rectangle_value == True:
        user_height = float(input("What height is your rectangle?"))
        user_width = float(input("What width is your rectangle?"))
        if user_height > 0 and user_width > 0:
            area = rectangle_formula(user_height, user_width)
            print(f"The area of your {user_shape} is {area}{exponent}")
            rectangle_value = False
        else:
            print("Enter a value greater than 0")
    ans = input("Would you like to know the formula?")
    if ans == "yes":
        print(f"The formula is {rectangle_form}.")


"If user chooses triangle, the following code will run. Code will repeat if invalid number is given"
if user_shape == "triangle":
    while triangle_value == True:
        user_base = float(input("What length is the base of your triangle?"))
        user_height = float(input("What height is your triangle?"))
        if user_height > 0 and user_base > 0:
            area = triangle_formula(user_base, user_height)
            print(f"The area of your {user_shape} is {area}{exponent}")
            triangle_value = False
        else:
            print("Enter a value greater than 0")
    ans = input("Would you like to know the formula?")
    if ans == "yes":
        print(f"The formula is {triangle_form}.")


"If user chooses circle, the following code will run. Code will repeat if invalid number is given"
if user_shape == "circle":
    while circle_value == True:
        circle_radius = float(input("What is the radius of your circle?"))
        if circle_radius > 0:
            area = circle_formula(circle_radius)
            print(f"The area of your {user_shape} is {area}{exponent}")
            circle_value = False
        else:
            print("Enter a value greater than 0")
    ans = input("Would you like to know the formula?")
    if ans == "yes":
        print(f"The formula is {circle_form}.")

