#snake_game.py
import curses as c

c.initstr()
win = c.newwin(20,60,0,0)
win.keypad(1)
c.noecho()
c.curs_set(0)
win.border(0)
win.nodelay(1)

snake = [[4,10], [4,9], [4,8]]
food = [10,20]

win.addch(food[0],food[1], 'O')

from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
#CODE FROM PREVIOUS TOPIC

key = KEY_RIGHT #default key

#ASCII value of ESC is 27
while key != 27:
    win.border(0)
    win.timeout(100) #speed for snake
    default_key = key
    event = win.getch()
    key = key if event == -1 else event
    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:
        key = default_key
while key != 27:
    #code from preceding topic
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) +
    (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) +
    (key == KEY_RIGHT and 1)])

from random import randint

while key != 27:
#add the following code after updating head position
  if snake[0] == food:
    food = []
    while food == []:
      food = [randint(1,18), randint(1,58)]
      if food in snake:
          food = []
    win.addch(food[0], food[1], 'O')
else:
    last = snake.pop()
    win.addch(last[0], last[1], ' ')
win.addch(snake[0][0], snake[0][1], 'X')

if snake[0] in snake[1:]:
    break

c.endwin()

score = 0
while key != 27:
  # CODE TO ADD SCORE IN THE SCREEN
  win.border(0)
  win.addstr(0, 2, 'Score : ' + str(score) + ' ')
  win.addstr(0, 27, ' SNAKE ')
  if snake[0] == food:
    food = []
    #AFTER EATING EVERY FOOD SCORE = FOOD
    score += 1
    while food == []:
      food = [randint(1,18), randint(1,58)]
      if food in snake: food = []
    win.addch(food[0], food[1], 'O')
else:
    end = snake.pop()
    win.addch(last[0], last[1], '')
win.addch(snake[0][0], snake[0][1], 'X')
c.endwin()

if snake[0][0] == 0:
    snake[0][0] = 18 #regenerate snake from lower boundary line
if snake[0][0] == 19:
    snake[0][0] = 1 #regenerate snake from upper boundary line

if snake[0][1] == 0:
    snake[0][1] = 58 #regenerate from left
if snake[0][1] == 59:
    snake[0][1] = 1 #regenerate from right

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint

WIDTH = 35
HEIGHT = 20

MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2 
SNAKE_LENGTH = 5
SNAKE_X = SNAKE_LENGTH + 1
SNAKE_Y = 3
TIMEOUT = 100

if __name__ == '__main__':
    curses.initscr()
    curses.beep()
    window.curses.newwin(HEIGHT, WIDTH, 0, 0)
    window.timeowt(TIMEOUT)
    window.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    window.border(0)

class Body(object):
    def __init__(self, x, y, char='#'):
        self.x = x
        self.y = y
        self.char = char
    def coor(self):
        return self.x, self.y
class Snake:
    REV_DIR_MAP = {
        KEY_UP: KEY_DOWN, KEY_DOWN: KEY_UP,
        KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT,
    }

    def __init__(self, x, y, window):
        self.body_list= []
        self.timeout = TIMEOUT
        for i in range(SNAKE_LENGTH, 0, -1):
            self.body_list.append(Body(x, - i, y))
        self.body_list.append(Body(x, y, 'O'))
        self.windows = window
        self.direction = KEY_RIGHT
        self.last_head_coor = (x, y)
        self.direction_map = {
            KEY_UP: self.move_up,
            KEY_DOWN: self.move_down,
            KEY_LEFT: self.move_left,
            KEY_RIGHT: self.move_right
        }

def add_body(self, body_list):
    self.body_list.extend(body_list)

def render(self):
            for body in self.body_list:
                self.window.addstr(body.y, body.x, body.char)

if __name__ == '__main__':
    #code from preceding topic
    snake = Snake(SNAKE_X, SNAKE_Y, window)
    while True:
    window.clear()
    window.border(0)
    snake.render()

def change_direction(self, direction):
        if direction != Snake.REV_DIR_MAP(self.direction):
            self.direction = direction

class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.email = '{0}.{1}@gmail.com'.format(self.first, self.last)
    
    per1 = Person('Ross', 'Geller')
    print(perl.first)
    print(perl.last)
    print(perl.email)

    #output
    Ross
    Geller
    Ross.Geller@gmail.com

    per1.first = "Rachel"
    print(perl.first)
    print(perl.email)

    #output
    Rachel
    Ross.Geller@gmail.com

class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return '{0}.{1}@gmail.com'.format(self.first,self.last)
    
    @property
    def head(self):
        return self.body_list[-1]
    
    @property
    def coor(self):
        return self.head_x, self.head_y
def update(self):
       last_body = self.body_list.pop(0)
       last_body = self.body_list[-1].x
       last_body = self.body_list[-1].y
       self.body_list.insert(-1, last_body)
       self.last_head_coor = (self.head.x, self.head.y)
       self.direction_map[self.direction]()

def render(self):
            for body in self.body_list:
                self.window.addstr(body.y, body.x, body.char)

if __name__ == '__main__':
    #code from preceding topic
    #snake = Snake(SNAKE_X, SNAKE_Y, window)
    while True:
    window.clear()
    window.border(0)
    snake.render()

class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.email = '{0}.{1}@gmail.com'.format(self.first, self.last)

per1 = Person('Ross', 'Geller')
print(perl.first)
print(perl.last)
print(perl.email)

#output
Ross
Geller
Ross.Geller@gmail.com

per1.first = "Rachel"
print(per1.first)
print(per1.email)

#output
Rachel
Ross.Geller@gmail.com

class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{0},{1}@gmail.com'.format(self.first,self.last)

    @property
    def head(self):
        return self.body_list[-1]

    @property
    def coor(self):
        return self.head.x, self.head.y

def update(self):
        last_body = self.body_list.pop(0)
        last_body.x = self.body_list[-1].x
        last_body.y = self.body_list[-1].y
        self.body_list.insert(-1, last_body)
        self.last_head_coor = (self.head_x, self.head.y)
        self.direction_map[self.direction]()
if __name__ == '__main__':
    #code from precending topic
    #snake is object of Snake class
    while True:
        event = window.getch()
        if event == 27:
            break
        
        if event in [KEY_UP, KEY_DOWN. KEY_LEFT, KEY_RIGHT]:
            snake.change_direction(event)

        if event == 32:
            key = -1
            while key != 32:
                key = window.getch()
        
        snake.update()

#These functions are added inside the Snake class
def move_up(self):
        self.head.y -= 1
        if self.head.y < 1:
            self.head.y = MAX_Y

def move_down(self):
    self.head.y += 1
    if self.head.y < 1
        self.head.y = 1

def move_down(self):
    self.head.y += 1
    if self.head.y > MAX_Y:
        self.head.y = 1

def move_left(self):
    self.head.x -= 1
    if self.head.x < 1:
        self.head.x = MAX_X:

def move_right(self):
    self.head.x += 1
    if self.head.x > MAX_X:
        self.head.x = 1

@property
def collided(self):
    return any([body.coor == self.head.coor
                for body in self.body_list[:-1]])

if __name__ == "__main__":
    while True:
       #code from preceding topics
       #snake is Snake class object
       if snake.collided:
            break

