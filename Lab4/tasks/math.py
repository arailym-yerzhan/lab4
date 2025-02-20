import math

def degree_to_radian(degree):
    return round(degree * (math.pi / 180), 6)

def trapezoid_area(height, base1, base2):
    return round(0.5 * (base1 + base2) * height, 1)

def regular_polygon_area(sides, length):
    return round((sides * (length ** 2)) / (4 * math.tan(math.pi / sides)), 1)

def parallelogram_area(base, height):
    return round(base * height, 1)

def main():
    print("\nChoose an option:")
    print("1. Convert degree to radian")
    print("2. Calculate area of a trapezoid")
    print("3. Calculate area of a regular polygon")
    print("4. Calculate area of a parallelogram")
    print("5. Exit")
    
    while True:
        choice = input("Enter your choice: ")
        
        if choice == "1":
            degree = float(input("Input degree: "))
            print("Output radian:", degree_to_radian(degree))
        elif choice == "2":
            height = float(input("Height: "))
            base1 = float(input("Base, first value: "))
            base2 = float(input("Base, second value: "))
            print("Expected Output:", trapezoid_area(height, base1, base2))
        elif choice == "3":
            sides = int(input("Input number of sides: "))
            length = float(input("Input the length of a side: "))
            print("The area of the polygon is:", regular_polygon_area(sides, length))
        elif choice == "4":
            base = float(input("Length of base: "))
            height = float(input("Height of parallelogram: "))
            print("Expected Output:", parallelogram_area(base, height))
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
