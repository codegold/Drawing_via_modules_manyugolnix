import turtle
turtle.shape('turtle')

for i in range(1, 5):
    for a in range(4):
        turtle.forward(10+i*10) 
        turtle.left(90) 
    turtle.end_fill()
    turtle.penup()
    turtle.goto(i*-5,i*-5)
    turtle.pendown()
