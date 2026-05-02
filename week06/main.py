from gallery import Gallery
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle

def add_circle(gallery):
    try:
        radius = float(input("Enter radius: "))
        shape = Circle(radius)
        gallery.add_shape(shape)
    except ValueError as error:
        print(f"Sorry! There's and error: {error}. Try Again")

def add_rectangle(gallery):
    try:
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        shape = Rectangle(width, height)
        gallery.add_shape(shape)
    except ValueError as error:
        print(f"Sorry! There's and error: {error}. Try Again")

def add_triangle(gallery):
    try:
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))
        shape = Triangle(a, b, c)
        gallery.add_shape(shape)
    except ValueError as error:
        print(f"Sorry! There's and error: {error}. Try Again")

def main():
    gallery = Gallery("My Shapes")

    while True:
        print("\n" + "*" * 65 )
        print("%40s" % ("Shape Menu"))
        print("*" * 65 + "\n")
        print("1. Add a Circle")
        print("2. Add a Rectangle")
        print("3. Add a Triangle")
        print("4. Display all shapes")
        print("5. Show total area")
        print("6. Show largest shape")
        print("7. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_circle(gallery)
        elif choice == "2":
            add_rectangle(gallery)
        elif choice == "3":
            add_triangle(gallery)
        elif choice == "4":
            gallery.display_all()
        elif choice == "5":
            print(f"Total area: {gallery.total_area():.2f}")
        elif choice == "6":
            largest = gallery.largest_shape()
            if largest:
                print(f"Largest shape: {largest.describe()}, Area: {largest.area():.2f}")
            else:
                print("Gallery is empty :( Try adding a shape!")
        elif choice == "7":
            print("Bye, Have a great day!")
        else:
            print("Invalid choice! Try again")


if __name__ == "__main__":
    main()