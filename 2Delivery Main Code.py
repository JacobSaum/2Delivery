#------------------- IMPORTS -------------------

import pygame
import time
import random
import math
import csv
pygame.init()
pygame.font.init()
pygame.mixer.init()



from Functions import scale_image
from Functions import blit_rotate_centre

#------------------- FILE LOADING -------------------

# Import map image
MAP = scale_image(pygame.image.load("imgs/MainMap.png"), 1.005)
MAP_COLLISIONS = scale_image(pygame.image.load("imgs/CollisionMap.png"), 0.1005)
MAP_COLLISIONS_MASK = pygame.mask.from_surface(MAP_COLLISIONS)

# Import veicle images 
MOPED = scale_image(pygame.image.load("imgs/RedMoped.png"), 0.0033)
PICKUP = scale_image(pygame.image.load("imgs/OrangePickup.png"), 0.0033)
VAN = scale_image(pygame.image.load("imgs/BlueVan.png"), 0.0033)
LORRY = scale_image(pygame.image.load("imgs/GreenLorry.png"), 0.0033)
UFO = scale_image(pygame.image.load("imgs/Ufo.png"), 0.0033)

# Import User Interface Images
UIBACKGROUND = scale_image(pygame.image.load("imgs/UI BG.png"), 0.1038)

MAINMENU = scale_image(pygame.image.load("imgs/MainMenuScreen.png"),0.13)

PLAY_BUTTON = scale_image(pygame.image.load("imgs/PlayButton.png"), 0.019)
QUIT_BUTTON = scale_image(pygame.image.load("imgs/QuitButton.png"), 0.019)
VOLONBUTTON = scale_image(pygame.image.load("imgs/VolumeOnButton.png"), 0.019)
VOLOFFBUTTON = scale_image(pygame.image.load("imgs/VolumeOffButton.png"), 0.019)

# Import Fonts
UI_FONT = pygame.font.Font("fonts/PixelifySans-SemiBold.ttf", 36)

# -- ANIMATIONS --

# -- SOUNDS --

CLICK_SOUND = pygame.mixer.Sound("sounds/blipSelect.wav")
CLICK_SOUND.set_volume(0.5)

WIN = pygame.display.set_mode((1280,1024))
pygame.display.set_caption("2Delivery")

# ------------------- MAIN CODE -------------------

# --- CAR STATS ---

carNames=[]
carAccelerations = []
carMaxSpeeds=[]
carCapacity = []
CarDeliveryMultiplier = []
carPrices = []

csv_file = open('CarStats.csv','r') 
for line in csv_file:                  
    name,accell,speed,capacity,multiplier,price=line[:-1].split(',')  
    carNames.append(name)
    carAccelerations.append(float(accell))
    carMaxSpeeds.append(float(speed))
    carCapacity.append(int(capacity))
    CarDeliveryMultiplier.append(float(multiplier))
    carPrices.append(int(price))
csv_file.close()                       

print(carNames)
print(carAccelerations)
print(carMaxSpeeds)
print(carCapacity)
print(CarDeliveryMultiplier)
print(carPrices)

# Volume
volumeBool = True

# -- TEMP CODE --
carSelection = VAN

# -- CLASSES --

