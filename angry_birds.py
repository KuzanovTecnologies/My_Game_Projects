from OpenGL.GL import *
from OpenGL.GLU import *

def renderCube():
    glBegin(GL_QUADS)
    for eachSurface in cube_Surfaces:
        for eachVertex in eachSurface:
            glColor3fv((1, 1, 0))  #yellow color code
            glVertex3fv(cube_Surfaces[eachVertex])
    glEnd()

    glBegin(GL_LINES)
      for eachEdge in cube_Edges:
        for eachVertex in eachEdge:
            glVertex3fv(cube_Vertices[eachVertex])
      glEnd()

def ActionHandler():
    pygame.init()
    screen = (800, 500)
    pygame.display.set_mode(screen, DOUBLEBUF|OPENGL)  #OPENGL is essential
    #1: ADD A CLIPPING TRANSFORMATION
    gluPerspective(85.0, (screen[0]/screen[1]), 0.1, 50)
    #  80.0 -> field view of camera
    #screem[0]/screen[1] -> aspect ratio (width/height)
    #0.1 -> near clipping plane
    #50 -> far clipping plane
    glRotatef(18, 2, 0, 0) #start point

while True:

    for anyEvent in pygame.event.get():
        if anyEvent.type == pygame.QUIT:
            pygame.quit()
            quit()
        if anyEvent.type == pygame.MOUSEBUTTONDOWN:
            print(anyEvent)
            print(anyEvent.button)  #printing mouse event
            #mouse button 4 and 5 are at the left side of the mouse
            #mouse button 4 is used as forward and backward navigation
            if anyEvent.button == 4:
                glTranslatef(0.0,0.0,1.0) #produces translation
                    of  (x, y, z)
            elif anyEvent.button == 5:
                glTranslatef(0.0,0.0,-1.0)

                glRotatef(1, 3, 1, 1)
#The glRotatef is used to perform matrix transformation which performs a
rotation
#of counterclockwise with an angle of degree about origin through the point
#provided as (x, y, z).
        #-----------------------------------------------------------------
        #indicates the buffer that needs to be cleared
        #GL_COLOR_BUFFER_BIT: enabled for color drawing
        #GL_DEPTH_BUFFER_BIT: depth buffer which needs to be cleared
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #render cube
        renderCube()
        pygame.display.flip()
        pygame.time.wait(12)

        #call main function only externally
        ActionHandler()

from pymunk.vec2d import Vec2d
print(Vec2d(2, 7) + Vec2d((3, 4)))

#results
Vec2d(2, 7)
Vec2d(5, 11)

print(Vec2d(3,4).get_distance(Vec2d(9,0)))
7.211102550927978

import pymunk
space = pymunk.Space()  #creating Space instance
body = pymunk.Body()  #creating Body instance
object = pymunk.circle(body, 4)
object.density = 2
#print body measurements
print("Mass : {:.0f} and Moment: {:.0f}".format(body.mass, body.moment))

space.add(body, object)
print("Mass: {:.0f} and Moment: {:.0f}",format(body.mass, body.moment))

Mass : 0 and Moment: 0 
Mass: 101 and Momnent: 804

pymunk.Circle(body, radius_of_circular_shape)

pymunk.Poly(body, vertices, transform = None, radius = 0)

pymunk.Segment(body, point1, point2, radius)

import pymunk as p #aliasing pymunk as p
from pymunk import Vec2d #for vector manipulation

class RoundBird():
    def __init__(self, distance, angle, x_pos, y_pos, space):
        weight = 5
        r = 12 #radius
        value_of_inertia = p.moment_for_circle(weight, 0, r, (0, ))
        obj_body = p.body(weight, value_of_inertia)
        obj_body.position = x_pos, y_pos
        power_value = distance * 53
        impulse = power_value * Vec2d(1, 0)
        angle = -angle
        obj_body.apply_impulse_at_local_point(impulse.rotated(angle))
        obj_shape = p.Circle(obj_body, r, (0, 0))
        obj_shape.elasticity = 0.95 #bouncing angry bird
        obj_shape.friction = 1 #for roughness
        obj_shape.collision_type = 0 #for checking collisions later 
        space.add(obj_body, obj_shape)
        #class RoundBird attribute ----
        self.body = obj_body
        self.shape = obj_shape

