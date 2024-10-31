import sys
import pygame
import time
import random

# Initialize Pygame
pygame.init()

size = width, height = 720, 640
speed = [2, 2]
black = 0, 0, 0
orange =255,165,0
green =0,128,0

# Set the size of the display window 
screen = pygame.display.set_mode(size)

# Load a spherical image to display 
ball = pygame.image.load("ball3.png")                       
ballrect = ball.get_rect()

# random color generation
def random_color_box():
    r= random.randint (0,255)
    g= random.randint (0,255)
    b= random.randint (0,255)
    return r,g,b 
border_color =random_color_box()

# Game main loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        border_color= random_color_box() 
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        border_color = random_color_box()
        
    
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.draw.rect(screen, border_color,ballrect,10)
    # draw border of box
    pygame.display.flip()
    
    pygame.time.wait(10)