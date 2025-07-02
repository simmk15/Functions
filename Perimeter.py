def square(a):
    return 4*a
def rect(a,b):
    return 2*(a+b)
choice=input("Do you want to calculate the perimeter of SQUARE or RECTANGLE?=")
if choice.lower()=="square":
    side=int(input("Enter the side of the square="))
    print("The perimeter of square is",square(side))
elif choice.lower()=="rectangle":
    lenght=int(input("Enter the lenght of the rectangle="))
    breadth=int(input("Enter the breadth of the rectangle="))
    print("The perimeter of the rectangle is",rect(lenght,breadth))