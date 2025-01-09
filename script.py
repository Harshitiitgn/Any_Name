import math

def greet(name):
    '''To greet the user with the name provided as an argument.'''
    print(f"Hello, {name}!")

def calculate_perimeter_circle(r):
    '''To calculate the perimeter of a circle. The formula is 2 * π * r.'''
    return 2 * math.pi * r


def calculate_area(r):
    '''To calculate the area of a circle. The formula is π * r^2.'''
    return math.pi * r**2

def calculate_area_square(l):
    '''To calculate the area of a square. The formula is l^2.'''
    return l**2

def calculate_perimeter_square(l):
    '''To calculate the perimeter of a square. The formula is 4 * l.'''
    return 4 * l

def calculate_area_rectangle(l, b):
    '''To calculate the area of a rectangle. The formula is l * b.'''
    return l * b

def calcualte_perimeter_rectangle(l, b):
    '''To calculate the perimeter of a rectangle. The formula is 2 * (l + b).'''
    perimeter  = 2 * (l + b)
    return perimeter

def main():
    '''The main function is used to call the other functions and print the results.'''
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

if __name__ == "__main__":
    main()