class GameInfo:
    def __init__(self):
        self.started = False
    
    def start_game(self):
        self.started = True

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def drawButton(self):
        WIN.blit(self.image, (self.rect.x, self.rect.y))

    def clickButton(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                if self.rect.collidepoint(event.pos):
                    CLICK_SOUND.play()
                    return True
        return False


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

    # Collision handler
    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi

    # gradually slowing down after no button presses
    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

class playerCar(AbstractCar):   
    IMG = carSelection
    START_POS = (648, 680)

    def bounce(self):
        self.vel = -self.vel
        self.move()

def draw(win, images, player_car):
    for img,pos in images:
        win.blit(img, pos)

    player_car.draw(win)

def drawMenu(win, menuImages):
    for img,pos in menuImages:
        win.blit(img, pos)

# -- CLOCK -- 

FPS = 60
clock = pygame.time.Clock()

# -- IMAGES --

images = [(UIBACKGROUND, (244.5,0)), (MAP, (0,0))] 

menuImages = [(MAINMENU, (0,0))]

# -- PLAYER CAR --

player_car = playerCar(1.5,2)
gameInfo = GameInfo()

# --- BUTTONS ---
quit_Button = Button(1048, 875, QUIT_BUTTON)
volumeOnButton = Button(1048, 765, VOLONBUTTON)
volumeOffButton = Button(1048, 765, VOLOFFBUTTON)

play_button = Button(575, 627, PLAY_BUTTON)
volumeOnButtonMenu = Button(1070, 20, VOLONBUTTON)
volumeOffButtonMenu = Button(1070, 20, VOLOFFBUTTON)
quit_button_menu = Button(1070,895, QUIT_BUTTON)

# -- EVENT LOOP --
run = True

while run:

    # set clock speed
    clock.tick(FPS)

    # Update key state once per frame
    keys = pygame.key.get_pressed()
    events = pygame.event.get()  # Fetch all events once per frame

    # Handle quitting events
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    # Main menu handling
    if not gameInfo.started:
        drawMenu(WIN, menuImages)

        quit_button_menu.drawButton()
        if quit_button_menu.clickButton(events):
            pygame.time.wait(250)
            run = False
            break

        play_button.drawButton()
        if volumeBool:
            volumeOnButtonMenu.drawButton()
        else:
            volumeOffButtonMenu.drawButton()
        pygame.display.update()
        
        if not pygame.mixer.music.get_busy() and volumeBool:
            pygame.mixer.music.load("sounds/Menu Music.mp3")
            pygame.mixer.music.play(-1, 0.0)

        # Check if play button is clicked
        if play_button.clickButton(events):
            gameInfo.start_game()
            if volumeBool:
                pygame.mixer.music.stop()  # Stop menu music before starting game music
                pygame.mixer.music.load("sounds/Game Music.mp3")
                pygame.mixer.music.play(-1, 0.0)
            else:
                # If music is muted, load the game music but keep it paused
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/Game Music.mp3")
                pygame.mixer.music.play(-1, 0.0)
                pygame.mixer.music.pause()

        # Volume button handling
        if volumeBool and volumeOnButtonMenu.clickButton(events):
            volumeBool = False
            pygame.mixer.music.pause()
        elif not volumeBool and volumeOffButtonMenu.clickButton(events):
            volumeBool = True
            pygame.mixer.music.unpause()

        continue  # Skip game logic while in the menu

    # Game logic begins after start
    moved = False

    # W Keybind
    if keys[pygame.K_w]:
        player_car.move_forward()
        moved = True

    # S Keybind
    if keys[pygame.K_s]:
        player_car.move_backward()
        moved 

    # A Keybind
    if keys[pygame.K_a] and player_car.vel != 0:
        player_car.rotate(left=True)

    # D Keybind
    if keys[pygame.K_d] and player_car.vel != 0:
        player_car.rotate(right=True)

    # Gradually slowing stop for player car
    if not moved:
        player_car.reduce_speed()

    # Check for collisions 
    if player_car.collide(MAP_COLLISIONS_MASK) is not None:
        player_car.bounce()

    # Redraw screen
    draw(WIN, images, player_car)
    quit_Button.drawButton()

    # Quit button handling
    if quit_Button.clickButton(events):
        pygame.time.wait(250)
        run = False
        break

    # --- VOLUME MANAGEMENT CODE ---
    if volumeBool:
        volumeOnButton.drawButton()
        if volumeOnButton.clickButton(events):
            volumeBool = False
            pygame.mixer.music.pause()
    else:
        volumeOffButton.drawButton()
        if volumeOffButton.clickButton(events):
            volumeBool = True
            pygame.mixer.music.unpause()

    # Redraw Text
    coinsText = UI_FONT.render('xxxx', False, (0, 0, 0))
    WIN.blit(coinsText, (1120, 130))
    parcelsText = UI_FONT.render('x/x', False, (0, 0, 0))
    WIN.blit(parcelsText, (1120, 242))
    deliveryLocationText = UI_FONT.render('xx', False, (0, 0, 0))
    WIN.blit(deliveryLocationText, (1120, 357))
    speedText = UI_FONT.render('xx mph', False, (0, 0, 0))
    WIN.blit(speedText, (1120, 470))

    # Update display
    pygame.display.update()

pygame.quit()