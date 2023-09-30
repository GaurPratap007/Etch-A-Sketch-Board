from turtle import *
import random

tim = Turtle()
screen = Screen()
col = ["green yellow", "bisque", "gainsboro", "cornflower blue", "light blue", "medium sea green", "gold", "tomato", "hot pink"]
register_shape('pen.gif')
shapes = ['pen.gif', 'turtle', 'square', 'arrow', 'circle']


# Control Functions
def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def background():
    screen.bgcolor(random.choice(col))

def pen():
    tim.pencolor(random.choice(col))

def shape():
    tim.shape(random.choice(shapes))

# Controls
screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")
screen.onkey(background, "b")
screen.onkey(pen, "p")
screen.onkey(shape, "s")
screen.exitonclick()
