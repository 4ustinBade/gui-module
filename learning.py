from turtle import Turtle, Screen, forward
import turtle
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape()
timmy_the_turtle.color("black")


""""" make a square
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)

screen = Screen()
screen.exitonclick()
"""""
"""""
def move():
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(15)
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(15)

for x in range(50):
    move()
    screen = Screen()
    screen.exitonclick()
"""
""""" draw shapes with increasing sides
colors = ["red", "green", "orange", "purple", "black", "grey"]
def draw_shape(n):
    int_angle = (180 * (n-2)) / n
    out_angle = 180 - int_angle 
    for i in range(n) :
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(out_angle)


for x in range(1, 11):
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(x)

screen = Screen()
screen.exitonclick()
"""

""""" random walk
turtle.colormode(255)

def random_color() : 
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

def random_walk():
    direction = [0, 90, 180, 270]
    movement = ["turn", "straight"]
    choice = random.choice(movement)
    if choice == "turn":
       timmy_the_turtle.forward(30)
       timmy_the_turtle.right(random.choice(direction))
       
    elif choice == "forward":
        timmy_the_turtle.forward(30)

timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

for x in range(1000):
    timmy_the_turtle.color(random_color())
    random_walk()
    
screen = Screen()
screen.exitonclick()

"""
""""" spyro
turtle.colormode(255)
timmy_the_turtle.speed("fastest")

def random_color() : 
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

def make_circle():
    timmy_the_turtle.circle(100)

  

for x in range(60):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.right(6)
    make_circle()
    
screen = Screen()
screen.exitonclick()

"""



