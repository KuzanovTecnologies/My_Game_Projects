import turtle

pacman = turtle.Turtle()

pacman.forward(50)
pacman.right(90)

pacman.forward(50)
pacman.right(90)

pacman.forward(50)
pacman.right(90)

turtle.done()

import turtle

pacman = turtle.Turtle()
for i in range(4):
    pacman.forward(50)
    pacman.right(90)

turtle.done()

import turtle
star = turtle.Turtle()

exit = False
def main():
    if not exit:
        for i in range(100):

star.forward(i)
star.right(144)
main()
turtle.mainloop()

def draw_objects():
    #statements
    draw_objects() #may be you want to call it within the time interval
                    of 100ms

draw_objects()
turtle.mainloop()

import turtle
star = turtle.Turtle()

exit = False
def main():
    if not exit:

        star.forward(50)
        star.right(144)
    turtle.ontimer(main,500)
main()

import turtle
star = turtle.Turtle()
def main():
    for i in range(30):
        star.forward(100)
star.right(144)
turtle.onkeypress(main,"space")
turtle.listen()
turtle.mainloop()

import turtle
pacman = turtle.Turtle()
def move(x, y):
    pacman.forward(180)
    print(x,y)

turtle.onclick(move) #calling move method
#turtle.onclick(None) #to remove event-binding

import turtle
hexagon = turtle.Turtle()
num_of_sides = 6
length_of_sides = 70
angle = 360.0 / num_of_sides
for i in range(num_of_sides):
    hexagon.forward(length_of_sides)
    hexagon.right(angle)
turtle.done()

from turtle import *

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

abs(pos()) < 1.

class Base:
    def __init__(self, first):
        self.first = first
    
    def add(self, other):
        print(self.first + other)

class Base:
    def __init__(self, first):
        self.first = first
    def __add__(self, other): #operator '+' is overloaded
print(self.first + other.first)

3
#for strings as add method is defined internally inside str class

class Base:
    def __new__(cls):
        print("This is __new__() magic method")
        obj = object.__new__(cls)
        return obj
    def __init__(self):
        print("This is __init__() magic method")
        self.info = "I love Python"


def line(a, b, x, y):
    "Draw line from `(a, b)` to `(x, y)`."
    import turtle
    turtle.up()
    turtle.goto(a, b)
    turtle.down()
    turtle.goto(x, y)

class Vector(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

def __iadd__(self, other):
    if isinstance(other, Vector):
        self.x += other.x
        self.y += other.y
    else:
        self.x += other
        self.y += other
    return "(%s, %s)"%(self.x, self.y)

def __isub__(self, other):
    if isinstance(other, Vector)
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other
        return "(%s, %s)"%(self.x, self.y)

def __imui__(self, other):
        if isinstance(other, Vector):
            self.x /= other.x
            self.y /= other.y
        else:
            self.x /= other.x
            self.y /= other.y
        return "(%s, %s)"%(self.x, self.y)

def __mul__(self, scalar):
    return (self.x * scalar, self.y * scalar)
def __div__(self, scalar):
    return (self.x / scalar, self.y / scalar)

def __reg__(self):
    return (-self.x, -self.y)

Pen.speed(0)
    Pen.color("#000000000")     #or Pen.color(0, 0, 0)
def box(Dimension): #box method creates rectangular box
        Pen.begin_fill()
    # 0 deg.
        Pen.forward(Dimension)
        Pen.left(90)
    # 90 deg.
        Pen.forward(Dimension)
        Pen.left(90)
    # 180 deg.
        Pen.forward(Dimension)
        Pen.left(90)
    # 270 deg.
        Pen.forward(Dimension)
        Pen.end_fill()
        Pen.setheading(0)

Pen.penup()
Pen.forward(-100)
Pen.setheading(90)
Pen.forward(100)
Pen.setheading(0)

boxSize = 10