import turtle

def sierpinski(level, size):
    if level == 0:
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        size /= 2
        sierpinski(level - 1, size)
        turtle.forward(size)
        sierpinski(level - 1, size)
        turtle.backward(size)
        turtle.left(60)
        turtle.forward(size)
        turtle.right(60)
        sierpinski(level - 1, size)
        turtle.left(60)
        turtle.backward(size)
        turtle.right(60)

# Set up the Turtle screen
turtle.speed(0)  # Set the drawing speed (0 is the fastest)
turtle.penup()
turtle.goto(-200, -200)  # Starting position
turtle.pendown()

# Draw the Sierpinski Triangle
sierpinski(4, 400)  # You can change the level and size as desired

# Close the Turtle graphics window when clicked
turtle.exitonclick()
