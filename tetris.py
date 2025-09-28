#following is for shape I
""" first element of list represents original structure,
    Second element represents rotational shape of objects """


I = ['..0..',
      '..0..',
      '..0..',
      '..0..',
#for square shape
O = [['.....',
      '.....',
      '0000.',
      '.....',
      '.....',
      '.....',]]

#for shape J
J = [['.....',
      '.0...',
      '.0...',
      '.....',
      '.....',
      '..0..',
      '.....',
      '...0.',
      '.....',
      '.....',
      '..0..',
      '..0..',
      '.00..',
      '.....',]]

#for shape L
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....',
      '.....',
      '.....',
      '..0..',
      '..00.',]]

    [['.....',
      '.....',
      '.....',
      '.0...',
      '.....',
      '.00..',
      '..0..',
      '..0..',
      '.....',]]

game_objects = [I, O, J, L, T] #you can create as many as you want
objects_color = [(255, 255, 0), (255, 0, 0), (255, 0, 0, 255), (255, 255, 0),
(128, 165, 0)]

#observe that this is not defined inside any class
def build_Grid(occupied = {}):
    shapes_grid = [(0, 0, 0) for _ in range (10) for _ in range(20)]
    for row in rangelen(shapes_grid)]
        for column in range(len(shapes_grid[row])):
            if (column, row) in occupied:
                piece = occupied[(column, row)]
                shapes_grid[row][column] = piece
return shapes_grid


class Shape:
    no_of_rows = 20 #for y dimension
    no_of_columns = 10 #for x dimension
    #constructor
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        #class attributes
        self.color = objects_color[(game_objects.index(shape))]
#get color based on character indicated by shape name or shape variable
        self.rotation = 0
def generate_shapes():
     global game_objects, objects_color
     return Shape(4, 0, random.choice(game_objects))  #creating instance
def create_Grid(screen_surface, grid_scene):
      screen_surface.fill(0, 0, 0)  #black background

    for i in range(len(grid_scene)):
    for j in range(len(grid_scene[i])):

#draw main rectangle which represents window
    pygame.draw.rect(screen_surface, grid_scene[i][j], (top_left_x +
      j* 30, top_left_y + i * 30, 30, 30), 0)
#above code will draw a rectangle at the middle of surface screen
   build_Grid(screen_surface, 20, 10)  #creating grid positions
   pygame.draw.rect(screen_surface,  (255, 0, 0), (top_left_x, top_left_y,
     game_width, game_height),  5)
   pygame.display.update()

"""function that will create borders in each row and column positions """

def show_grid(screen_Surface, grid):
    """ --- following two variables will show from where to
     draw lines---- """
   side_x = top_left_x
   side_y = top_left_y
   for eachRow in range(grid):
       pygame.draw.line(screen_Surface, (128,128,128), (side_x, side_y+
       eachRow*30),  (side_x + game_width, side_y + eachRow * 30
        # drawing horizontal lines (30)
       for eachCol * 30, side_y),  (side_y),  (side_x + eachCol * 30, side_y +
              game_height))
           # drawing vertical group of lines

def main():
occupied = {} # this refers to the shapes occupied into the screen
grid = build_Grid(occupied)

done = False
current_shape = generate_shapes()  #random shapes chosen from the lists.
next_shape = generate_shapes()
clock = pygame.time.Clock()
time_of_fall = 0 #for automatic fall of shapes

while not done:
for eachEvent in pygame.event.get():
if eachEvent.type == pygame.QUIT:
done = True
exit()

if anyEvent.type == pygame.KEYDOWN:
        if anyEvent.key == pygame.K_RIGHT:
            current_shape.x -= 1   #go left with shape

        elif anyEvent.key == pygame.K_RIGHT:
            current_shape.x += 1   #go right with shape
        elif anyEvent.key == pygame.K_UP:
            # rotate shape with angle of rotation
             (rotation variable)
            current_shape.rotation = current_shape.rotation + 1 %
             len(current_shape.game_objects)
        if anyEvent.key == pygame.K_DOWN:
            # moving current shape down into the grid
            current_shape.y += 1
        create_Grid(screen_surface) #screen surface will be initialized with
                                     pygame below
        screen_surface = pygame.display.set_mode((width, height))
        main() #calling only

        #for square shapes
        square = [['.....',
              '.....',
              '.00..',
              '.00..',
              '.....']]

def define_shape_position(shape_piece):
    positions = []
    list_of_shapes = shape_piece.game_objects[shape_piece.rotation %
                     len(shape_piece.shape)]
for i, line in enumerate(list_of_shapes):
    row = list(line)
    for j, column in enumerate(row):
        if column == '0':
            positions.append((shape_piece.x + j, shape_piece.y + i))

for p, block_pos in enumerate(positions):
    positions[p] = (block_pos[0] - 2, block_pos[1] - 4)

return positions

def check_Moves(shape, grid):
    """ checking if the background color of particular position is
        black or not, if it is, that means position is not occupied """

    valid_pos = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)]
                for i in range(20)]
    """ valid_pos contains color code in i variable and
        position in j variable--we have to filter to get only
        j variable """
    valid_pos = [j for p in valid_pos for j in p]
           """ list comprehension --same as writing
                    for p in valid_pos:
                        for j in p:
                            p
                            """
""" Now get only the position from such shapes using
    define_shape_position function """
shape_pos = define_shape_position(shape)

"""check if pos is valid or not """
for eachPos in shape_pos:
    if eachPos not in valid_pos:
        if eachPos[1] > -1: #eachPos[1] represents y value of shapes
          and if it hits boundary
            return False #not valid move
return True

global grid

occupied = {} # (x pos, y pos)  :   (128, 0, 128)
grid = build_Grid(occupied)
change_shape = False
done = False
current_shape = generate_shapes()
next_shape = generate_shapes()
clock = pygame.time.Clock()
timeforFall = 0

