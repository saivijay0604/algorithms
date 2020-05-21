import turtle
import time

def triangle():
    tri = turtle.Turtle()
    tri.color("blue")
    tri.pensize(2.5)
    for i in range(2):
        tri.forward(100)
        tri.left(120)
    tri.forward(100)

def square():
    sq = turtle.Turtle()
    sq.pensize(5)
    for i in range(2):
        sq.forward(100)
        sq.left(90)
        sq.forward(90)
        sq.left(90)
    sq.left(42)
    sq.forward(130)
wn = turtle.Screen()
wn.bgcolor("red")
triangle()
square()
wn.exitonclick()