# Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        print(self.radius,"  :  ",self.color)  

# Create an object RedCircle

RedCircle = Circle(10, 'red')

# Find out the methods can be used on the object RedCircle
RedCircle.drawCircle()
print(dir(RedCircle))

