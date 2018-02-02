import turtle

def draw_polygon():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    
    i=0
    while(i<4):
      brad.forward(100)
      brad.right(90)
      i=i+1
    

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    i=0
    while(i<2):
      
      brad.right(-60)
      brad.forward(100)
      i=i+1
    brad.right(-150)
    brad.forward(180)

    window.exitonclick()
    

draw_polygon()
