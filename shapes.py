
# circle class
class Circle:

    def __init__(self,radius):
        self.radius = radius
    def area(self):
        radee = 3.142 * (self.radius * self.radius)
        return radee
    def circumference (self):
        sum = 2 * (3.142 * self.radius)
        return sum

# Square class
class Square:

     def __init__ (self, sideway):
         self.sideA = sideway
    
     def square_area(self):
         sqArea = self.sideA * self.sideA
         return sqArea
     
     def square_perimeter(self):
         sqPerimeter = 4 * (self.sideA)
         return sqPerimeter
    
# Rectangle class
class Rectangle:
    def __init__ (self, width, length):
        self.width = width
        self.length = length
    
    def rectangle_area(self):
        rtArea = self.width * self.length
        return rtArea
    
    def rectangle_perimeter(self):
        rtPerimeter = 2 * (self.width + self.length)
        return rtPerimeter

# sphere class

class Sphere:
    def __init__(self, radiusA):
        self.radiusA = radiusA
    
    def surfaceArea (self):
        sphere_area =  4 * (3.142 * (self.radiusA * self.radiusA)) 
        return sphere_area
    
    def volume (self):
        sphere_volume = 4/3 * (3.142 * (self.radiusA * self.radiusA * self.radiusA)) 