class Food:
    def __init__(self, window, char='&'):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)
        self.char = char
        self.window = window

    def render(self):
        self.window.addstr(self.y, self.x, self.char)

    def reset(self):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)

if __name__ == '__main__':
    food = Food(window, '*')
    while True:
        food.render()

def eat_food(self, food):
    food_reset()
    body = Body(self.last_head_coor[0], self.last_head_coor[1])
    self.body_list.insert(-1, body)

if __name__ == '__main__':
#snake is object of Snake class
#food is object of Food class
    while True:
        if snake.head.h == food.x and snake.head.y == food.y:
            snake.eat_food(food)

curses.endwin()


class Snake:
    self.score = 0
    @property
    def score(self):
        return 'Score : {0}'.format(self.score)

def eat_food(self, food):
    food.reset()
    body = Body(self.last_head_coor[0], self.last_head_coor[1])
    self.body_list.insert(-1, body)
    self.score += 1

while True:
    window.addstr(0, 5, snake.score)

n = int(input("Enter any number"))
for i in range(1,100):
    if i == n:
        print(i)
        break

for i in range(1, 10):
    for j in range(i):
        print(i, end='')
    print()

for i in range(1, 10):
        print (str(i) * i)

#output
1
22
333
4444
55555
666666
7777777
88888888
999999999

new_list = []
for i in range(10):
    new_list.append(i)
print(new_list)

#output
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = [i for i in range(10)]
print(new_list)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

even_power  = [i * i        for i in range(5)           if i % 2 == 0]
print(even_power)
[0, 4, 16]

numbers = [1,2,3,4,5]
alphabets = ['a','b','c','d','e',]

new_list = [[n,a] for n in numbers for a in alphabets]
print(new_list)
[[1, 'a'], [1, 'b', [1, 'c'], [1, 'd'], [1, 'e'], 
[2, 'a'], [2, 'b']  [2, 'c'], [2, 'd'], [2, 'e'], 
[3, 'a'], [3, 'b'], [3, 'c'], [3, 'd']  [3, 'e'], 
[4, 'a'], [4, 'b'], [4, 'c'], [4, 'd']  [4, 'e'], [5, 'a'], [5, 'b'], [5, 'c'], [5, 'd'] [5, 'e']]]

dict_comp = {x:chr(65+x) for x in range(1, 6)}
print(dict_comp)
{1: 'B', 2: 'C', 3: 'D', 'E', 5: 'F'}
set_comp = {x ** 2 for x in range(5) if x % 2 == 0}
type(set_comp)
print(set_comp)

#output
<class 'set'>
{0, 16, 4}

Input: a = [2,3,4,5,6,7] and b = [0,3,2,1,3,4]
Output: [0, 3, 2, 1, 3, 4]

a = [2,3,4,5,6,7]
b = [0,3,2,1,3,4]
result = []
length = len(a)
for i in range(length):
    result.append(min(a[i],b[i]))
print(result)
#output
[0, 3, 2, 1, 3, 4]

def fun1(info):
    print(info)

fun1("Good Morning")
fun2 = fun1
fun2("Good Morning")

def decorate_it(func):
    def inner():
        print("Decorated")
        func()
    return inner

def non_Decorated():
    print("Not-Decorated")

@decorate_it
def non_Decorated():
    print("Not-Decorated")

def non_Decorated():
    print("Not-Decorated")

decorate = decorate_it(non_Decorated)

def smart_multiply(func):
    def inner(a,b):
        if (a.isdigit() and b.isdigit()):
            a = int(a)
            b = int(b)
            print("multiplying",a," with ",b)
            return func(a,b)
        else:
            print("Whoops!! Not valid multiplication")
            return
    return inner

@smart_multiply
def multiply(a,b):
    print(a*b)

a = input("value of a: ")
b = input("value of b: ")
multiply(a,b)

value of a: 4
value of b: 5
multiplying 4 with 5
20

value of a: t
value of b: y
Whoops!! Not valid multiplication

def universal(func):
    def inner(*args, **kwargs):
        print("It works for any function")
        return func(*args,**kwargs)
return inner

class Speed:
    def __init__(self, speed = 0):
        self.speed = speed
    
    def change_to_mile(self):
        return (self.speed*0.6213,"miles")
#new updates are made as follows using getter and setter
    def get_speed(self):
        return self._speed
    def set_speed(self, km):
        if km > 50:
            raise ValueError("You are liable to speeding ticket")

class Speed:
    def __init__(self, speed = 0):
        self.speed = speed

    def change_to_mile(self):
        return (self.speed*0.6213," miles")

    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self,km):
        if km > 50:
            raise ValueError("You are liable to speeding ticket")
        self._speed = km

class Speed:
    def __init__(self, speed = 0):
        self.speed = speed

    def change_to_mile(self):
        return (self.speed*0.6213," miles")
    def get_speed(self):
        return self._speed
    def set_speed(self, km):
        if km > 50:
            raise ValueError("You are liable to speeding ticket")
        self._speed = km
    #using property
    speed = property(get_speed,set_speed)

    def collided(self):
        return any([body.coor == self.head.coor
                        for body in self.body_list(:-1)])


    @property
    def score(self):
        return 'Score: {0}'.format(self.score)


palette = ["#4B610B" , "#FAFAFA" , "#DF0101" , "#FE9A2E"]

for i in range (0,len(grid_of_pixels)):
        for j in range (0, len(grid_of_pixels[i])):
            Pen.Color(palette(grid_of_pixels[i][[j]]))
            box(boxSize)
            Pen.penup()
            Pen.forward(boxSize)
            Pen.pendown()
        Pen.setheading(270)
        Pen.penup()
        Pen.forward(boxSize)
        Pen.setheading(180)
        Pen.forward(boxSize*len(grid_of_pixels[i]))
        Pen.setheading(0)
        Pen.pendown()

        #following class will create vector
        #representing current position of game character
        class vector(collections.Sequence):
            """Two-dimensional vector.
            Vectors can be modified in-place
            vector(1, 2)
            vector(-2.0, 1.0)
            """
            PRECISION = 6 #value 6 represents level of rounding
            #for example: 4.53434343 => 4.53343
            __slots__ = ('_x', '_y', '_hash')

def __init__(self, x, y):
    """Initialize vector with coordinates: x, y.
    1
    2
    """
    self._hash = None
    self._x = round(x, self.PRECISION)
    self._y = round(y, self.PRECISION)

@property
    def x(self):
        """X-axis component of vector.
        
        1

        3
        """
        return self._
@x.setter
def x(self, value):
    if self._hash is not None:
         raise ValueError('cannot set x after hashing')

self._x = round(value, self.PRECISION)

@property
def y(self):
    """Y-axis component of vector.
    v = vector(1, 2) 
    v.y
    2
    v.y = 5
    v.y
    5
    """
    return self._y
@y.setter
def y(self, value):
    if self._hash is not None:
        raise ValueError('cannot set y after hashing')
    self._y = round(value, self.PRECISION)
def __hash__(self):
    """v.__hash__() -> hash(v)
    >>> v = vector(1, 2)
    >>> h = hash(v) 
    >>> v.x = 2 
    """
    if self._hash is None:
        pair = (self.x, self.y)
        self._hash = hash(pair)
    return self._hash
