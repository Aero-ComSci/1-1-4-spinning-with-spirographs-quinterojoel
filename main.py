import turtle as trtl
screen = trtl.Screen()
screen.bgcolor("white")
painter = trtl.Turtle()
painter.speed("fastest")

size = 1000
color = "white"
x = 100
y = 100
origin = (x, y)

for i in range (100):
    painter.penup()
    painter.goto(origin)
    if color == "black":
        color = "white"
    else:
        color = "black"
    x = x + 5
    y = y - 5
    origin = (x, y)
    size = size - 10
    painter.color(color)
    painter.begin_fill()
    painter.pendown()
    for i in range(4):
        painter.forward(size)
        painter.right(90)
    painter.end_fill()

painter.hideturtle()
screen.mainloop()
