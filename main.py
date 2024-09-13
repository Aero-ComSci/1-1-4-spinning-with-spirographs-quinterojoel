import turtle as trtl
screen = trtl.Screen()
screen.bgcolor("white")
painter = trtl.Turtle()
painter.speed(0)

size = 800
color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
index = -1
x = -400
y = 400
origin = (x, y)

for i in range (160):
    painter.penup()
    painter.goto(origin)
    index += 1
    x += 2.5
    y -= 2.5
    origin = (x, y)
    size -= 5
    painter.color(color[index])
    painter.begin_fill()
    painter.pendown()
    for i in range(4):
        painter.forward(size)
        painter.right(90)
    painter.end_fill()
    if index == 6:
        index = -1

painter.hideturtle()
screen.mainloop()