class RoundPig():
    def __init__(self, x_pos, y_pos, space):
        self.life = 20 #life will be decreased after
            collision of pig with bird
        weight = 5
        r = 14 #radius
        value_of_inertia = p.moment_for_circle(weight, 0, r, (0, 0))
        obj_body = p.body(weight, value_of_inertia)

        #creates virtual space to render shape
        obj_body.position = x_pos, y_pos
        #add circle to obj body
        obj_shape = p.Circle(obj_body, r, (0, 0))
        obj_shape.elasticity = 0.95
        obj_shape.friction = 1 
        obj_shape.collision_type = 1
        space.add(obj_body, obj_shape)
        self.body = obj_body
        self.shape = obj_shape 

import pymunk as pym
from pymunk import Vec2d
import Pygame as pg
import math

class Polygon():
    def __init__(self, position, length, height, space, mass=5.0):
        value_moment = 1000
        body_obj = pym.Body(mass, value_moment)
        body_obj.position = Vec2d(position)
        shape_obj = pym.Poly.create_box(body_obj, (length, height))
        shape_obj.color = (0, 0, 255)
        shape_obj.friction = 0.5
        shape_obj.collision_tyype = 2 #adding to check collision later
        space.add(body_obj, shape_obj)
        self.body = body.obj
        self.shape = shape_obj
        wood_photo = 
            pg.image.load("../res/photos/wood.jpg").convert_alpha()
        wood2_photo =
            pg.image.load("../res/photos/wood2.jpg").convert_alpha()
        rect_wood = pg.Rect(251, 357, 86, 22)
        self.beam_image = wood_photo.subsurface(rect_wood).copy()
        rect_wood2 = pg.Rect(16, 252, 22, 84)
        self.column_image = wood2_photo.subsurface(rect_wood2).copy()

def convert_to_pygame(self, pos):
    """Function that will transform pymunk coordinates to
         Pygame coordinates"""
    return int(pos.x), int(-pos.y+610)

def draw_poly(self, element, screen):
    """Draw beams and columns"""
    polygon = self.shape

    if element == "beams":
        pos = polygon.body.position
        pos = Vec2d(self.convert_to_pygame(pos))
        angle_degrees = math.degrees(polygon.body.angle)
        rotated_beam = pg.transform.rotate(self.beam_image,
                                                  angle_degrees)
        offset = Vec2d(rotated_beam.get_size()) / 2.

        pos = pos - offset
        final_pos = pos
        screen.blit(rotated_beam,   (final_pos.x, final_pos.y))

if element == 'columns':
    pos = polygon.body.position
    pos = Vec2d(self.convert_to_pygame(pos))
    angle_degrees = math.degrees(polygon.body.angle) + 180
    rotated_column = pg.transform.rotate(self.column_image,
                                               angle_degrees)
    offset = Vec2d(rotated_column.get_size()) / 2.
    pos = pos - offset
    final_pos = pos
    screen.blit(rotated_column, (final_pos.x, final_pos.y))

import os
import sys
import math
import time
import Pygame
import pymunk
from characters import RoundBird #our characters.py file here have Bird class

Pygame.init()
screen = Pygame.display.set_mode((1200, 650))
redbird = Pygame.image.load(
 "../res/photos/red-bird3.jpg").convert_alpha()
background_image = Pygame.image.load(
 "../res/photos/sling-3.jpg").convert_alpha()
full_sprite = Pygame.image.load(
 "../res/photos/full-sprite.jpg").convert_alpha()
rect_screen = Pygame.Rect(181, 1050, 50, 50)
cropped_image = full_sprite.subsurface(rect_screen).copy()
pig_image = Pygame.transform.scale(cropped_image, (30, 30))
#(30, 30) resulting height and width of pig

running = True
#base physics code
space_obj = pymunk.Space()
space_obj.gravity = (0.0, -700.0)

mouse_distance = 0 #distance after stretch
rope_length = 90

angle = 0 
mouse_x_pos = 0
mouse_y_pos = 0

mouse_pressed = False
time_of_release = 0 

initial_x_sling, initial_y_sling = 135, 450 #sling position at rest not 
stretched)
next_x_sling, next_y_sling = 160, 450

total_pig = []
total_birds = []
beams = []
columns = []
#color code
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Static floor
static_floor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
static_lines_first = [pymunk.Segment(static_floor_body, (0.0, 060.0),
(1200.0, 060.0), 0.0)]
static_lines_second = [pymunk.Segment(static_floor_body, (1200.0, 060.0),
(1200.0, 800.0), 0.0)]

