from shutil import move
from turtle import Turtle, Screen, forward
from color_for_hirst import final_colors
import turtle
import random

#set up turtle basics
turtle.colormode(255)
painter = Turtle()
painter.speed("fastest")
painter.pensize(2.5)
painter.hideturtle()

#create random color
def random_color() : 
   color =  random.choice(final_colors)
   r = color[0]
   g = color[1]
   b = color[2]
   return (r,g,b)

#draw circle and select random color for circle
def draw_circle(circle_size) : 
    painter.color(random_color())
    painter.begin_fill()
    painter.circle(circle_size)
    painter.end_fill()

# position turtle to starting point
def move_to_start():
    painter.penup()
    painter.left(90)
    painter.forward(400)
    painter.left(90)
    painter.forward(300)
    painter.left(180)

#move across the page horizontally to the right
def move_right(amount_dots):
    for x in range(amount_dots + 1):
        if x <= (amount_dots - 1):
            painter.pendown()
            draw_circle(20)
            painter.penup()
            painter.forward(70)
        else:
            painter.pendown()
            draw_circle(20)
            painter.penup()

    painter.penup()
    painter.right(90)
    painter.forward(50)
    painter.right(90)
    painter.pendown()

#move across the page horizontally to the left
def move_left(amount_dots):
    for x in range(amount_dots + 1):
        if x <= (amount_dots - 1):
            draw_circle(20)
            painter.penup()
            painter.forward(70)
            painter.pendown()
        else:
            draw_circle(20)
            painter.penup()
           
    painter.left(90)
    painter.forward(125)
    painter.left(90)

# initiate paint
def paint(rows , dots) :
    move_to_start()
    for x in range(int(rows / 2)) :
        move_right(dots -1 )
        move_left(dots - 1)

#run program
paint(10 , 10)

#create and exit screen
screen = Screen()
screen.exitonclick()