def copy(self):
    """Return copy of vector.
    >>> v = vector(1, 2)
    >>> w = v.copy()
    >>> v is w
    False
    """
    type_self = type(self)
    return type_self(self.x, self.y)

def __iadd__(self, other):
        """v.__iadd__(w) -> v += w
        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v += w
        >>> v 
        vector(5, 7)
        """
        if self._hash is not None:
            raise ValueError:('cannot add vector after hashing')
        elif isinstance(other, vector):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        return self

def __add__(self, other):
    """v.__add__(w) -> v + w
    >>> v = vector(1, 2)
    >>> w = vector(3, 4)
    >>> v + w
    vector(4, 6)
    >>> v + 1
    vector(2, 3)
    >>> 2.0 + v
    vector(3.0, 4.0)
    
    """
    copy = self.copy()
    return copy.__iadd__(other)
__radd__ = __add__
def move(self, other):
    """Move vector by other (in-place).
    >>> v = vector(1, 2)
    >>> w = vector(3, 4)
    >>> v.move(w)
    >>> v 
    vector(4, 6)
    >>> v.move(3)
    >>> v 
    vector(4, 6)
    >>> v.move(3)
    >>> v
    vector(7, 9)
    """
    self.__add__(other)

import math
def rotate(self, angle):
    """Rotate vector counter-clockwise by angle (in-place).
    >>> v = vector(1, 2)
    >>> v.rotate(90)
    >>> v == vector(-2, 1)
    True
    
    """
    if self._hash is not None:
        raise ValueError('cannot rotate vector after hashing')
    radians = angle * math.pi / 180.0
    cosine = math.cos(radians)
    sine = math.sin(radians)
    x = self.x
    y = self.y
    self.x = x * cosine - y * sine
    self.y = y * cosine + x * sine

from random import *
from turtle import * 
from base import vector

ant = vector(0, 0) #ant is character
aim = vector(2, 0) #aim is next position

def wrap(value):
    return value

def draw():
    "Move ant and draw screen."
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)
    aim.rotate(random() * 10 - 5)
    clear()
    goto(ant.x, ant.y)
    dot(10)
    if running:
        ontimer(draw, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()
running = True
draw()
done()

from turtle import *
from random import randrange
from base import vector

def square(x, y, size, name):
    """Draw square at `(x, y)` with side length `size` and fill color
    `name`.
    The square is oriented so the bottom left corner is at (x, y).
    """
    import turtle
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(name)
    turtle.begin_fill()
    for count in range(size)
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

    from base import square

    food = vector(0, 0)
    snake = [vector(10, 0)]
    aim = vector(0, -10)

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, "red")
        update()
        return
    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10 
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    clear()
    for body in snake:
        square(body.x, body.y, 9, 'black')
    
    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

listen()
onkey(lambda: change(10,0), 'Right')
onkey(lambda: change(-10, 0) 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

    move()
    done()

from random import choice, random
from turtle import *
from base import vector

def value():
    "Randomly generate value between (-5, -3) or (3, 5)."
    return (3 + random() * 2) * choice([1, -1])
ball = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0}

def rectangle(x, y, width, height):
    "Draw rectangle at (x, y) with given width and height."
    up()
    goto(x, y)
    down()

begin_fill()
for count in range(2):
    forward(width)
    left(90)
    forward(width)
    left(90)
end_fill()

def draw():
    "Draw game and move pong ball."
    clear()
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)
    ball.move(aim)
    x = ball.x
    y = ball.y

    up()
    goto(x, y)
    dot(10)
    update()
    #when ball hits upper or lower boundary
    #Total height is 420 (-200 down and 200 up)
        if y < -200 or y > 200:
            aim.y = -aim.y
    #when ball is near left boundary
        if x < -185:
            low = state[1]
            high = state[1] + 50
            #when player1 hits ball 
            if low <= high:
                aim.x = -aim.x
            else:
                return
    #when ball is near right boundary
            if x > 185:
                low = state[2]
                high = state[2] + 50
                #when player2 hits ball
                if low <= y <= high:
                    aim.x -aim.x
                else:
                    return
                ontimer(draw, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)

def move(player, change):
    "Move player position by change."
    state[player] += change

listen()
onkey(lambda: move(1, 20), 'w')
onkey(lambda: move(1, -20), 's')
onkey(lambda: move(2, 20), 'i')
onkey(lambda: move(2, -20), 'k')
draw()
done()

def inside(point):
    "Return True if point on screen."
    return -200 < point.x < 200 and -200 < point.y < 200

bird = vector(0, 0)
balls = []

def draw(align):
    "Draw screen objects."
    clear()
    goto(bird.x, bird.y)
    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')
    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')
    update()

from random import *
from base import vector #for vectored motion
def move():
    "Update object positions."
    bird.y -= 5
    for ball in balls:
        ball.x -= 3

if randrange(10) == 0:
    y = randrange(-199, 199)
    ball = vector(199, y)
    balls.append(ball)      #append each obstacles to list

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return
    
    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return
    draw(True)
    ontimer(move, 50) #calls move function at every 50ms

    def tap(x, y):
        "Move bird up in response to screen tap."
        up = vector(0, 30)
        bird.move(up)
    
    hideturtle()
    up()
    tracer(False)
    onscreenclick(tap)
    move()
    done()

import turtle
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(5, 1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(5, 1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align='center',
  font=('Courier', 24, 'bold'))
pen.hideturtle()
#  Score
score_a = 0
score_b = 0

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_a.ycor():
    y += -20
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')

wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

while True:
    wn.update()

    # Moving Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    #1: For upper and lower boundary
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
    #2: for RIGHT boundary
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx += -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B:  {}".format(score_a, score_b),
           align="center", font=('Courier', 24, 'bold'))

    #3: For LEFT boundary
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx += -1
        score_b += 1

        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
           align='center', font=('Courier', 24, 'bold'))

# Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor()
        < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60):

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()
        < paddle_b.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60):
        ball.setx(-340)
        ball.dx *= -1

import pygame
print(pygame.version.ver)  #this command will check pygame version installed
print(pygame.version.vernum)  #alternate command

if pygame.overlay is None:
    print("No such module! Try other one")
    print("https://www.pygame.org/contribute.html")
    exit()

import pygame as p #abbreviating pygame with p 

p.init()
screen = p.display.set_mode((400, 350)) #size of screen
finish = False

