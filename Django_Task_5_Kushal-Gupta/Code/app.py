class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        self.__length = 0
        self.__width = 0
    
    def set_dimensions(self, length, width):
        if length > 0 and width > 0:
            self.__length = length
            self.__width = width
        else:
            print("Dimensions must be positive!")
    
    def calculate_area(self):
        return self.__length * self.__width

class Circle(Shape):
    def __init__(self):
        self.__radius = 0
    
    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Radius must be positive!")
    
    def calculate_area(self):
        return 3.14 * self.__radius * self.__radius

def main():
    exit = 1
    while(exit):
        print("Calculate area of Rectangle or Circle:\n1. Rectangle\n2. Circle\n3. Exit")
        choice = input('Enter your choice: ')

        if choice=='1':
            rect = Rectangle()

            length = int(input("Enter length of rectangle: "))
            width = int(input("Enter width of rectangle: "))

            rect.set_dimensions(length, width)
            print(f"Rectangle area:  {rect.calculate_area()}\n")

        elif choice=='2':
            circle = Circle()

            radius = int(input("Enter radius of circle: "))

            circle.set_radius(radius)
            print(f"Circle area: {rect.calculate_area()}\n")

        elif choice == '3':
            print('Quitting the program')
            exit = 0
        
        else:
            print("Enter a correct choice!")

if __name__ == "__main__":
    main()