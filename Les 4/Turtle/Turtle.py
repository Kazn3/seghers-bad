import turtle
import random


def teken(lengte):
    for teller in range (4):
        turtle.forward(lengte)
        turtle.right(90)

kleur = ("red","blue", "green","yellow")
som = 0
while som != 100:
    turtle.pendown()
    turtle.speed(100)
    turtle.pensize(3)
    turtle.pencolor(random.choice(kleur))
    teken(150)
    turtle.right(5)
    som += 1

turtle.done()