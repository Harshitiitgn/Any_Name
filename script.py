def greet(name):
    """Greet the user with the provided name."""
    print(f"Hello, {name}!")

def calculate_perimeter_circle(r):
    import math
    """Calculate the perimeter (circumference) of a circle."""
    return 2 * math.pi * r

def calculate_area(r):
    """Calculate the area of a circle."""
    return math.pi * r**2

def calculate_area_square(l):
    """Calculate the area of a square."""
    return l**2

def calculate_perimeter_square(l):
    """Calculate the perimeter of a square."""
    return 4 * l

def calculate_area_rectangle(l, b):
    """Calculate the area of a rectangle."""
    return l * b

def calculate_perimeter_rectangle(l, b):
    """Calculate the perimeter of a rectangle."""
    return 2 * (l + b)

def main():
    """Main function to demonstrate the usage of the above functions."""
    greet("Harshit")
    r = 5
    l = 10
    b = 6
    # Call all the functions and print their results
    area = calculate_area(r)
    perimeter = calculate_perimeter_circle(r)
    square_area = calculate_area_square(l)
    square_perimeter = calculate_perimeter_square(l)
    rectangle_area = calculate_area_rectangle(l, b)
    rectangle_perimeter = calculate_perimeter_rectangle(l, b)
    print(f"The area of a circle with radius {r} is {area}")
    print(f"The perimeter of a circle with radius {r} is {perimeter}")
    print(f"The area of a square with side {l} is {square_area}")
    print(f"The perimeter of a square with side {l} is {square_perimeter}")
    print(f"The area of a rectangle with length {l} and breadth {b} is {rectangle_area}")
    print(f"The perimeter of a rectangle with length {l} and breadth {b} is {rectangle_perimeter}")

if __name__ == "__main__":
    main()
