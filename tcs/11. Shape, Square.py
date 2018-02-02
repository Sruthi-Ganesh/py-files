class Shape(object):
    def __init__(self):
        pass
        
    def findArea(self):
        self.area=0.00

class Square(Shape):
    def __init__(self,length):
        self.length=length

    def findArea(self):
        super(Square,self).findArea()
        self.area=self.length*self.length
        return self.area
    
print "ct20162001781",
print "sruthibadal@gmail.com \n"
length=float(raw_input("Enter length of square "))
S=Square(length)
print S.findArea()
