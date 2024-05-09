import math
def area_circumference(radius):
    ar=math.pi*(radius**2)
    circumference=2*math.pi*radius
    return ar,circumference

print(area_circumference(5))
ar,circumference=area_circumference(5)
print(ar,circumference)