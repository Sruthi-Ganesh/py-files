class circle:
    def __init__(self,radius):
        self.radius=radius
        self.pi=3.14
    def area(self):
        self.area=self.pi*self.radius*self.radius
        print self.area
    def perimeter(self):
        self.perimeter=2*self.pi*self.radius
        print self.perimeter
    def greaterarea(self,value):
        if(self.area>value):
            return 'true'
        else:
            return 'false'
print "ct20162001781",
print "sruthibadal@gmail.com \n"
radius=float(raw_input("Enter radius "))
c=circle(radius)
c.area()
c.perimeter()
checkvalue=float(raw_input("Enter a value to check whether the area is greater than the current given value "))
print c.greaterarea(checkvalue)

           

        
    
    
