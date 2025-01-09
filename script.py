import math

def greet(name):
    print(f"Hello, {name}!")

'''To greet the user with the name provided as an argument.'''

def calculate_perimeter_circle(r):
    return 2 * math.pi * r
'''To calculate the perimeter of a circle. The formula is 2 * π * r, where r is the radius of the circle.'''

def calculate_area(r):
    return math.pi * r**2
'''To calculate the area of a circle. The formula is π * r^2, where r is the radius of the circle.'''

def calculate_area_square(l):
    return l**2
'''To calculate the area of a square. The formula is l^2, where l is the length of the side of the square.'''

def calculate_perimeter_square(l):
    return 4 * l
'''To calculate the perimeter of a square. The formula is 4 * l, where l is the length of the side of the square.'''

def calculate_area_rectangle(l, b):
    return l * b
'''To calculate the area of a rectangle. The formula is l * b, where l is the length and b is the breadth of the rectangle.'''

def calcualte_perimeter_rectangle(l, b):
    perimeter  = 2 * (l + b)
    return perimeter
'''To calculate the perimeter of a rectangle. The formula is 2 * (l + b), where l is the length and b is the breadth of the rectangle.'''

def main():
    greet("Harshit")
    r = 5
    l = 10
    b = 6
    area = calculate_area(r)
    perimeter = calculate_perimeter_circle(r)
    square_area = calculate_area_square(l)
    square_perimeter = calculate_perimeter_square(l)
    rectangle_area = calculate_area_rectangle(l, b)
    rectangle_perimeter = calcualte_perimeter_rectangle(l, b)
    print(f"The area of a circle with radius {r} is {area}")
    print(f"The perimeter of a circle with radius {r} is {perimeter}")
    print(f"The area of a square with side {l} is {square_area}")
    print(f"The perimeter of a square with side {l} is {square_perimeter}")
    print(f"The area of a rectangle with length {l} and breadth {b} is {rectangle_area}")
    print(f"The perimeter of a rectangle with length {l} and breadth {b} is {rectangle_perimeter}")

    '''The main function is used to call the other functions and print the results.'''


if __name__ == "__main__":
    main()
