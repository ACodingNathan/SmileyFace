import turtle

# Initialize a turtle instance
pen = turtle.Turtle()

# Function to create an eye
def eye(color, radius):
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.up()

# Draw the face
pen.fillcolor('yellow')
pen.begin_fill()
pen.circle(100)
pen.end_fill()
pen.up()

# Draw the eyes
pen.goto(-40, 120)
eye('white', 15)
pen.goto(-37, 125)
eye('black', 5)

pen.goto(40, 120)
eye('white', 15)
pen.goto(40, 125)
eye('black', 5)

# Draw the nose
pen.goto(0, 75)
eye('black', 8)

# Draw the mouth
pen.goto(-40, 85)
pen.down()
pen.right(90)
pen.circle(40, 180)
pen.up()

# Draw the tongue
pen.goto(-10, 45)
pen.down()
pen.right(180)
pen.fillcolor('red')
pen.begin_fill()
pen.circle(10, 180)
pen.end_fill()

# Hide the turtle and display the drawing
pen.hideturtle()
turtle.done()