while not finish:
    for each_event in p.event.get():
        if each_event.type == p.QUIT:
            finish = True
    p.draw.rect(screen, (0, 128, 0), p.rect(35, 35, 65, 65))
    p.display.flip()

    pygame.display.set_caption("My First Game")

    screen_surface = pygame.Surface((200,200))

    background_surface = pygame.image.load(bg.jpg).convert()

    screen = Pygame.load("bg.jpg")
    screen.subsurface((0,0),(20,20))
    screen.subsurface((20,0),(20,20))

    screen.blit(image_file_name.png, (0,0))
    screen.blit(list_of_images, (400, 300), (frame_number*10, 0, 100, 100))

    import pygame as game
    from pygame.locals import *
    from random import *
    import sys

    game.init()
    display_screen = game.display.set_mode((650, 470), 0, 32)
    while True:
        for eachEvent.type == QUIT:
            sys.exit()

        circle_generate_color = (randint(0,255), randint(0,255),
                                randint(0,255)
        circle_position_arbitrary = randint(0, 649), randint(0,469))
        circle_radius_arbitrary = randint(1,230)
        game.draw.circle(display_screen, circle_generate_color,
        circle_position_arbitrary, circle_radius_arbitary)
        game.display.update()

        displayScreen = pygame.display.set_mode((640, 480), 0, 32) #standard size
        displayScreen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)

        import pygame as p #abbreviating pygame module as p
        from pygame.locals import *
        import sys
        p.init()
        displayScreen = p.display.set_mode((640, 480), 0, 32)
        while True:
            for Each_event in p.event.get():
                if Each_event.type == QUIT:
                    sys.exit()
                if Each_event.type == KEYDOWN:
                    if Each_event.key == K_f:
                            displayFullscreen = not displayFullscreen
                            if displayFullscreen:
                                displayScreen = p.display.set_mode((640, 480),
                                                FULLSCREEN, 32)

                            else:
                                displayScreen = p.display.set_mode((640, 480), 0,
                                                32)
                p.display.update()

                import pygame as p
                any_key_pressed = p.key.get_pressed()
                if any_key_pressed[K_UP]:
                    #UP key has been pressed
                    jump()
import pygame as p
import sys
while True:
    for anyEvent in p.event.get():
        if anyEvent.type == QUIT:
            sys.exit()
        any_keys_pressed = p.key.get_pressed()
        movement_keys = Vector2(0, 0) #Vector2 imported from gameobjects
        #movement keys are directional (arrow) keys
        if any_keys_pressed[K_LEFT]:
            movement_keys.x = +1
        if any_keys_pressed[K_UP]:
            movement_keys.y = -1
        elif any_keys_pressed[K_DOWN]:
            movement_keys.y = +1
        movement_keys.normalize() #creates list comprehension
                                    [refer chapter 7]
resultant_x = sin(angle_of_rotational_sprite*pi/180.0)
#sin(theta)  represents base rotation about x-axix
resultant_y = cos(angle_of_rotational_sprite*pi/180.0)
#cos(theta)  represents height rotation about y-axis
new_heading_movement = Vector2(resultant_x, resultant_y)
new_heading_movement *= movement_direction

import pygame as game #now instead of using pygame, you can use game

game.init()
windowScreen = game.display.set_mode((300, 300))
done = False

# Draw Rect as place where mouse pointer can be clicked
RectangularPlace = game.draw.rect(windowScreem, (255, 0, 0), (150, 150, 150,
150))
game.display.update()
# Main Loop
while not done:
    # Mouse position and button clicking.
    position = game.mouse.get_pos()
    leftPressed, rightPressed, centerPressed = game.mouse.get_pressed()
    #checking if left mouse button is collided with rect place or not
    if RectangularPlace.collidepoint(position) and leftPressed:
        print("You have clicked on a rectangle")
    # Quit pygame.
    for anyEvent in game.event.get():
        if anyEvent.type == game.QUIT:
            done = True
    gameBackground = pygame.image.load(image_filename_for_background).convert()
    Image_cursor =
    pygame.image.load(image_filename_mouseCursor).convert_alpha()

    pygame.transform.rotate(img, 270) #rotation of image by 270 degree

    import pygame as game
    from sys import exit
    game.init()

    DisplayScreen = game.display.set_mode((850,650))
    game.display.set_caption('The Snake Game') #game title

    game.display.update()

    gameOver = False

    while not gameOver:
        for anyEvent in game.event.get():
            print(event)
            exit()
    game.quit()
    quit()

    white = (255,255,255)
    color_black = (0,0,0)
    green = (0,255,0)
    color_red = (255,0,0)

    while not gameOver:
        #1 EVENT GET
        DisplayScreen.fill(white) #BACKGROUND WHITE
        game.display.update()
    while not gameOver:
        DisplayScreen.fill(white) #background of game
        game.draw.rect(DisplayScreen, color_black, [450,300,10,10]) #1. snake
        #two ways of defining rect objects
        DisplayScreem.fill(color_red, rect=[200,200,50,50]) #2. food

        change_x = 300
        change_y = 300
        while not gameOver:
            for anyEvent in game.event.get():
                if anyEvent.type == game.QUIT:
                    gameOver = True:
                if anyEvent.key == game.K_LEFT:
                    change_x -= 10
                if anyEvent.key == game.K_RIGHT:
                    change_x += 10
            DisplayScree.fill(white)
            game.draw.rect(DisplayScreen, black, [change_x,change_y,10,10])
            game.display.update()

            lead_x_change = 0

            while not gameOver:
                for anyEvent in game.event.get():
                    if anyEvent.type == game.QUIT:
                        gameOver = True
                    if anyEvent.type == game.K_LEFT:
                        lead_x_change = -10
                    if anyEvent.key == game.K_RIGHT:
                        lead_x_change = 10
                        
                        change_x += lead_x_change
                        DisplayScreen.fill(white)
                        game.draw.rect(DisplayScreen, black, [change_x,change_y,10,10])
                        game.display.update()

                        clock = game.time.Clock()
                        while not gameOver:
                            #event handling
                            #code from preceding topic
                            clock.tick(30) #FPS

                            lead_y_change = 0
                            while not gameOver:
                                    if anyEvent.type == game.KEYDOWN:
                                        if anyEvent.key == game.K_LEFT:
                                            lead_x_change = -10
                                            lead_y_change = 0
                                        elif anyEvent.key == game.K_RIGHT:
                                            lead_x_change = 10
                                            lead_y_change = 0
                                        elif anyEvent.key == game.K_UP:
                                            lead_y_change = -10
                                            lead_x_change = 0
                                        elif anyEvent.key == game.K_DOWN:
                                            lead_y_change = 10
                                            lead_x_change = 0
                                    
                                    change_x += lead_x_change
                                    change_y += lead_y_change

                            while not gameOver:
                                if change_x >= 800 or change_x < 0 or change_y >= 600 or change_y < 0:
                                        gameOver = True
                                
                                #variable initialization step
                                import pygame as game

                                game.init()

                                color_white = (255,255,255)
                                color_black = (0,0,0)
                                color_red = (255,0,0)

                                #display size
                                display_width = 800
                                display_height = 600

                                DisplayScreen = game.display.set_mode((display_width,display_height))
                                game.display.set_caption('') #game title 

                                gameOver = False

                                change_x = display_width/2
                                change_y = display_height/2

                                lead_x_change = 0 
                                lead_y_change = 0

                                objectClock = game.time.Clock()

                                pixel_size = 10 #box size
                                FPS = 30 #frame rate

                                #main loop
                                while not gameOver:
                                    for anyEvent in game.event.get():
                                        if anyEvent.type == game.QUIT:
                                            gameOver = True
                                if anyEvent.type == game.KEYDOWN:
                                    if anyEvent.key == game.K_LEFT:
                                        lead_x_change = -pixel_size
                                        lead_y_change = 0
                                    elif anyEvent.key == game.K_RIGHT:
                                        lead_x_change = pixel_size
                                        lead_y_change = 0
                                    elif anyEvent.key == game.K_UP:
                                        lead_x_change = -pixel_size
                                        lead_y_change = 0
                                    elif anyEvent.key == game.K_DOWN:
                                        lead_y_change = pixel_size
                                        lead_x_change = 0

                                #step 3: adding logic which will check if snake hit boundary or not

                                if change_x >= display_width or change_x < 0 or change_y >= display_height
                                                or change_y < 0:
                                       gameOver = True

                                change_x += lead_x_change
                                change_y += lead_y_change
                                DisplayScreen.fill(color_white)
                                game.draw.rect(DisplayScreen, color_black,
                                  [change_x,change_y,pixel_size,pixel_size])
                                game.display.update()

                                objectClock.tick(FPS)

            def MainLoopForGame():
                global arrow_key #to track which arrow key user pressed

                gameOver = False
                gameFinish = False
                #initial change_x and change_y represent center of screen
                #initial position for snake
                change_x = display_width/2
                change_y = display_height/2

                lead_x_change = 0
                lead_y_change = 0

                XpositionApple = round(random.randrange(0, display_width-pixel_size))
                YpositionApple = round(random.randrange(0, display_height-pixel_size))

        while not gameOver:

            while gameFinish == True:
                DisplayScreen.fill(color_white)
                game.display.update()

                #game is object of pygame
                for anyEvent in game.event.get():
                    if anyEvent.type == pygame.KEYDOWN:
                        if anyEvent.key == pygame.K_q:
                            gameOver = True
                            gameFinish = False
                        if anyEvent.key == pygame.K_c:
                            MainLoopForGame()
