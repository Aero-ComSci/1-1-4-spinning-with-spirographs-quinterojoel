import turtle as trtl
screen = trtl.Screen()
screen.bgcolor("white")
painter = trtl.Turtle()
painter.speed("fastest")

size = 800
color = "white"
x = -400
y = 400
origin = (x, y)

for i in range (160):
    painter.penup()
    painter.goto(origin)
    if color == "black":
        color = "white"
    else:
        color = "black"
    x = x + 2.5
    y = y - 2.5
    origin = (x, y)
    size = size - 5
    painter.color(color)
    painter.begin_fill()
    painter.pendown()
    for i in range(4):
        painter.forward(size)
        painter.right(90)
    painter.end_fill()

painter.hideturtle()
screen.mainloop()
