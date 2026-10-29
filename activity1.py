import turtle
screen=turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Mandala Art!!")
board=turtle.Turtle()
board.speed("fastest")
board.hideturtle()
colors=["Blue","Red","White","Orange","Purple"]
for i in range(80):
    board.color(colors[i%len(colors)])
    board.width(2)
    board.forward(i*2)
    board.right(91)

board.penup()
board.goto(0, -65)
board.setheading(90)
board.pendown()
board.color("gold", "yellow")
board.begin_fill()
for i in range(5):
    board.forward(133)
    board.right(144)
board.end_fill()
board.penup()
board.goto(0,0)
board.pendown()
petal_color=["Cyan","Green","Orange","Darkblue"]
for i in range(28):
    board.color(petal_color[i%len(petal_color)])
    board.begin_fill()
    for j in range(4):
        board.forward(50)
        board.right(90)
    board.end_fill()
    board.right(10)
turtle.done()