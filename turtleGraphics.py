import turtle
import random
from turtle import Turtle, Screen

colors = ['red', 'green', 'blue', 'yellow',
          'pink', 'orange', 'purple', 'black', 'grey']
tim = turtle.Turtle()
tim.color('red')
tim.pensize(5)
tim.shape('turtle')

tim.forward(100)
tim.left(90)
tim.penup()
tim.forward(100)
tim.right(90)
tim.pendown()
tim.color('green')
tim.forward(100)

# set pen width
tim.width(5)

# Fill in shape with color
tim.begin_fill()
tim.circle(50)
tim.end_fill()

# square
for x in range(4):
    tim.forward(100)
    tim.right(90)

# random circles
for x in range(5):
    randColor = random.randrange(0, len(colors))
    tim.color(colors[randColor], colors[random.randrange(0, len(colors))])
    rand1 = random.randrange(-300, 300)
    rand2 = random.randrange(-300, 300)
    tim.penup()
    tim.setpos((rand1, rand2))
    tim.pendown()
    tim.begin_fill()
    tim.circle(random.randrange(0, 80))
    tim.end_fill()

jim = turtle.Turtle()
jim.speed(0)
jim.width(5)


def up():
    jim.setheading(90)
    jim.forward(100)


def down():
    jim.setheading(270)
    jim.forward(100)


def left():
    jim.setheading(180)
    jim.forward(100)


def right():
    jim.setheading(0)
    jim.forward(100)


def clickleft(x, y):
    jim.color(random.choice(colors))


def clickright(x, y):
    jim.color(random.choice(colors))
    jim.stamp()


turtle.listen()

turtle.onscreenclick(clickleft, 1)  # 1 for left mouse button
turtle.onscreenclick(clickright, 3)  # 3 for right mouse button

# move with arrowkeys
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.mainloop()

# mouse input
