from math import *
class rectangle(object):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height

    
class square(rectangle):
    def __init__(self,width):
        super().__init__(width,width)

    
class ellipse():
    def __init__(self,a,b):
       self.a=a
       self.b=b
    def area(self):
        return self.a*self.b*pi

class circle(ellipse):
    def __init__(self,r):
        self.a=r
        self.b=r
        
        
shapes=[ellipse(10,20),square(15),circle(5),rectangle(20,15),circle(5),square(15),
        ellipse(10,20)]
i=total_area=0
while(i<len(shapes)):
    total_area+=shapes[i].area()
    i+=1
print(total_area)
