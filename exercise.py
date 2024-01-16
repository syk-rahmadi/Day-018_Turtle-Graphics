from turtle import Turtle, Screen

tomtom = Turtle()
tomtom.color("purple")
tomtom.shape("turtle")

# Simple way
# tomtom.forward(100)
# tomtom.right(90)
# tomtom.forward(100)
# tomtom.right(90)
# tomtom.forward(100)
# tomtom.right(90)
# tomtom.forward(100)
# tomtom.right(90)


# Using loop
for n in range (20):
    tomtom.pen(fillcolor="black", pencolor="red", pensize=5)
    tomtom.penup()
    tomtom.forward(10)
    tomtom.pendown()
    tomtom.forward(10)
    while n == 19:
        tomtom.right(90)
        tomtom.forward(20)
        tomtom.pendown()
        tomtom.forward(20)

    # tomtom.penup()
    # tomtom.forward(10)
    # tomtom.pendown()
    # tomtom.forward(10)
    # tomtom.right(90)
    # tomtom.penup()
    # tomtom.forward(10)
    # tomtom.pendown()
    # tomtom.forward(10)
    # tomtom.right(90)
    # tomtom.penup()
    # tomtom.forward(10)
    # tomtom.pendown()
    # tomtom.forward(10)
    # tomtom.right(90)






screen = Screen()
screen.exitonclick()
