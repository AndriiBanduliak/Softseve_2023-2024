import math

def rectangle_area(a, b):
    return a * b

def triangle_area(h, a):
    return 0.5 * h * a

def circle_area(r):
    return math.pi * math.pow(r, 2)

def calculate_area():
    shape = input("Enter the shape (rectangle, triangle, circle): ")
    if shape == "rectangle":
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        print("The area of the rectangle is: ", rectangle_area(a, b))
    elif shape == "triangle":
        h = float(input("Enter the height of the triangle: "))
        a = float(input("Enter the base of the triangle: "))
        print("The area of the triangle is: ", triangle_area(h, a))
    elif shape == "circle":
        r = float(input("Enter the radius of the circle: "))
        print("The area of the circle is: ", circle_area(r))
    else:
        print("Invalid shape")

calculate_area()
