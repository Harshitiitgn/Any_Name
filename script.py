import math

def greet(name):
    print(f"Hello, {name}!")

def calculate_perimeter_circle(r):
    return 2 * math.pi * r

def calculate_area(r):
    return math.pi * r**2

def calculate_area_square(l):
    return l**2

def calculate_perimeter_square(l):
    return 4 * l

def calculate_area_rectangle(l, b):
    return l * b

def calcualte_perimeter_rectangle(l, b):
    perimeter  = 2 * (l + b)
    return perimeter

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

if __name__ == "__main__":
    main()
