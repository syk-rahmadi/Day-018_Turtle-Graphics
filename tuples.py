# python list = [1,2,3]
# python tuples = (1,2,3)
# my_tuple = (1,2,3)
# my_tuple[1]

import turtle as T
import random

tom = T.Turtle()
T.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


directions = [0, 90, 180, 270]

for i in range (200):
    tom.shape("turtle")
    tom.pensize(10)
    tom.color(random_color())
    tom.forward(30)
    tom.setheading(random.choice(directions))
    tom.speed(10)

screen = Screen()
screen.exitonclick()