while not done:
speedforFall = 0.25

grid = build_Grid(occupied)
timeforFall += clock.get_rawtime()
clock.tick()

# code for making shape fall freely down the grid
if timeforFall/1000 >= speedforFall:

timeForFall = 0
current_shape.y += 1 #moving downward
#moving freely downward for invalid moves
if not (check_Moves(current_shape, grid)) and current_shape.y > 0:
current_shape.y -= 1
change_shape = True

if anyEvent.type == pygame.KEYDOWN:
                if anyEvent.key == pygame.K_LEFT:
                    current_shape.x -= 1
                    if not check_Moves(current_shape, grid):
""" ROTATING OBJECTS """
            elif anyEvent.key == pygame.K_UP:
                current_shape.rotation = current_shape.rotation + 1 %
                    len(current_shape.shape)
                if not check_moves(current_shape, grid):
                    current_shape.rotation = current_shape.rotation - 1
                        % len(current_shape.shape)
"""Moving faster while user presses down action key """
                if anyEvent.key == pygame.K_DOWN:
                    current_shape.y += 1
                    if not check_Moves(current_shape, grid):
                        current_shape.y -= 1
                position_of_shape = define_shape_position(current_shape)
                """ define_shape_function was created to return position of blocks of
                an object """

                # adding color to each objects in to the grid.
                for pos in range(len(position_of_shape)):
                    x, y = position_of_shape[pos]
                    """ when shapes is outside the main grid, we don't care """
                    if y > -1: # But if we are inside the screen or grid, 
                    we add color
                     grid[y][x] = current_shape.color #adding color to the grid
if change_shape:
        for eachPos in position_of_shape:
            pos = (eachPos[0], eachPos[1])
            occupied[pos] = current_shape.color
            current_shape = next_shape
            next_shape = generate_shapes()
            change_shape = False

create_Grid(screen_surface, grid)

def delete_Row(grid, occupied):
    # check if the row is occupied or not
    black_background_color
    number_of_rows_deleted = 0
    for i in range(len(grid)[i]
        eachRow = grid[i]
        if black_background_color not in eachRow:
            number_of_rows_deleted += 1
            index_of_deleted_rows = i
            for j in range(len(eachRow)):
                try:
                    del occupied[(j, i)])
                except:
                    continue
#code should be added within delete_Row function outside for loop
if number_of_rows_deleted > 0:          #if there is at least one rows deleted
    for position in sorted(list(occupied), position=lambda x:
    x[1])[::-1]:
    x, y = position
    if y < index_of_deleted_rows:
        """ shifting operation """
        newPos = (x, y + number_of_rows_deleted)
        occupied[newPos] = occupied.pop(position)

return number_of_rows_deleted

def main():
    ...
    while not done:
        ...
        if change_shape:
            ...
            change_shape = False
            delete_Row(grid, occupied)
def Welcome_Screen(surface):
    done = False
    while not done:
        surface.fill((128,0,128))
        font = pygame.font.SysFont("comicsans", size, bold=True
        label = font.render('Press ANY Key To Play Tetris!!', 1, (255, 255,
        255)))

        surface.blit(label, (top_left_x + game_width /2 - 
        label.get_width()/2, top_left_y + game_height/2 - 
        label.get_height()/2))

        pygame.display.update()
        for eachEvent in pygame.event.get():
            if eachEvent.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                main(surface) #calling main when user enters Enter key

        pygame.display.quit()

        timeforLevel = 0

        while not done:
            speedforFall = 0.27 - timeforLevel
            ...
            if timeforLevel / 10000 > 0.5:
                timeforLevel = 0
                if timeforLevel > 0.15:
                    timeforLevel += 0.05
            ...
    """ -----------------------------------------------------
            speedforFall = 0.24 will make object to fall faster comparative 
                            to speedforFall = 0.30 
        ----------------------------------------------------- """

def increaseSpeed(score):
    game_level = int(score*speedForFall)
    speedforFall = 0.28 - (game_level)
    return speedforFall

import pygame
from pygame.locals import *
window_screen = pygame.display.set_mode((640, 480), 
  HWSURFACE|OPENGL|DOUBLEBUF)

#Draw a geometry for the scene 
def draw():
 #translation (moving) about 6 unit into the screen and 1.5 unit to left
    glTranslatef(-1.5,0.0,-6.0)
    glBegin(GL_TRIANGLES)  #GL_TRIANGLE is constant for TRIANGLES
    glVertex3f( 0.0, 1.0, 0.0)  #first vertex
    glVertex3f(-1.0, -1.0, 0.0)  #second vertex
    glVertex3f( 1.0, -1.0, 0.0)  #third vertex
    glEnd()

    glBegin(GL_QUADS)
    glColor(0.0, 1.0, 0.0)  # vertex at y-axis
    glVertex(1.0, 1.0, 0.0) # Top left
    glVertex(1.0, 1.0, 0.0) # Top right

    glVertex(1.0, 1.0, 0.0) # Bottom right
    glVertex(1.0, 1.0, 0.0) # Bottom left
    glEnd()

from OpenGL.GL import *
from OpenGL.GLU import *

def change_View():
    pass
glViewport(0, 0 , WIDTH, HEIGHT)

glMatrixMode(GL_PROJECTION) #first step to apply projection matrix

aspect_ratio = float(width/height)
glLoadIdentity()
gluPerspective(40., aspect_ratio, 1., 800.)

glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

cube_Vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
)

cube_Edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),    
)

cube_Surfaces = (
  (0,1,2,3),
  (3,2,7,6),
  (6,7,5,4),
  (4,5,1,0),
  (1,5,7,2),
  (4,0,3,6)
)