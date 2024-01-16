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

for i in range (360):
    tam.shape("turtle")
    tam.pensize(1)
    tam.color(random_color())
    tam.circle(100)
    tam.left(10)
    tam.speed("fastest")



screen = Screen()
screen.exitonclick()
