import math 
def circumference(a):
    return 2*math.pi*a
radius=float(input("Enter the radius of the circle="))
ans=circumference(radius)
print("The radius of the circle=",ans)