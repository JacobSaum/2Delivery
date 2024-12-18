#------------------- IMPORTS -------------------

import pygame
import time
import random
import math
import csv
pygame.init()
pygame.font.init()


from Functions import scale_image
from Functions import blit_rotate_centre

#edit

#------------------- FILE LOADING -------------------

# Import map image
MAP = scale_image(pygame.image.load("imgs/MainMap.png"), 0.3)
MAP_COLLISIONS = scale_image(pygame.image.load("imgs/CollisionMap.png"), 3)
MAP_COLLISIONS_MASK = pygame.mask.from_surface(MAP_COLLISIONS)

# Import veicle images 
MOPED = scale_image(pygame.image.load("imgs/RedMoped.png"), 0.01)
PICKUP = scale_image(pygame.image.load("imgs/OrangePickup.png"), 0.01)
VAN = scale_image(pygame.image.load("imgs/BlueVan.png"), 0.01)
LORRY = scale_image(pygame.image.load("imgs/GreenLorry.png"), 0.01)
UFO = scale_image(pygame.image.load("imgs/Ufo.png"), 0.01)
COINS_UI = scale_image(pygame.image.load("imgs/CoinsUI.png"), 0.03)
PARCEL_UI = scale_image(pygame.image.load("imgs/ParcelUI.png"), 0.03)
SPEED_UI = scale_image(pygame.image.load("imgs/SpeedUI.png"),0.02)

# Import Fonts
UI_FONT = pygame.font.Font("Fonts/PixelifySans-SemiBold.ttf", 44)

# -- ANIMATIONS --

# -- SOUNDS --

WIN = pygame.display.set_mode((1280,1024))
pygame.display.set_caption("2Delivery")

# ------------------- MAIN CODE -------------------

# -- TEMP CODE --
carSelection = MOPED

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

    def rotate(self, left=False, right=False):
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

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

class playerCar(AbstractCar):   
    IMG = carSelection
    START_POS = (150,500)

    def bounce(self):
        self.vel = -0.5 * self.vel
        self.move()

def draw(win, images, uiimages, player_car):
    for img,pos in images:
        win.blit(img, pos)

    player_car.draw(win)
    
    for img,pos in uiimages:
        win.blit(img, pos)

    
    pygame.display.update()

    


# -- CLOCK --

FPS = 60
clock = pygame.time.Clock()

# -- IMAGES --

images = [(MAP, (0,0))]
uiImages = [(PARCEL_UI, (15,15)), (SPEED_UI, (15,915)), (COINS_UI, (15,200))]

# -- PLAYER CAR --

player_car = playerCar(4,4)

# -- EVENT LOOP --

run = True

while run:

    clock.tick(FPS)

    # -- DISPLAY IMAGES --

    draw(WIN, images, uiImages, player_car)

    # -- EVENT LOOP --

    for event in pygame.event.get():
        
        # -- QUIT --

        if event.type == pygame.QUIT:
            run = False
            break

    if player_car.collide(MAP_COLLISIONS_MASK) != None:
        player_car.bounce()
            

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

    # A key is pressed
    if keys[pygame.K_a] and player_car.vel != 0:
        player_car.rotate(left=True)

    # D key is pressed
    if keys[pygame.K_d] and player_car.vel != 0:
        player_car.rotate(right=True)
    
    # no key is pressed
    if not moved:
        player_car.reduce_speed()
    
    #if esc key is pressed
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    #def handle_collision(player_car):
        #if player_car.collide(MAP_COLLISIONS_MASK) != None:
            #player_car.bounce()

    #handle_collision(player_car)
   
pygame.quit()