#lets add elasticity and friction to surface
for eachline in static_lines_first:
    eachline.elasticity = 0.95
    eachline.friction = 1
    eachline.collision_type = 3
for eachline in static_lines_second:
    eachline.elasticity = 0.95
    eachline.friction = 1
    eachline.collision_type = 3
space_obj.add(static_lines_first)

def convert_to_pygame(pos):
    """ function that performs conversion of pymunk coordinates to
        Pygame coordinates"""
    return int(pos.x), int(-pos.y+600)

def vector(a, b):
    #return vector from points
    p = b[0] - a[0]
    q = b[1] - a[1]
    return (p, q)

def distance(x0, y0, x1, y1):
    """function to calculate the distance between two points"""
    dx = x1 - x0
    dy = y1 - y0
    dist = ((dx ** 2) + (dy ** 2)) ** 0.5
    return dist
def unit_vector(v):
    """ returns the unit vector of a point v = (a, b) """
    mag = ((v[0]**2)+(v[1]**2))**0.5
    if mag == 0:
        mag = 0.0000000000000001
    unit_p = v[0] / mag #formula to calculate unit vector:
vector[i]/magnitude
    unit_q = v[1] / mag
    return (unit_p, unit_q)

def sling_action():
    """will Set up sling action according to player input events"""
    global mouse_distance
    global rope_length
    global angle
    global mouse_x_pos
    global mouse_y_pos

#add code inside sling_action function
""" Fixing bird to the sling rope (Addressing picture 1)"""
vec = vector((initial_x_sling, initial_y_sling), (mouse_x_pos,
mouse_y_pos))
unit_vec = unit_vector(vec)
uv_1 = unit_vec[0]
uv_2 = unit_vec[1]

mouse_distance = distance(initial_x_sling, initial_y_sling, mouse_x_pos,
mouse_y_pos)
#mouse_distance = is a distance between sling initials point to the point at
which current bird is

fix_pos = (uv_1*rope_length+initial_x_sling,
uv_2*rope_length+initial_y_sling)
highest_length = 102 #when stretched

#to make bird stay within rope
x_redbird = mouse_x_pos - 20
y_redbird = mouse_y_pos - 20
if mouse_distance > rope_length:
    pux, puy = fix_pos
    pux -= 20
    puy -= 20
    first_pos = pux, puy
    screen.blit(redbird, first_pos)
    second_pos = (uv_1*highest_length+initial_x_sling,
uv_2*highest_length+initial_y_sling) #current position ==> second_pos
    Pygame.draw.line(screen, (255, 0, 0), (next_x_sling, next_y_sling),
        second_pos, 5)
    #front side catapult rope
    screen.blit(redbird, first_pos)
    Pygame.draw.line(screen,  (255, 0, 0), (initial_x_sling,
       initial_y_sling), second_pos, 5)
    #ANOTHER SIDE of catalpult
else:
    #when rope is not fully stretched
    mouse_distance += 10
    third_pos = (uv_1*mouse_distance+initial_x_sling,
      uv_2*mouse_distance+initial_y_sling)
    Pygame.draw.line(screen, (0, 0, 0), (initial_x_sling,
       initial_y_sling), third_pos, 5)
#this is angle of impulse (angle at which bird is projected)
change_in_y = mouse_y_pos - initial_y_sling
change_in_x = mouse_x_pos - initial_x_sling
if change_in_x == 0:
    #if no change in x, we make fall within the area of sling
    dx = 0.00000000000001
angle = math.atan((float(change_in_y))/change_in_x)  #tan(dy / dx)

def post_solve_bird_pig(arbiter, space_obj, _):
    """Action to perform after collision between bird and pig"""

    object1, object2 = arbiter.shapes #Arbiter class obj
    bird_body = object1.body
    pig_body = object2.body
    bird_position = convert_to_pygame(bird_body.position)
    pig_position = convert_to_pygame(pig_body.position)
    radius = 30
    Pygame.draw.circle(screen, (255, 0, 0), bird_position, radius, 4)
       #screen => Pygame surface
    Pygame.draw.circle(screen, RED, pig_position, radius, 4)
    #removal of pig
    pigs_to_remove = []
    for pig in total_pig:
        if pig_body == pig.body:
            pig.life -= 20 #decrease life
            pigs_to_remove.append(pig)
    
    for eachPig in pigs_to_remove:
        space_obj.remove(eachPig.shape, eachPig.shape.body)
        total_pig.remove(eachPig)