#event to make movement for snake based on arrow keys
       for anyEvent in game.event.get():
           if anyEvent.type == game.QUIT:
                gameOver = True
           if anyEvent.key == game.K_RIGHT:
               arrow_key = 'left'
               lead_x_change = pixel_size
               lead_y_change = 0
           elif anyEvent.key == game.K_UP:
                arrow_key = 'up'
                lead_y_change = -pixel_size
                lead_x_change = 0
           if change_x >= display_width or change_x < 0 or change_y >=
                          display_height or change_y < 0:
              gameFinish = True
        change_x += lead_x_change
        change_y += lead_y_change
        DisplayScreen.fill(color_white)

        Width_Apple = 30
        game.draw.rect(DisplayScreen, color_red, [XpositionApple,
        YpositionApple, Width_Apple, Width_Apple])
        game.draw.rect(DisplayScreen, color_black,
            [change_x,change_y,pixel_size, pixel_size])
        game.display.update()

        objectClock.tick(FPS)
    game.quit()
    quit()

MainLoopForGame()

def drawSnake(pixel_size, snakeArray):
    for eachSegment in snakeArray:
        game.draw.rect(DisplayScreen, color_green
[eachSegment[0],eachSegment[1],pixel_size, pixel_size])

def MainLoopForGame():
    snakeArray = []
    snakeLength = 1

        while not gameOver:
            head_of_Snake = []
    #at the beginning, snake will only have head
    head_of_Snake.append(change_x)
    head_of_Snake.append(change_y)
            snakeArray.append(head_of_Snake)

            if len(snakeArray) > snakeLength:
                del snakeArray[0] #deleting overflow of elements

            for eachPart in snakeArray[:-1]:
            if eachPart == head_of_Snake:
                gameFinish = True #when snake collides with own body
        drawSnake(pixel_size, snakeArray)
        game.display.update()

        #condition where snake rect is at the top of apple rect
        if change_x > XpositionApple and change_x < XpositionApple + Width_Apple or
        change_x + pixel_size > XpositionApple and change_x + pixel_size < 
        XpositionApple + Width_Apple:

            if change_y > YpositionApple and change_Y < YpositionApple +
            Width_Apple:
                    #generate apple to new position
                    XpositionApple = round(random.randrange(0,
                                     display_width-pixel_size))
                    YpositionApple = round(random.randrange(0,
                                     display_height-pixel_size))
                    snakeLength += 1

            elif change_y + pixel_size > YpositionApple and change_y + pixel_size
                 < YpositionApple + Width_Apple:

                     XpositionApple = round(random.randrange(0, display_width-
                                      pixel_size))
                     YpositionApple = round(random.randrange(0, display_height-
                                      pixel_size))
                    snakeLength += 1

                    image = game.image.load('snake-4773742_1920.jpg')

                    DisplayScreen.blit(image, (snakeArray[-1][0], snakeArray[-1][1]))

                    def drawSnake(pixel_size, snakeArray):
                     if arrow_key == "right":
                     head_of_Snake = game.transform.rotate(image, 270) #making rotation of 270

                     if arrow_key == "left":
                     head_of_Snake = game.transform.rotate(image, 90)

                     if arrow_key == "up":
                     head_of_Snake = image #default

                     if arrow_key == "down":
                     head_of_Snake = game.transform.rotate(image, 180)

                     DisplayScreen.blit(head_of_Snake, (snakeArray[-1][0], snakeArray[-1][1]))
                     for eachSegment in snakeArray[:-1]:
                     game.draw.rect(DisplayScreen, color_green, [eachSegment[0], eachSegment[1],
                     pixel_size, pixel_size])

                     appleimg = game.image.load('sara-cervera-oJGca8Ch828-unsplash.jpg')
                     #add apple.jpg file in same directory of python file
                     while not gameOver:
                         #code must be added before checking of user eats apple or not
                         DisplayScreen.blit(appleimg,   (XpositionApple, YpositionApple))

                         font_small = game.font.SysFont("comicsansms", 25)
                         font_medium = game.font.SysFont("comicsansms", 50)
                         font_large = game.font.SysFont("comicsansms", 80)
            def objects_text(sample_text, sample_color, sample_size):
             if sample_size == "small":
             surface_for_text = font_small.render(sample_text, True, sample_color)
             elif sample_size == "medium":
             surface_for_text = font_medium.render(sample_text, True, sample_color)
             elif sample_size == "large":
             surface_for_text = font_large.render(sample_text, True, sample_color)

             return surface_for_text, surface_for_text.get_rect()

             def display_ScreenMessage(message, font_color, yDisplace=0,
             font_size="small"):
             textSurface, textRectShape = objects_text(message, font_color, font_size)
             textRectShape.center = (display_width/ 2), (display_height/ 2) + yDisplace
             DisplaceSurface.blit(textSurface, textRectShape)

             def intro_for_game(): #function for adding game intro
              intro_screen = True

              while intro_screen:

              for eachEvent in game.event.get():
              if eachEvent.type == game.QUIT:
              game.quit()
              quit()

              if eachEvent.type == game.KEYDOWN:
              if eachEvent.key == game.K_c:
              intro_screen = False
              if eachEvent.key == game.K_q:
              game.quit()
              quit()

              DisplayScreen.fill(color_white)
              display_ScreenMessage("Welcome to Snake",

              color_green,
              -99,
              "large")

              display_ScreenMessage("Press C to play or Q to quit.",
              color_red,
              180)

              game.display.update()
              objectClock.tick(12)

              intro_for_game()
              MainLoopForGame()

try:
    display = pygame.display.set_mode((640,0))
