import pygame
import time
import random

# initialize a screen and choose the size of the window and cells
pygame.init()
print('Please define the size of the window')
window = (int(input('x-axis:  ')), int(input('y-axis:  ')))
cell = int(input('Which width should the cells have:  '))  
screen = pygame.display.set_mode(window)


# colors in use
purple = (166, 133, 188)
orange = (255,128,0)
lime = (211, 244, 193)
green = (0, 255, 0)
                 
grid = []
visited = []
backtrack = []


def draw_walls(x, y, w, size):

    ''' Function that builds a grid net where every squared cell has four walls.

    Parameters: Takes the x and y coordinates, the width of the cell and the size of the window.

    Returns: a picture of the grid net and a list containing the coordinates for every cell.
    '''
 
    for i in range(2, (size[1]//w)):
        x = w                                                            
        y = y + w                                                        
        for j in range(2, (size[0]//w)):
            pygame.draw.rect(screen, purple,( x, y, w, w), 3)
            grid.append((x,y))                                            
            x = x + w                                                   
            

def draw_up(x, y, w):
    pygame.draw.rect(screen, lime, (x + 1 , y - w + 1, w-2, w*2-2), 0)         
    pygame.display.update()                                              


def draw_down(x, y, w):
    pygame.draw.rect(screen, lime, (x +1 , y + 1 , w-2, w*2-2), 0)
    pygame.display.update()


def draw_left(x, y, w):
    pygame.draw.rect(screen, lime, (x - w + 1, y+1 , w*2-2, w-2), 0)
    pygame.display.update()


def draw_right(x, y, w):
    pygame.draw.rect(screen, lime, (x + 1 , y+1 ,  w*2-2, w-2), 0)
    pygame.display.update()


def moving_cell( x, y, w):
    # The moving cell seen as orange
    pygame.draw.rect(screen, orange, (x +2, y +2, w-4, w-4), 0)    
    pygame.display.update()



def backtracked_cell(x, y, w):
    # Re-color the orange path to lime
    pygame.draw.rect(screen, lime, (x +2, y +2, w-4, w-4), 0) 
    
                                           

def build_maze(x, y, w):

    ''' Function which looks for avaliable directions for the cell to move. 

    Parameters: Takes the current cells x and y coordinates and the width of the cell.

    Returns: It chose a random direction and calls for its function that draws the path.

    '''
    moving_cell(x, y, w)    
    backtrack.append((x,y))                                            
    visited.append((x,y))   
    
    while len(visited) != len(grid):   
        time.sleep(0.07)                                            
        neighbours = [] 

        if (x, y - w) not in visited and (x , y - w) in grid:      # north
            neighbours.append((x , y - w))

        if (x + w, y) not in visited and (x + w, y) in grid:       # east
            neighbours.append((x + w, y))                                   

        if (x , y + w) not in visited and (x , y + w) in grid:     # south
            neighbours.append((x , y + w))

        if (x - w, y) not in visited and (x - w, y) in grid:       # west
            neighbours.append((x - w, y))

       
        if len(neighbours) > 0:                                                      
            direction = (random.choice(neighbours))
            if direction == (x , y - w):                
                draw_up(x, y, w)
                y = y - w
                
                visited.append((x, y))
                backtrack.append((x, y))
                moving_cell(x, y, w)

            elif direction == (x + w, y):                                            
                draw_right(x, y, w)                                  
                x = x + w
                
                visited.append((x, y))                              
                backtrack.append((x, y)) 
                moving_cell(x, y, w)

            elif direction == (x , y + w):               
                draw_down(x, y, w)
                y = y + w
                
                visited.append((x, y))
                backtrack.append((x, y))  
                moving_cell(x, y, w)
                
            elif direction == (x - w, y):          
                draw_left(x, y, w)
                x = x - w
                
                visited.append((x, y))
                backtrack.append((x, y))
                moving_cell(x, y, w)


        else:           
            x, y = backtrack.pop()                                    
            moving_cell(x, y, w)                                      
            backtracked_cell(x, y, w)     
            

    if len(visited) == len(grid):          
         backtracked_cell(x, y, w)
         pygame.display.update()
         maze = 'Labyrinth.png'
         pygame.image.save(screen, maze)


start_x, start_y = cell, cell
draw_walls(0, 0, cell, window)             
build_maze(start_x, start_y, cell)               


#Main loop

done = False

while not done:
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
             done = True
            


