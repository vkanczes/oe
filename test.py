import turtle

tt=turtle.Turtle()
wn=turtle.Screen()

# color the background of the screen
wn.bgcolor("blue")

# set color to fill the circles
tt.pen(fillcolor = "white", pensize=3)

tt.speed(0)

# turtle starts in center
tt.pencolor("white")
tt.penup()

# move turtle down to start the circle
tt.right(90)
tt.forward(70)
tt.left(90)

# keep track of each position
start = tt.position()

# start drawing
tt.pendown()
tt.begin_fill()

# create bottom circle
for i in range(360):
    tt.forward(4)
    tt.right(1)

tt.end_fill()
tt.begin_fill()

# create middle circle
for i in range(360):
    if i == 180:
        middleTop=tt.position()
    tt.forward(3)
    tt.left(1)
tt.end_fill()

# go to next position to draw
tt.penup()
tt.goto(middleTop)
tt.pendown()
tt.begin_fill()

print (middleTop)

tt.pendown()
tt.begin_fill()
#tt.goto(3,273.77)

# create top circle
for i in range(360):
    if i == 180:
        topTop=tt.position()
    tt.forward(2)
    tt.left(1)

tt.end_fill()

print (topTop)

# create the buttons
# go to position to start draw
tt.penup()
tt.goto(middleTop)
tt.right(90)
tt.forward(25)
tt.dot(25, "red")
tt.forward(50)
tt.dot(25, "red")
tt.forward(50)
tt.dot(25, "red")
armPosition = tt.position()
tt.forward(50)
tt.dot(25, "red")
tt.forward(50)

# create the right arm
tt.goto(armPosition)
tt.right(90)
tt.forward(100)
tt.pencolor("black")
tt.pendown()
tt.forward(100)

tt.stamp()

degrees = 60
# create the right fingers
for i in range(6):
    tt.pendown()
    tt.right(degrees)
    tt.forward(20)
    tt.back(20)
    tt.penup()

# create the left arm 
tt.penup()
tt.goto(armPosition)
tt.right(180)
tt.forward(100)
tt.pendown()
tt.forward(100)

# create the left fingers
for i in range(6):
    tt.pendown()
    tt.right(degrees)
    tt.forward(20)
    tt.back(20)
    tt.penup()

# create the eyes
tt.goto(topTop)
tt.right(90)
tt.forward(80)
topCenter = tt.position()
tt.right(90)
tt.forward(50)
tt.dot(25, "black")


# 2nd eye
tt.goto(topCenter)
tt.right(180)
tt.forward(50)
tt.dot(25,"black")

# set color to fill the circles
tt.pen(fillcolor = "orange", pensize=3)
tt.pencolor("orange")

# draw a triangle..
tt.goto(topCenter)
tt.begin_fill()
tt.forward(25)
tt.right(110)
tt.forward(50)
tt.right(140)
tt.forward(50)
tt.right(110)
tt.forward(25)
tt.end_fill()

       

