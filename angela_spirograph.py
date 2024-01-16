import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)


tam = Turtle()
tam.shape("turtle")
tam.color("purple")
tam.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

tam.speed("fastest")

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tam.shape("turtle")
        tam.color(random_color())
        tam.circle(100)
        tam.pensize(1)
        tam.setheading(tam.heading() + size_of_gap)

draw_spirograph(5)


screen = Screen()
screen.exitonclick()
