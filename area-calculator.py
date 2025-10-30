# A calculator program that calculates the area of the following shapes:
# Square, Rectangle, Triangle, Circle

import math
pi = math.pi
repeat = True

print("==================\nArea Calculator 📐\n==================\n")
print("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit")

while repeat == True:
    option = int(input("What area you like to calculate? "))

    if option == 1:
        height = float(input("What is the height of your triangle? "))
        base = float(input("What is the base of your triangle? "))

        area = (base*height)/2

        print(f"\nThe area of your triangle is {area}\n")

    elif option == 2:
        height = float(input("What is the height of your rectange? "))
        base = float(input("What is the base of your rectange? "))

        area = (base*height)

        print(f"\nThe area of your rectangle is {area}\n")

    elif option == 3:
        side = float(input("What is the side length of your square? "))

        area = (side**2)

        print(f"\nThe area of your square is {area}\n")

    elif option == 4:
        rad = float(input("What is the radius of your circle? "))

        area = (pi*(rad**2))

        print(f"\nThe area of your circle is {area}\n")

    else:
        print("\nThanks for using this calculator!")
        repeat = False
