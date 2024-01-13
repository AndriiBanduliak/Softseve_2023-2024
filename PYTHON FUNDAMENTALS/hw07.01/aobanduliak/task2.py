import math


def area_rectangle(length, width):
    """Returns the area of a rectangle.

    Parameters:
    length (int or float): The length of the rectangle.
    width (int or float): The width of the rectangle.

    Returns:
    int or float: The area of the rectangle.
    """
    return length * width


def area_triangle(base, height):
    """Returns the area of a triangle.

    Parameters:
    base (int or float): The base of the triangle.
    height (int or float): The height of the triangle.

    Returns:
    int or float: The area of the triangle.
    """
    return 0.5 * base * height


def area_circle(radius):
    """Returns the area of a circle.

    Parameters:
    radius (int or float): The radius of the circle.

    Returns:
    int or float: The area of the circle.
    """
    return math.pi * radius ** 2


# Main program
choice = input("Choose a shape: rectangle, triangle, or circle: ")
if choice == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = area_rectangle(length, width)
elif choice == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = area_triangle(base, height)
elif choice == "circle":
    radius = float(input("Enter the radius of the circle: "))
    area = area_circle(radius)
else:
    print("Invalid choice.")
    area = None

if area is not None:
    print(f"The area of the {choice} is {area}.")
