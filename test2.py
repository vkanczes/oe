import turtle

verySlowTurtle=turtle.Turtle()
wn=turtle.Screen()

# color the background of the screen
wn.bgcolor("blue")

# set color to fill the circles
verySlowTurtle.pen(fillcolor = "white", pensize=3)

verySlowTurtle.speed(0)

'''
# turtle starts in center
verySlowTurtle.pencolor("white")
verySlowTurtle.penup()

# move turtle down to start the circle
verySlowTurtle.right(90)
verySlowTurtle.forward(70)
verySlowTurtle.left(90)

# keep track of each position
start = verySlowTurtle.position()

# start drawing
verySlowTurtle.pendown()
verySlowTurtle.begin_fill()

# create boverySlowTurtleom circle
for i in range(360):
    verySlowTurtle.forward(4)
    verySlowTurtle.right(1)

verySlowTurtle.end_fill()
verySlowTurtle.begin_fill()

# create middle circle
for i in range(360):
    if i == 180:
        middleTop=verySlowTurtle.position()
    verySlowTurtle.forward(3)
    verySlowTurtle.left(1)
verySlowTurtle.end_fill()

# go to next position to draw
verySlowTurtle.penup()
verySlowTurtle.goto(middleTop)
verySlowTurtle.pendown()
verySlowTurtle.begin_fill()

print (middleTop)

verySlowTurtle.pendown()
verySlowTurtle.begin_fill()
#verySlowTurtle.goto(3,273.77)

# create top circle
for i in range(360):
    if i == 180:
        topTop=verySlowTurtle.position()
    verySlowTurtle.forward(2)
    verySlowTurtle.left(1)

verySlowTurtle.end_fill()

print (topTop)

# create the buverySlowTurtleons
# go to position to start draw
verySlowTurtle.penup()
#verySlowTurtle.goto(middleTop)
verySlowTurtle.goto(3,273.77)
verySlowTurtle.right(90)
verySlowTurtle.forward(25)
verySlowTurtle.dot(25, "red")
verySlowTurtle.forward(50)
verySlowTurtle.dot(25, "red")
verySlowTurtle.forward(50)
verySlowTurtle.dot(25, "red")
armPosition = verySlowTurtle.position()
verySlowTurtle.forward(50)
verySlowTurtle.dot(25, "red")
verySlowTurtle.forward(50)

# create the right arm
verySlowTurtle.goto(armPosition)
verySlowTurtle.right(90)
verySlowTurtle.forward(100)
verySlowTurtle.pencolor("black")
verySlowTurtle.pendown()
verySlowTurtle.forward(100)

verySlowTurtle.stamp()

degrees = 60
# create the right fingers
for i in range(6):
    verySlowTurtle.pendown()
    verySlowTurtle.right(degrees)
    verySlowTurtle.forward(20)
    verySlowTurtle.back(20)
    verySlowTurtle.penup()

# create the left arm 
verySlowTurtle.penup()
verySlowTurtle.goto(armPosition)
verySlowTurtle.right(180)
verySlowTurtle.forward(100)
verySlowTurtle.pendown()
verySlowTurtle.forward(100)

# create the left fingers
for i in range(6):
    verySlowTurtle.pendown()
    verySlowTurtle.right(degrees)
    verySlowTurtle.forward(20)
    verySlowTurtle.back(20)
    verySlowTurtle.penup()

# create the eyes
#verySlowTurtle.goto(topTop)
verySlowTurtle.goto(5,502.94)
verySlowTurtle.right(90)
verySlowTurtle.forward(80)
topCenter = verySlowTurtle.position()
verySlowTurtle.right(90)
verySlowTurtle.forward(50)
verySlowTurtle.dot(25, "black")


# 2nd eye
verySlowTurtle.goto(topCenter)
verySlowTurtle.right(180)
verySlowTurtle.forward(50)
verySlowTurtle.dot(25,"black")

# set color to fill the circles
verySlowTurtle.pen(fillcolor = "orange", pensize=3)
verySlowTurtle.pencolor("orange")

'''

# draw a triangle..
#verySlowTurtle.goto(topCenter)
verySlowTurtle.begin_fill()
verySlowTurtle.forward(25)
verySlowTurtle.right(110)
verySlowTurtle.forward(50)
verySlowTurtle.right(140)
verySlowTurtle.forward(50)
verySlowTurtle.right(110)
verySlowTurtle.forward(25)
verySlowTurtle.end_fill()

       