except pygame.error:
    print("Not possible to create display")
    exit()

#creates snow
for eachSnow in range(50):
    x_pos = random.randrange(0, 500)
    y_pos = random.randrange(0, 500)
    pygame.draw.circle(displayScreen, (255,255,255) , [x_pos, y_pos], 2)
#size:2

for eachSnow in range(50):
    x_pos = random.randrange(0, 500)
    y_pos = random.randrange(0, 500)
    snowArray.append((x_pos, y_pos))
for eachSnow in range(len(snowArray)):
 # Draw the snow flake
     pygame.draw.circle(displayScreen, (255,255,255) , snowArray[i], 2)

if snowArray[i][1] > 500:
# Reset it just above the top
y_pos = random.randrange(-50, -10)
snowArray[i][1] = y_pos
# Give it a new x position
x_pos = random.randrange(0, 500)
snowArray[i][O] = y_pos

import pygame as p
import random as r
# Initialize the pygame
p.init()
color_code_black = [0, 0, 0]
color_code_white = [255, 255, 255]
# Set the height and width of the screen
DISPLAY = [500, 500]
WINDOW = p.display.set_mode(DISPLAY)
# Create an empty list to store position of snow
snowArray = []

# Loop 50 times and add a snow flake in a random x,y position
for eachSnow in range(50):
    x_pos = r.randrange(0, 500)
    y_pos = r.randrange(0, 500)
    snowArray.append([x_pos, y_pos])
    objectClock = game.time.Clock()

# Loop until the user clicks the close button.
finish = False
while not finish:
    for anyEvent in p.event.get(): # User did something
        if anyEvent.type == p.QUIT: # If user clicked close
            finish = True # Flag that we are done so we 
                          exit this loop
# Set the screen background
        WINDOW.fill(BLACK)
# Process each snow flake in the list
        for eachSnow in range(len(snowArray)):
# Draw the snow flake
        p.draw.circle(WINDOW, color_code_white, snowArray[i], 2)
# One step down for snow [falling of snow]
        snowArray[i][1] += 1
# Checking if snow is out of boundary or not
if snowArray[i][1] > 500:
# Reset if it from top
y_pos = r.randrange(-40, -10)
snowArray[i][1] = y_pos
# New random x_position
x_pos = r.randrange(0, 500)
snowArray[i][O] = x_pos

# Update screen with what you've drawn.
    game.display.update()
    objectClock.tick(20)
#if you remove following line of code, IDLE will hang at exit 
game.quit()

import pygame
pygame.init()
win = pygame.display.set_mode((500, 480))
pygame.quit()
#walk_Right contains images in which character is turning towards
   Right direction
walkRight = [pygame.image.load('Right1.jpg'),
 pygame.image.load('Left2.jpg'), pygame.image.load('Left3.jpg'),
 pygame.image.load('Left4.jpg'), pygame.image.load('Left5.jpg'),
 pygame.image.load('Left6.jpg'), pygame.image.load('Left7.jpg'),
 pygame.image.load('Left8.jpg'), pygame.image.load('Left9.jpg')]
#Background and stand still images
background = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.jpg')

x = 50
y = 400
width = 40
height = 60
vel = 5
clock = pygame.time.Clock()

left = False
right = False
walkCount = 0

finish = False
while not finish: clock.tick(27)

while not finish:
    clock.tick(27)
    for anyEvent in pygame.event.get():
        if anyEvent.type == pygame.QUIT:
            finish = True
    keys = pygame.key.get_pressed()
   #checking key pressed and if character is at x(boundary) or not?
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel #going left by 5pixels
        left = True
        right = False
    #checking RIGHT key press and is character coincides with
        RIGHT boundary.
    # value (500 - vel - width) is maximum width of screen,
        thus x should be less
    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel #going right by 5pixels
        left = False
        right = True
    else:
        #not pressing any keys
        left = False
        right = False
        walkCount = 0
    Animation_Logic()

def Animation_Logic()
    global walkCount
    win.blit(background, (0,0))
    #check_1
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0
    pygame.display.update()

import math
import os
from random import randint
from collections import deque
import pygame
from pygame.locals import *

Frame_Rate = 60 #FPS
ANIMATION_SPEED = 0.18  # pixels per millisecond
WINDOW_WIDTH = 284 * 2  # Background image sprite size: 284x512 px;
                        #our screen is twice so to rendered twice: *2
WINDOW_HEIGHT = 512

def loading_images():
    """Function to load images"""
    def loading_image(image_name):
    """Return the sprites of pygame by create unique filename so that
    we can reference them"""
    new_filename = os.path.join('.', 'images', image_name)
    image = pygame.image.load(new_filename) #loading with pygame
                                            module
    image.convert()

        return image
    return {'game_background': loading_Image('background.jpg'),
    'endPipe': loading_Image('endPipe.jpg'),
    'bodyPipe': loading_Image('bodyPipe.jpg'),
    # GIF format file/images are not supported by Pygame
    'WingUp': loading_Image('bird-wingup.jpg'),
    'WingDown': loading_Image('bird-wingdown.jpg')}

def frames_to_msec(frames, fps=FPS):
    """Convert frames to milliseconds at the specificied framerate.
    
    Arguments:
    frames: How many frames to convert to milliseconds.
    fps: The framerate to use for convertion.   Default: FPS.
    """
    return 1000.0 * frames / fps

def msec_to_frames(milliseconds, fps=FPS):
    """Convert milliseconds to frames at the specified framerate.
    
    Arguments:
    milliseconds: How many milliseconds to convert to frames.
    fps: The framerate to use for convertion.   Default: FPS.
    """
    return fps * milliseconds / 1000.0

class Bird(pygame.sprite.Sprite):

    WIDTH = HEIGHT = 50
    SINK_SPEED = 0.18
    CLIMB_SPEED = 0.3
    CLIMB_DURATION = 333.3

    def __init__(self, x, y, msec_to_climb, images):
        """Initialize a new Bird instance.
        
        super(Bird, self).__init__()
        self.msec_to_climb = msec_to_climb
        self._img_wingup, self._img_wingdown = images
        self._mask_wingup = pygame.mask.from_surface(self._img_wingup)
        self._mask_wingdown = pygame.mask.from_surface(self._img_wingdown)
        """

@property
def mask(self):
    """Get a bitmask for use in collision detection.
    
    The bitmask excludes all pixels in self.image with a
    transparency greater than 127."""
    if pygame.time.get_ticks() % 500 >= 250:
        return self._mask_wingup
    else:
        return self._mask_wingdown
@property
def rect(self):
    """Get the bird's position, width, and height, as a pygame.Rect."""
    return Rect(self.x, self.y, Bird.WIDTH, Bird.HEIGHT)

def update(self, delta_frames=1)
    """Update the bird's position.
    
    Arguments:
    delta_frames: The number of frames elapsed since this method was
        last called.
    """
    if self.msec_to_climb > 0:
        frac_climb_done = 1 - self.msec_to_climb/Bird.CLIMB_DURATION
        #logic for climb movement
        self.y -= (Bird.CLIMB_SPEED * frames_to_msec (delta_frames) *
                    (1 - math.cos(frac_climb_done * math.pi)))
        self.msec_to_climb -= frames_to_msec(delta_frames)
    else:
        self.y += Bird.SINK_SPEED * frames_to_msec(delta_frames)
