import turtle

def draw_polygon():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    angie = brad
    squarecount=0
    
    while(squarecount<36):
        i=0
        while(i<4):
            brad.forward(100)
            brad.right(90)
            i=i+1
        brad.right(10)
        squarecount=squarecount+1
     

draw_polygon()
