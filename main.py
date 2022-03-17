import turtle

from colorgram import extract
from turtle import Turtle,Screen
from random import choice

tim = Turtle()
tim.pensize(2)
turtle.colormode(255)
colors = extract('source1.jpg',10)
colors_final = []
for i in range(len(colors)):
    red = colors[i].rgb.r
    green = colors[i].rgb.g
    blue = colors[i].rgb.b
    color = (red,green,blue)
    colors_final.append(color)

columns = int(input("[Number of columns] : "))
rows = int(input("[Number of rows] : "))
dot_size = int(input("[Size of dots] : "))

tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward((dot_size*2 + 10)*(columns-3))
tim.right(225)
tim.speed("fastest")


for i in range(1,rows*columns + 1):
    random_color = choice(colors_final)
    tim.color(random_color[0], random_color[1], random_color[2])
    tim.dot(dot_size,random_color)
    tim.forward(dot_size*2 + 10)
    if i % columns == 0:
        tim.left(90)
        tim.forward(dot_size*2 + 10)
        tim.left(90)
        tim.forward((dot_size*2 + 10)*columns)
        tim.right(180)

my_screen = Screen()
my_screen.exitonclick()