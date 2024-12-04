#------------------- IMPORTS -------------------

import pygame
import time
import random
import math
pygame.init()


from Functions import scale_image
from Functions import blit_rotate_centre


#------------------- FILE LOADING -------------------

# Import map image
MAP = scale_image(pygame.image.load("imgs/MainMap.png"), 0.3)

# Import veicle images 
MOPED = scale_image(pygame.image.load("imgs/RedMoped.png"), 0.015)
PICKUP = scale_image(pygame.image.load("imgs/OrangePickup.png"), 0.015)
VAN = scale_image(pygame.image.load("imgs/BlueVan.png"), 0.015)
LORRY = scale_image(pygame.image.load("imgs/GreenLorry.png"), 0.015)
UFO = scale_image(pygame.image.load("imgs/Ufo.png"), 0.015)

# -- ANIMATIONS --

# -- SOUNDS --

WIN = pygame.display.set_mode((1280,1024))
pygame.display.set_caption("2Delivery")

# ------------------- MAIN CODE -------------------

# -- TEMP CODE --
carSelection = LORRY

# -- CLASSES --

class AbstractCar:

    def __init__ (self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left = False, right = False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_centre(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

class playerCar(AbstractCar):
    IMG = carSelection
    START_POS = (550,550)


def draw(win, images, player_car):
    for img,pos in images:
        win.blit(img, pos)

        player_car.draw(win)
        pygame.display.update()


# -- CLOCK --

FPS = 60
clock = pygame.time.Clock()

# -- IMAGES --

images = [(MAP, (0,0))]

# -- PLAYER CAR --

player_car = playerCar(4,4)

# -- EVENT LOOP --

run = True

while run:

    clock.tick(FPS)

    # -- DISPLAY IMAGES --

    draw(WIN, images, player_car)
   
    # -- EVENT LOOP --

    for event in pygame.event.get():
        
        # -- QUIT --

        if event.type == pygame.QUIT:
            run = False
            break
            

    # -- KEY PRESSES --

    keys = pygame.key.get_pressed()

    moved = False
    # W key is pressed
    if keys[pygame.K_w]:
        player_car.move_forward()
        moved = True
        
    # S key is pressed
    if keys[pygame.K_s]:
        player_car.move_backward()
        moved = True

    # Akey is pressed
    if keys[pygame.K_a]:
        player_car.rotate(left = True)

    # Dkey is pressed
    if keys[pygame.K_d]:
        player_car.rotate(right = True)
    
    # NO CLICK
    if not moved:
        player_car.reduce_speed()
   
pygame.quit()