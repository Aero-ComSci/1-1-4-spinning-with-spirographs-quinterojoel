import turtle as trtl
screen = trtl.Screen()
screen.bgcolor("white")
painter = trtl.Turtle()
painter.speed("fastest")

size = 20
color = "black"
x = 0
y = 0
origin = (x, y)

while True:
    painter.penup()
    painter.goto(origin)
    x = x - 10
    y = y + 10
    origin = (x, y)
    size = size + 20
    painter.color(color)
    painter.begin_fill()
    painter.pendown()
    for i in range(4):
        painter.forward(size)
        painter.right(90)
    painter.end_fill()
