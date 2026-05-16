import math

def area(length, breadth):
    return length * breadth

def circle(radius):
    circumference = 2 * math.pi * radius
    circumference = round(circumference, 2)
  
    area = math.pi * radius * radius
    area = round(area, 2)

    return circumference, area

print(area(5, 10))
result1, result2 = circle(7)
print("Circumference:", result1)
print("Area:", result2)