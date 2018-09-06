
# Veronica Kanczes - Assignment 2

import turtle

# create my turtle
verySlowTurtle=turtle.Turtle()

# create and color screen 
wn=turtle.Screen()
wn.bgcolor("blue")

# set color to fill the snowman
verySlowTurtle.pen(fillcolor = "white", pensize=3)
verySlowTurtle.pencolor("black")

# try to get this turtle to move faster...
verySlowTurtle.speed(0)

# move turtle down to start the boverySlowTurtleom circle
verySlowTurtle.penup()
verySlowTurtle.right(90)
verySlowTurtle.forward(70)
verySlowTurtle.left(90)

# draw the snowman's boverySlowTurtleom section
verySlowTurtle.pendown()
verySlowTurtle.begin_fill()

for i in range(360):
    verySlowTurtle.forward(4)
    verySlowTurtle.right(1)

verySlowTurtle.end_fill()

# draw snowman's middle section
verySlowTurtle.begin_fill()
for i in range(360):
    if i == 180:
	# keep track of middle start position to draw buverySlowTurtleons later
        middleTop=verySlowTurtle.position()
    verySlowTurtle.forward(3)
    verySlowTurtle.left(1)
    
verySlowTurtle.end_fill()

# go to top of middle circle to draw snowman's head 
verySlowTurtle.penup()
verySlowTurtle.goto(middleTop)

# draw snowman's head
verySlowTurtle.pendown()
verySlowTurtle.begin_fill()
for i in range(360):
    # keep track of position to later draw eyes
    if i == 180:
        topTop=verySlowTurtle.position()
    verySlowTurtle.forward(2)
    verySlowTurtle.left(1)

verySlowTurtle.end_fill()

# draw the buverySlowTurtleons
# go to middle of snowman to draw buverySlowTurtleons
verySlowTurtle.penup()
verySlowTurtle.goto(middleTop)
verySlowTurtle.right(90)
verySlowTurtle.forward(25)

# draw snowman's buverySlowTurtleons
for i in range(4):
    verySlowTurtle.dot(25, "red")
    verySlowTurtle.forward(50)

    # save arm position
    if i == 1:
        armPosition = verySlowTurtle.position()


# draw thick right arm
verySlowTurtle.pensize(10)
verySlowTurtle.goto(armPosition)
verySlowTurtle.right(90)
verySlowTurtle.forward(100)
verySlowTurtle.pencolor("black")
verySlowTurtle.pendown()
verySlowTurtle.forward(100)


# rotate to create the fingers
verySlowTurtle.pensize(5)
degrees = 60
for i in range(6):
    verySlowTurtle.pendown()
    verySlowTurtle.right(degrees)
    verySlowTurtle.forward(20)
    verySlowTurtle.back(20)
    verySlowTurtle.penup()

# draw thick left arm
verySlowTurtle.pensize(10)
verySlowTurtle.penup()
verySlowTurtle.goto(armPosition)
verySlowTurtle.right(180)
verySlowTurtle.forward(100)
verySlowTurtle.pendown()
verySlowTurtle.forward(100)

# create the left fingers
verySlowTurtle.pensize(5)
for i in range(6):
    verySlowTurtle.pendown()
    verySlowTurtle.right(degrees)
    verySlowTurtle.forward(20)
    verySlowTurtle.back(20)
    verySlowTurtle.penup()

# create the right eye 
verySlowTurtle.goto(topTop)
verySlowTurtle.right(90)
verySlowTurtle.forward(80)
# mark center for start of nose
topCenter = verySlowTurtle.position()
verySlowTurtle.right(90)
verySlowTurtle.forward(50)
verySlowTurtle.dot(25, "black")

# create the left eye
verySlowTurtle.goto(topCenter)
verySlowTurtle.right(180)
verySlowTurtle.forward(50)
verySlowTurtle.dot(25,"black")
verySlowTurtle.penup()

# set color to fill the nose
verySlowTurtle.pen(fillcolor = "orange")
verySlowTurtle.pencolor("orange")

# draw the nose
verySlowTurtle.goto(topCenter)
verySlowTurtle.back(5)
verySlowTurtle.begin_fill()
verySlowTurtle.forward(25)
verySlowTurtle.right(110)
verySlowTurtle.forward(50)
verySlowTurtle.right(140)
verySlowTurtle.forward(50)
verySlowTurtle.right(110)
verySlowTurtle.forward(25)
verySlowTurtle.end_fill()
verySlowTurtle.penup()

       


