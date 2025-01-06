
class Geometry:
    def __init__(self):
        self.length = 2
        self.breadth = 3
        self.rad = 5
        self.h = 6

    def area_rect(self,length,breadth):
        print("area of rectangle is: ", self.length*self.breadth)

    def area_circle(self,rad):
        print("arera of circle is: ", 3.14*self.rad*self.rad)

    def area_triangle(self,length,h):
        print("area of triangle is: ", 0.5*self.length*self.h)

    def vol_cyl(self,rad,h):
        print("volume of cyclinder is ", 3.14*self.rad*self.rad*self.h)

r1 = Geometry()
r2 = Geometry()
r3 = Geometry()
r4 = Geometry()

r1.area_rect(4,5)
r2.area_triangle(5,8)
r3.area_circle(8)
r4.vol_cyl(3,7)