def post_solve_bird_wood(arbiter, space_obj, _):
    """Action to perform after collision between bird and wood structure"""
    #removing polygon
    removed_poly = []
    if arbiter.total_impulse.length > 1100:
        object1, object2 = in columns:
        for Each_column in columns:
            if object2 == Each_column.shape:
                removed_poly.append(Each_column)
        for Each_beam in beams:
            if object2 == Each_beam.shape:
                removed_poly.append(Each_beam)
        for Each_poly in removed_poly:
            if Each_poly in columns:
                columns.remove(Each_poly)
            if Each_poly in beams:
                beams.remove(Each_poly)
        space_obj.remove(object2, object2.body)
        #you can also remove bird if you want

def post_solve_pig_wood(arbiter, space_obj, _):
    """Action to perform after collision between pig and wood"""
    removed_pigs = []
    if arbiter.total_impulse.length > 700:
        pig_shape, wood_shape = arbiter.shapes
        for pig in total_pig:
            if pig_shape == pig.shape:
                pig.life -= 20

                if pig.life <= 0: #when life is 0


                    removed_pigs.append(pig)
        for Each_pig in removed_pigs:
            space_obj.remove(Each_pig.shape, Each_pig.shape.body)
            total_pig.remove(Each_pig)

    # bird and pigs
    space.add_collision_handler(0, 1).post_solve=post_solve_bird_pig
    # bird and wood
    space.add_collision_handler(0, 1).post_solve=post_solve_bird_wood
    # pig and wood
    space.add_collision_handler(1, 2).post_solve=post_solve_pig_wood

from characters import RoundPig #HAVE TO ADD PIG IN STRUCTURE
from polygon import Polygon #POLYGON

class Level():
    #each level will be construct by beam, column, pig
    #will create wooden structure
    def __init__(self, pigs_no, columns_no, beams_no, obj_space):
        self.pigs = pigs_no #pig number
        self.columns = columns_no
        self.beams = beams_no
        self.space = obj_space
        self.number = #to create build number
        self.total_number_of_birds = 4 #total number of initial bird


def build_0(self):

    pig_no_1 = RoundPig(980, 100, self.space)
    pig_no_2 = RoundPig(985, 182, self.space)
    self.pigs.append(pig_no_1)
    self.pigs.append(pig_no_2)
    pos = (950, 80)
    self.columns.append(Polygon(pos, 20, 85, self.space))
    pos = (1010, 80)
    self.columns.append(Polygon(pos, 20, 85, self.space))
    pos = (980, 150)
    self.beams.append(Polygon(pos, 85, 20, self.space))
    pos = (950, 200)
    self.columns.append(Polygon(pos, 20, 85, self.space))
    pos = (1010, 200)
    self.columns.append(Polygon(pos, 20, 85, self.space))
    pos = (980, 240)
    self.beams.append(Polygon(pos, 85, 20, self.space))
    self.total_number_of_birds = 4


def load_level(self):
    try:
        level_name = "build_"+str(self.number)
        getattr(self, level_name)()
    except AttributeError:
        self.number = 0
        level_name = "build_"+str(self.number)
        getattr(self, level_name)()

#write it in main.py file
from level import Level
level = Level(total_pig, columns, beams, space)
level.number = 0
level.load_level()

while running
    # handle Input events
    for eachEvent in Pygame.event.get()
        if eachEvent.type == Pygame.QUIT:
            running = False
        elif eachEvent.type == Pygame.KEYDOWN and event.key ==
          Pygame.K_ESCAPE:
            running = False

if (Pygame.mouse.get_pressed()[0] and mouse_x_pos > 100 and
        mouse_x_pos < 250 and mouse_y_pos > 370 and mouse_y_pos < 550):
if (event.type == Pygame.MOUSEBUTTONUP and 
        event.button == 1 and mouse_pressed):

# Release new bird
mouse_pressed = False
if level.number_of_birds > 0:
    level.number_of_birds -= 1
    time_of_release = time.time()*1000
    x_initial = 154
    y_initial = 156

#add code after x-initial and y-initial declaration
if mouse_distance > rope_length:
    mouse_distance = rope_length
