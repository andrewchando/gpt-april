# inspired by this chat w lex fridman https://www.youtube.com/watch?v=TAYhx1U2JjU&ab_channel=LexClips 

# Creating a natural-looking snowflake simulation with growth and randomness can be quite complex. It involves a lot of concepts such as diffusion-limited aggregation (DLA), which is beyond the scope of a simple Python script.

# TODO ^ need to revisit with this actual code, vs. simple koch below

# In this code, the koch_snowflake function draws a Koch curve of a given length and level of detail. It does this recursively: if the level is 0, it just draws a straight line of the given length. Otherwise, it breaks the line into four segments, turning left or right by 60 degrees at each junction. The amount of turn is randomized by up to 10 degrees in either direction to give each snowflake a unique shape.

# The draw_snowflake function uses the koch_snowflake function to draw three Koch curves in a triangle shape, forming a Koch snowflake.

# You can modify the length and level parameters to change the size and detail of the snowflake. Please note that this code needs to be run in a local environment, as the turtle graphics library is not supported in many online Python environments.

import turtle
import random

def koch_snowflake(t, length, level):   
    if level == 0:
        t.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, length / 3, level - 1)
            t.left(angle + random.randint(-10,10))

def draw_snowflake(t, length, level):
    for _ in range(3):
        koch_snowflake(t, length, level)
        t.right(120)

if __name__ == "__main__":
    wn = turtle.Screen()
    wn.bgcolor("white")  

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(0)  # Fastest speed

    # Position the turtle
    snowflake_turtle.penup()
    snowflake_turtle.goto(-150, 50)
    snowflake_turtle.pendown()

    draw_snowflake(snowflake_turtle, 300, 3)

    # Hide the turtle
    snowflake_turtle.hideturtle()

    # Keep the window open
    turtle.done()
