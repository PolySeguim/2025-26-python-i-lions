import turtle

# Create a screen and a turtle object
screen = turtle.Screen()
screen.title("Turtle Example in Python")

# Create a turtle instance
my_turtle = turtle.Turtle()

# Draw a square
for _ in range(4):
    my_turtle.forward(100)  # Move forward by 100 units
    my_turtle.right(90)     # Turn right by 90 degrees

# Keep the window open until clicked
closeWindow = input("Press any key to close window. ")
screen.mainloop()

# Keep the window open until clicked
turtle.done()