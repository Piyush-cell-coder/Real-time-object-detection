import turtle

def olympic_rings(radius):
    colors = ["blue", "black", "red", "yellow", "green"]
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-radius*2, 0)
    turtle.pendown()
    for color in colors:
        turtle.color(color)
        turtle.circle(radius)
        turtle.penup()
        turtle.forward(radius*2)
        turtle.pendown()

radius = int(input("Enter the radius of the rings: "))
olympic_rings(radius)
turtle.exitonclick()
