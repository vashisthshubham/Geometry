
python
Copy code
class Geometry:
    def __init__(self):
        self.length = 2
        self.breadth = 3
        self.rad = 5
        self.h = 6

    def area_rect(self, length, breadth):
        print("Area of rectangle is:", length * breadth)

    def peri_rect(self, length, breadth):
        print("Perimeter of rectangle is:", 2 * (length + breadth))

    def area_circle(self, rad):
        print("Area of circle is:", 3.14 * rad * rad)

    def area_triangle(self, length, h):
        print("Area of triangle is:", 0.5 * length * h)

    def vol_cyl(self, rad, h):
        print("Volume of cylinder is:", 3.14 * rad * rad * h)


# Create an instance of the class
geometry = Geometry()

# Get user input
x = input("""Please choose your mathematical operation to perform:
1. Area of rectangle
2. Perimeter of rectangle
3. Area of circle
4. Area of triangle
5. Volume of cylinder
Enter your choice (1-5): """)

def option(choice):
    match choice:
        case "1":
            geometry.area_rect(4, 5)
        case "2":
            geometry.peri_rect(4, 5)
        case "3":
            geometry.area_circle(8)
        case "4":
            geometry.area_triangle(5, 8)
        case "5":
            geometry.vol_cyl(3, 7)
        case _:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Call the function with the user input
option(x)