class PipePair(pygame.sprite.Sprite):
    """class that provides obstacles in the way of the bird in the form of
    pipe-pair."""

        WIDTH = 80
        HEIGHT_PIECE = 32
        ADD_INTERVAL = 3000
def __init__(self, end_image_pipe, body_image_pipe):
    """
    """
    self.x = float(WINDOW_WIDTH - 1)
    self.score_counted = False
    self.image = pygame.Surface((PipePair.WIDTH, WINDOW_HEIGHT),
                 SRCALPHA)
    self.image.convert() # speeds up blitting
    self.image.fill((0, 0, 0, 0))
#Logic 1: **create pipe-pieces**--- Explanation is provided after
             the code
   total_pipe_body_pieces = int((WINDOW_HEIGHT - # fill window from
                                                   top to bottom
    3 * Bird.HEIGHT - # make room for bird to fit through
    3 * PipePair.HEIGHT_PIECE) / # 2 end pieces + 1 body piece
    PipePair.HEIGHT_PIECE # to get number of pipe pieces
    )
    self.bottom_pipe_pieces = randint (1, total_pipe_body_pieces)
    self.top_pipe_pieces = total_pipe_body_pieces - 
                           self.bottom_pieces

# bottom pipe
  for i in range(1, self.bottom_pipe_pieces + 1):
      piece_pos = (0, WIN_HEIGHT - i*PipePair.PIECE_HEIGHT)
      self.image.blit(body_image_pipe, piece_pos)
      end_y_bottom_pipe = WIN_HEIGHT - self.bottom_height_px
      bottom_end_piece_pos = (0, end_y_bottom_pipe - 
                             PipePair.PIECE_HEIGHT)
      self.image.blit(end_image_pipe, bottom_end_piece_pos)

      # top pipe
      for i in range(self.top_pipe_pieces):
          self.image.blit(body_image_pipe, (0, i *
               PipePair.PIECE_HEIGHT))
      end_y_top_pipe = self.top_height_px
      self.image.blit(end_image_pipe, (0, end_y_top_pipe))

# external end pieces are further added to make compensation
self.top_pipe_pieces += 1
self.bottom_pipe_pieces += 1

# for collision detection
self.mask = pygame.mask.from_surface(self.image)

@property
def height_topPipe_px(self):
    """returns the height of the top pipe, measurement is done in pixels"""
    return (self.top_pipe_pieces * PipePair.HEIGHT_PIECE)

@property
def height_bottomPipe_px(self):
    """returns the height of the bottom pipe, measurement is done in pixels"""
    return (self.bottom_pipe_pieces * PipePair.HEIGHT_PIECE)

@property
def visible(self):
    """Get whether this PipePair on screen, visible to the player."""
    return -PipePair.WIDTH < self.x < WINDOW_WIDTH

@property
def rect(self):
    """Get the Rect which contains this PipePair."""
    return Rect(self.x, 0, PipePair.WIDTH, PipePair.HEIGHT_PIECE)

def collides_with(self, bird):
    """check whether bird collides with any pipe in the pipe-pair. The
    collide-mask deploy a method which returns a list of sprites--in
    this case images of bird--which collides or intersect with
    another sprites (pipe-pair)
    
    Arguments:
    bird: The Bird which should be tested for collision with this 
        PipePair.
    """
    return pygame.sprite.collide_mask(self, bird)

def update(self, delta_frames=1):
    """Update the PipePair's position.
    
    Arguments:
    delta_frames: The number of frames elapsed since this method was
        last called.
    """
    self.x -= ANIMATION_SPEED * frames_to_msec(delta_frames)

def main():
    """Only function that will be externally called, this
    is main function
    
    Instead of importing externally, if we call this function from
    if name == __main__(), this main module will be executed.
    """

    pygame.init()

    display_surface = pygame.display.set_mode((WIN_WIDTH,
        WIN_HEIGHT)) #display for screen
    objectClock = pygame.time.Clock()
    images = loading_Images()

#at any moment of game, bird can only change its y position,
  so x is constant
    #lets put bird at center
    Objectbird = Bird((50, int(WIN_HEIGHT/2 - Bird.HEIGHT/2), 2,)
                   (images['WingUp'], images['WingDown']))
    pipes = deque()
#deque is similar to list which is preferred otherwise
    if we need faster operations like
#append and pop
    frame_clock = 0  # this counter is only incremented
      if the game isn't paused
done = paused = False
  while not done:
      clock.tick(FPS)
      # Handle this 'manually'.
        If we used pygame.time.set_timer(),
      # pipe addition would be messed up when paused.
      if not (paused or frame_clock %
        msec_to_frames(PipePair.ADD_INTERVAL)):
          pipe_pair = PipePair(images['endPipe'],
           images['bodyPipe'])
          pipes.append(pipe_pair)
#handling events
    #Since Flappy Bird is Tapped game
    #we will handle mouse events
    for anyEvent in pygame.event.get():
        #EXIT GAME IF QUIT IS PRESSED
        if anyEvent.type == QUIT or (anyEvent.type == KEYUP and
          anyEvent.key == K_ESCAPE):
             done = True
             break
        elif anyEvent.type == KEYUP and anyEvent.key in
          (K_PAUSE, K_p): paused = not paused
        elif anyEvent.type == MOUSEBUTTONUP or
            (anyEvent.type == KEYUP and anyevent.key in
            (K_UP, K_RETURN, K_SPACE)): bird.msec_to_climb =
            Bird.CLIMB_DURATION
        if paused:
            continue #not doing anything [halt position]

        # check for collisions
                pipe_collision = any(eachPipe.collides_with(bird)
                  for eachPipe in pipes)
                if pipe_collision or 0 >= bird.y or

                bird.y >= WIN_HEIGHT - Bird.HEIGHT:
                  done = True

            #blit background
            for position_x_coord in (0, WIN_WIDTH / 2):
                display_surface.blit(image['game_background'],
                   (position_x_coord, 0))
            #pipes that are out of visible, remove them
            while pipes and not pipes[0].visible:
                pipes.popleft()

            for p in pipes:
                p.update()
                display_surface.blit(p.image, p.rect)
            bird.update()
            display_surface.blit(bird.image, bird.rect)

                pygame.display.flip()
                frame_clock += 1
            print('Game Over!')
            pygame.quit()
#-----------------uptill here add it to main function--------------
if __name__ == '__main__':
  #indicates two things:
  #In case other program import this file, then value of
     __name__ will be flappybird
  #if we run this program by double clicking filename
     (flappybird.py), main will be called
    main()      #calling main function

score = 0
scoreFont = pygame.font.SysFont(None, 30, bold=True)   #Score default font:
WHITE

while not done:
    #after check for collision
    # procedure for displaying and updating scores of player
     for eachPipe in pipes:
         if eachPipe in pipes:
           eachPipe.score_counted:
            #when bird crosses each pipe
             score += 1
             eachPipe.score_counted = True
     Surface_Score = scoreFont.render(str(score),
        True, (255, 255, 255))  #surface
     x_score_dim = WIN_WIDTH/2 - score_surface.get_width()/2
     #to render score, no y-position
     display_surface.blit(Surface_Score, (x_score_dim,
        PipePair.HEIGHT_PIECE))   #rendering

    pygame.display.flip()   #update
    frame_clock += 1 
