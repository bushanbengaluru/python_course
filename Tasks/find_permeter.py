#Find the perimeter of a circle with a given radius
def find_permeter(radius, pi):
    return 2 * pi * radius

def main():
    print("Program to find perimiter of a circle")
    radius = float(input("Enter the radius of the circle: "))
    pi = 3.14159
    perimeter =  find_permeter(radius, pi)
    print(f"The perimeter of the circle is: {perimeter} ")

if __name__ == "__main__":
    main()