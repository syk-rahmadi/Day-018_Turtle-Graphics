from turtle import Turtle
import random


tomtim = Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape (num_sides):
    angle = 360 / num_sides
    for n in range(num_sides):
        tomtim.forward(100)
        tomtim.right(angle)

for side in range (3, 10):
    tomtim.color(random.choice(colors))
    draw_shape(side)