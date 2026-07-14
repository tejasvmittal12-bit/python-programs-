# ================================
# COLOUR LOOP ARTWORK
# ================================
# Topics:
# The Turtle Library | Setting Up the Canvas
# Moving the Turtle | Pen Control
# Drawing Shapes with Fill

import turtle

# ------------------------------------------------
# PART 1 — SET UP THE CANVAS
# ------------------------------------------------

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colour Loop Artwork")

# ------------------------------------------------
# PART 2 — CREATE THE TURTLE
# ------------------------------------------------

artist = turtle.Turtle()
artist.speed("fastest")
artist.hideturtle()
artist.pensize(2)

# ------------------------------------------------
# PART 3 — DRAW A FILLED PETAL
# ------------------------------------------------

def draw_petal(size, colour):
    artist.color(colour)
    artist.begin_fill()

    for _ in range(2):
        artist.circle(size, 60)
        artist.left(120)

    artist.end_fill()


# ------------------------------------------------
# PART 4 — CREATE THE COLOUR LOOP ARTWORK
# ------------------------------------------------

colours = ["red", "orange", "yellow", "lime", "cyan", "blue", "magenta"]

for i in range(36):
    draw_petal(90, colours[i % len(colours)])
    artist.right(10)

# ------------------------------------------------
# PART 5 — DRAW A FILLED CENTRE CIRCLE
# ------------------------------------------------

artist.penup()
artist.goto(0, -25)
artist.pendown()

artist.color("white")
artist.begin_fill()
artist.circle(25)
artist.end_fill()

# ------------------------------------------------
# PART 6 — KEEP THE WINDOW OPEN
# ------------------------------------------------

turtle.done()