if mouse_x_pos < initial_x_sling+5:
    bird = RoundBird(mouse_distance, angle, x_initial, y_initial,
    space_obj)
    total_birds.append(bird)
if level.number_of_birds
    game_finish_time = time.time()

mouse_x_pos, mouse_y_pos = Pygame.mouse.get_pos()
# Blit the background image

screen.fill((130, 200, 100))
screen.blit((background_image, (0, -50)))

# Blitting the first part of sling image
rect = Pygame.Rect(50, 0, 70, 220)
screen.blit(sling_image, (138, 420), rect)

# Blit the remaining number of angry bird
if level.total_number_of_birds > 0:
    for i in range(level.total_number_of_birds-1):
        x = 100 - (i*35)
        screen.blit(redbird, (x, 508))

# Draw sling action checking user input
if mouse_pressed and level.total_number_of_birds > 0:
    sling_action()
else: #blit bird when there is no stretch of sling
    if time.time()*1000 - time_of_release > 300 and
      level.number_of_birds > 0:
        screen.blit(redbird, (130, 426))

removed_bird_after_sling = []
removed_pigs_after_sling = []
# Draw total_birds
for bird in total_birds:
    if bird.shape.body.position.y < 0:
        removed_bird_after_sling.append(bird)
    pos = convert_to_pygame(bird.shape.body.position)
    x_pos, y_pos = pos
    x_pos -= 22 #Pygame compatible
    y_pos -= 20
    screen.blit(redbird, (x_pos, y_pos)) #blit bird
    Pygame.draw.circle(screen, BLUE,
                      pos, int(bird.shape.radius), 2)  #creates blue circle
                                                        at the edge of bird

# Remove total_birds and total_pig
for bird in removed_bird_after_sling:
    space_obj.remove(bird.shape, bird.shape.body)
    total_birds.remove(pig.shape, pig.shape.body)
for pig in removed_pigs_after_sling:
    space_obj.remove(pig.shape, pig.shape.body)
    total_pig.remove(pig)

# Draw total_pig
for Each_pig in total_pig:

    pig = Each_pig.shape
    if pig.body.position.y < 0: #when pig hits ground or fall to the ground
        removed_pigs_after_sling.append(pig)
    
    pos = convert_to_pygame(pig.body.position) #pos is a tuple
    x_pos, y_pos = pos

    angle_degrees = math.degrees(pig.body.angle)
    pig_rotated_img = Pygame.transform.rotate(pig_image, angle_degrees)
    #small random rotation within wooden frame
    width,height = pig_rotated_img.get_size()
    x_pos -= width*0.5
    y_pos -= height*0.5
    screen.blit(pig_rotated_img, (x_pos, y_pos))
    Pygame.draw.circle(screen, BLUE, pos, int(pig.radius), 2)

# Draw columns and Beams
#beam and column are object of Poly class
for column in columns:
    column.draw_poly('columns', screen)
for beam in beams:
    beam.draw_poly('beams', screen)

time_step_change = 1.0/50.0/2.

#time_step_change = 1.0/50.0/2.
for x in range(2):
    space_obj.step(time_step_change) # This causes two updates for frame

# Blitting second part of the sling
rect_for_sling = Pygame.Rect(0, 0, 60, 200)
screen.blit(sling_image, (120, 420), rect_for_sling)

Pygame.display.flip()  #updating the game objects
clock.tick(50)

def load_music():
    """Function that will load the music"""
    song_name = '../res/sounds/angry-birds.ogg'
    Pygame.mixer.music.load(song_name)
    Pygame.mixer.music.play(-1)

    load_music()

def build_1(self):
    """Function that will render level 1"""
    obj_pig = RoundPig(1000, 100, self.space)
    self.pigs.append(obj_pig)
    pos = (900, 80)
    self.columns.append(Polygon(pos, 20, 85, self.space))
    pos = (850, 80)
    self.columns.append(Polygon(pos, 20, 85, self.space))
    pos = (850, 150)
    self.columns.append(Polygon(pos, 20, 85, self.space))
    pos = (1050, 150)
    self.columns.append(Polygon(pos, 20, 85, self.space))
    pos = (1105, 210)
    self.beams.append(Polygon(pos, 85, 20, self.space))
    self.total_number_of_birds = 4 #reduce the number to
       make game more competitive

