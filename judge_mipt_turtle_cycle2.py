import turtle
turtle.shape('turtle')
for a in range(4):
        turtle.forward(20) 
        turtle.left(90) 
for b in range(1):
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-5,-5)
        turtle.pendown()    #first
for a in range(4):
        turtle.forward(30)
        turtle.left(90)
for b in range(1):
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-10,-10)
        turtle.pendown()    #second    
for a in range(4):
        turtle.forward(40)
        turtle.left(90)
for b in range(1):
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-15,-15)
        turtle.pendown()    #third
