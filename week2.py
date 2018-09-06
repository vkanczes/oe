# school work week 2

import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

verySlowTurtle = turtle.Turtle()
wn.setworldcoordinates(0,-1.25,360,1.25)

for angle in range(0,360):
    y = math.cos(math.radians(angle))
    verySlowTurtle.goto(angle,y)

wn.exitonclick()