print('Game over! Score: %i' %score)
pygame.quit()

WIDTH = HEIGHT = 30 #change it to make space between pipe pairs
                     smaller/bigger
SINK_SPEED = 0.18 #speed at which bird falls
CLIMB_SPEED = 0.3 #when user taps on screen, it is climb speed

CLIMB_DURATION = 333.3

import pygame
import random

#declare GLOBALS
width = 800
height = 700

#since each shape needs equal width and height as of square
game_width = 300 #each block will have 30 width
game_height = 600 #each block will have 30 height 
shape_size = 30

#check top left position for rendering shapes afterwards

top_left_x, top_left_y = (width - game_width) // 2, height - game_height

#pseudocode for random movement
state.player_movement():
    if state.hits_boundary:
        state.change_movement()

#pseudocode for check if human player and computer are near
if state.player == "explore":
    if human(x, y) == computer(x, y):
        state.fire_player()
    else:
        state.player_movement()
from pygame.locals import *
from random import randint
import pygame
import time
from operator import *

class Player:
    x = [0] #x-position
    y = [0] #y-position
    size = 44 #step size must be same for Player, Computer, Food
    direction = 0 #to track which direction snake is moving
    length = 3 #initial length of snake

    MaxMoveAllow = 2
    updateMove = 0

    def __init__(self, length):
        self.length = length
        for i in range(0, 1800):
            self.x.append(-100)
            self.y.append(-100)
        
        # at first rendering no collision
        self.x[0] = 1 * 44
        self.x[0] = 2 * 44

def update(self):

    self.updateMove = self.updateMove + 1
    if gt(self.updateMove, self.MaxAllowedMove):

        # update previous to new position
        for i in range(self.length -1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # updating the position of snake by size of block (44)
        if self.direction == 0:
            self.x[0] = self.x[0] + self.size
        if self.direction == 1:
            self.x[0] = self.x[0] - self.size
        if self.direction == 2:
            self.y[0] = self.y[0] - self.size
        if self.direction == 3:
            self.y[0] = self.y[0] + self.size

        self.updateMove = 0

        def moveRight(self):
            self.direction = 0

        def moveLeft(self):
            self.direction = 1

        def moveUp(self):
            self.direction = 2

        def moveDown(self):
            self.direction = 3

        def draw(self, surface, image):
        for item in range(0, self.length):
        surface.blit(image, (self.x[item], self.y[item]))

class Computer:
    x = [0]
    y = [0]
    size = 44 #size of each block of snake
    direction = 0
    length = 3

    MaxAllowedMove = 2
    updateMove = 0

    def __init__(self, length):
        self.length = length
        for item in range(0, 1800):
            self.x.append(-100)
            self.y.append(-100)

        # making sure no collision with player
        self.x[0] = 1 * 44
        self.y[0] = 4 * 44

def update(self):
    if gt(self.updateMove, self.MaxAllowedMove):

        # Previous position changes one by one
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # head position change
        if self.direction == 0:
            self.x[0] = self.x[0] + self.size
        if self.direction == 1:
            self.x[0] = self.x[0] - self.size
        if self.direction == 2:
            self.y[0] = self.y[0] - self.size
        if self.direction == 3:
            self.y[0] = self.y[0] + self.size
        
        self.updateMove = 0

def moveRight(self):
    self.direction = 0
def moveLeft(self):
    self.direction = 1
def moveUp(self):
    self.direction = 2
def moveDown(self):
    self.direction = 3

def target(self, food_x, food_y):
    if gt(self.x[0] ,   food_x):
        self.moveLeft()

    if lt(self.x[0] , food_x):
        self.moveRight()

    if gt(self.y[0] , food_y):
        self.moveUp()

def draw(self, surface, image):
    for item in range(0, self.length):
        surface.blit(image,  (self.x[item], self.y[item]))

class Game:
    def checkCollision(self, x1, y1, x2, y2, blockSize):
        if ge(y1 , y2) and le(y1, y2 + blockSize):
             return True
        return False

class Frog:
    x = 0
    y = 0
    size = 44

    def __init__(self, x, y):
        self.x = x * self.size
        self.y = y * self.size

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))

class App:
    Width = 800 #window dimension 
    Height = 600 
    player = 0 #to track either human or computer
    Frog = 0 #food

    def __init__(self):
        self._running = True
        self._running = None
        self._image_surf = None
        self._Frog_surf = None
        self.game = Game()
        self.player = Player(5) #instance of Player with length 5 (5
        blocks
        self.Frog = Frog(8, 5) #instance of Frog with x and y position
        self.computer = Computer(5) #instance of Computer player with
        length 5

def loader(self):
    pygame.init()
    self.surface = pygame.display.set_mode((self.Width, self.Height),
    pygame.HWSURFACE)

    self._running = True
    self._image_surf = pygame.image.load("snake.jpg").convert()
    self._Frog_surf = pygame.image.load("frog-main.jpg").convert()

def on_event(self, event):
    if event.type == QUIT:
        self._running = False
def on_cleanup(self):
    pygame.quit()

def main(self):
    self.computer.target(self.Frog.x, self.Frog.y)
    self.player.update()
    self.computer.update()

def renderer(self):
    self.surface.fill((0, 0, 0))
    self.player.draw(self.surface, self._image_surf)
    self.Frog.draw(self.surface, self._image_surf)
    self.computer.draw(self.surface, self._image_surf)
    pygame.display.flip()

def handler(self):
    if self.loader() == False:
        self._running = False
    
    while (self._running):
        keys = pygame.key.get_pressed()

        if (keys = pygame.key.get_pressed())
            self.player.moveRight()

        if (keys[K_RIGHT]):
            self.player.moveRight()
        
        if (keys[K_LEFT]):
            self.player.moveLeft()
        
        if (keys[K_UP]):
            self.player.moveUp()
        
        if (keys[K_DOWN]):
            self.player.moveDown()

        self.main()
        self.renderer()

        time.sleep(50.0 / 1000.0);

if __name__ == "__main__":
    main = App()
    main.handler()

# Does human player snake eats Frog
for i in range(0, self.player.length):
    if self.game.checkCollision(self.Frog.x, self.Frog.y,
    self.player.x[i], self.player.y[i], 44):
        #after each player eats frog; next frog should be spawn in next
        position
        self.Frog.x = randint(2, 9) * 44
        self.Frog.y = randint(2, 9) * 44
        self.player.length = self.player.length + 1
# Does computer player eats Frog
for i in range(0, self.player.length):

    if self.game.checkCollision(self.Frog.x, self.Frog.y,
        self.computer.x[i], self.computer.y[i], 44):
        self.Frog.x = randint(2, 9) * 44
        self.Frog.y = randint(2, 9) * 44

# To check if the human player snake collides with its own body
for i in range(2, self.player.length):
    if self.game.checkCollision(self.player.x[0], self.player.y[0],
       print("You lose!"))
       exit(0)


pass

       self.computer.length = self.computer.length + 1