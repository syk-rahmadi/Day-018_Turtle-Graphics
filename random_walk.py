from turtle import Turtle
import random


tomtam = Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

for i in range (200):
    tomtam.shape("turtle")
    tomtam.pensize(10)
    tomtam.color(random.choice(colors))
    tomtam.forward(30)
    tomtam.setheading(random.choice(directions))
    tomtam.speed(10)
