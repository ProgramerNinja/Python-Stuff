##calculate the area of a circle
##radius*radius*pi
pi=3.14159265358462643383

def areaOfCircle():
    
#1: get radius
    radius=input("What is the radius?")
    radius=int(radius)
#2: calcilate area
    area=radius*radius*pi
#3: display area
    print("The area of the circle is; ",area)

areaOfCircle()
