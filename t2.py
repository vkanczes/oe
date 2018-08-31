import turtle

# create my turtle
tt=turtle.Turtle()

# create and color screen 
wn=turtle.Screen()
wn.bgcolor("blue")

# set color to fill the snowman
tt.pen(fillcolor = "white", pensize=3)
tt.pencolor("white")

# try to get this turtle to move faster...
tt.speed(0)

# move turtle down to start the bottom circle
tt.penup()
tt.right(90)
tt.forward(70)
tt.left(90)

# draw the snowman's bottom section
tt.pendown()
tt.begin_fill()

for i in range(360):
    tt.forward(4)
    tt.right(1)

tt.end_fill()

# draw snowman's middle section
tt.begin_fill()
for i in range(360):
    if i == 180:
	# keep track of middle start position to draw buttons later
        middleTop=tt.position()
    tt.forward(3)
    tt.left(1)
    
tt.end_fill()

# go to top of middle circle to draw snowman's head 
tt.penup()
tt.goto(middleTop)

# draw snowman's head
tt.begin_fill()
for i in range(360):
    # keep track of position to later draw eyes
    if i == 180:
        topTop=tt.position()
    tt.forward(2)
    tt.left(1)

tt.end_fill()

# draw the buttons
# go to middle of snowman to draw buttons
tt.penup()
tt.goto(middleTop)
tt.right(90)
tt.forward(25)

# draw snowman's buttons
for i in range(4):
    tt.dot(25, "red")
    tt.forward(50)

    # save arm position
    if i == 1:
        armPosition = tt.position()


# draw thick right arm
tt.pensize(10)
tt.goto(armPosition)
tt.right(90)
tt.forward(100)
tt.pencolor("black")
tt.pendown()
tt.forward(100)


# rotate to create the fingers
tt.pensize(5)
degrees = 60
for i in range(6):
    tt.pendown()
    tt.right(degrees)
    tt.forward(20)
    tt.back(20)
    tt.penup()

# draw thick left arm
tt.pensize(10)
tt.penup()
tt.goto(armPosition)
tt.right(180)
tt.forward(100)
tt.pendown()
tt.forward(100)

# create the left fingers
tt.pensize(5)
for i in range(6):
    tt.pendown()
    tt.right(degrees)
    tt.forward(20)
    tt.back(20)
    tt.penup()

# create the right eye 
tt.goto(topTop)
tt.right(90)
tt.forward(80)
# mark center for start of nose
topCenter = tt.position()
tt.right(90)
tt.forward(50)
tt.dot(25, "black")

# create the left eye
tt.goto(topCenter)
tt.right(180)
tt.forward(50)
tt.dot(25,"black")
tt.penup()

# set color to fill the nose
tt.pen(fillcolor = "orange")
tt.pencolor("orange")

# draw the nose
tt.goto(topCenter)
tt.back(5)
tt.begin_fill()
tt.forward(25)
tt.right(110)
tt.forward(50)
tt.right(140)
tt.forward(50)
tt.right(110)
tt.forward(25)
tt.end_fill()

       


