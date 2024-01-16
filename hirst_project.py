from turtle import Turtle, Screen
import turtle as turtle_module
import random

turtle_module.colormode(255)

#Color list for hirst painting
color_list = [(234, 214, 75), (188, 163, 38), (207, 177, 74), (35, 17, 7), (185, 79, 20), (244, 231, 176), (146, 32, 8),
              (223, 206, 22), (238, 93, 26), (37, 7, 10), (91, 67, 26), (9, 15, 8), (254, 252, 254), (250, 254, 250),
              (251, 252, 254), (12, 10, 17), (236, 175, 154), (128, 22, 31), (106, 78, 83), (75, 83, 70), (154, 116, 118), (164, 121, 128)]

#Turtle for the hirst painting
timtum = Turtle()
timtum.hideturtle()
timtum.speed("fastest")
timtum.penup()

#Turtle position for the hirst painting
timtum.goto(-450,-450)

#number of dots
number_of_dots = 400

#Function for the hirst painting
for i in range(1, number_of_dots + 1):
    timtum.dot(15, random.choice(color_list))
    timtum.forward(50)
    if i % 10 == 0:
        timtum.setheading(90)
        timtum.forward(50)
        timtum.setheading(180)
        timtum.forward(500)
        timtum.setheading(0)


#Set up the screen
screen = Screen()
screen.exitonclick()