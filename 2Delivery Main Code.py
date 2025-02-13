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
MAP = scale_image(pygame.image.load("imgs/MainMap.png"), 0.1005)
MAP_COLLISIONS = scale_image(pygame.image.load("imgs/CollisionMap.png"), 0.1005)
MAP_COLLISIONS_MASK = pygame.mask.from_surface(MAP_COLLISIONS)

# Import veicle images 
MOPED = scale_image(pygame.image.load("imgs/RedMoped.png"), 0.0027)
PICKUP = scale_image(pygame.image.load("imgs/OrangePickup.png"), 0.003)
VAN = scale_image(pygame.image.load("imgs/BlueVan.png"), 0.0031)
LORRY = scale_image(pygame.image.load("imgs/GreenLorry.png"), 0.004)
SPORTSCAR = scale_image(pygame.image.load("imgs/SportsCar.png"), 0.0032)



# Import User Interface Images
UIBACKGROUND = scale_image(pygame.image.load("imgs/UI BG.png"), 0.1038)

MAINMENU = scale_image(pygame.image.load("imgs/MainMenuScreen.png"),0.13)

PLAY_BUTTON = scale_image(pygame.image.load("imgs/PlayButton.png"), 0.019)
QUIT_BUTTON = scale_image(pygame.image.load("imgs/QuitButton.png"), 0.019)
VOLONBUTTON = scale_image(pygame.image.load("imgs/VolumeOnButton.png"), 0.019)
VOLOFFBUTTON = scale_image(pygame.image.load("imgs/VolumeOffButton.png"), 0.019)

CARSHOPUI = scale_image(pygame.image.load("imgs/carShopUI.png"), 0.085)
BUYBUTTON = scale_image(pygame.image.load("imgs/buyButton.png"), 0.03)
GREYBUYBUTTON  = scale_image(pygame.image.load("imgs/GreyBuyButton.png"), 0.03)

WAREHOUSEUI = scale_image(pygame.image.load("imgs/WarehouseUI.png"), 0.085)
PARCELBUTTON = scale_image(pygame.image.load("imgs/WarehouseParcelButton.png"), 0.04)

UIEXITBUTTON = scale_image(pygame.image.load("imgs/MenuExitButton.png"), 0.008)
MAPBUTTON = scale_image(pygame.image.load("imgs/MapButton.png"), 0.019)
MAPUI = scale_image(pygame.image.load("imgs/LocationMap.png"), 0.85)

HELPBUTTON = scale_image(pygame.image.load("imgs/HelpButton.png"), 0.019)
HELPUI = scale_image(pygame.image.load("imgs/helpUI.png"), 0.85)

# --- DELIVERY COLLISION MASKS ---

CARSHOPCOLLISION = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/CarShopCollision.png"), 1.005))

WAREHOUSECOLLISION = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/WarehouseCollision.png"), 1.005))

# Apartments
A1 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/A1Collision.png"), 1.005))
A2 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/A2Collision.png"), 1.005))
A3 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/A3Collision.png"), 1.005))
A4 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/A4Collision.png"), 1.005))
A5 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/A5Collision.png"), 1.005))

# Cabins
C1 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/C1Collision.png"), 1.005))
C2 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/C2Collision.png"), 1.005))
C3 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/C3Collision.png"), 1.005))

# Houses
H1 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/H1Collision.png"), 1.005))
H2 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/H2Collision.png"), 1.005))
H3 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/H3Collision.png"), 1.005))
H4 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/H4Collision.png"), 1.005))
H5 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/H5Collision.png"), 1.005))
H6 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/H6Collision.png"), 1.005))
H7 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/H7Collision.png"), 1.005))
H8 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/H8Collision.png"), 1.005))
H9 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/H9Collision.png"), 1.005))
H10 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/H10Collision.png"), 1.005))
H11 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/H11Collision.png"), 1.005))
H12 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/H12Collision.png"), 1.005))
H13 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/H13Collision.png"), 1.005))
H14 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/H14Collision.png"), 1.005))

# Modern Houses
M1 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/M1Collision.png"), 1.005))
M2 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/M2Collision.png"), 1.005))
M3 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/M3Collision.png"), 1.005))
M4 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/M4Collision.png"), 1.005))
M5 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/M5Collision.png"), 1.005))
M6 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/M6Collision.png"), 1.005))
M7 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/M7Collision.png"), 1.005))
M8 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/M8Collision.png"), 1.005))
M9 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/M9Collision.png"), 1.005))
M10 = pygame.mask.from_surface(scale_image(pygame.image.load("DeliveryColissions/M10Collision.png"), 1.005))


# Import Fonts
FONTFILENAME = "fonts/RasterForgeRegular.ttf"
UI_FONT = pygame.font.Font(FONTFILENAME , 32)
SPEED_UI_FONT = pygame.font.Font(FONTFILENAME , 22)
SMALL_UI_FONT = pygame.font.Font(FONTFILENAME, 14)
LARGE_UI_FONT = pygame.font.Font(FONTFILENAME, 70)
STATS_UI_FONT = pygame.font.Font(FONTFILENAME, 27)
PRICE_UI_FONT = pygame.font.Font(FONTFILENAME, 55)
# -- ANIMATIONS --

# -- SOUNDS --

CLICK_SOUND = pygame.mixer.Sound("sounds/blipSelect.wav")
ERROR_SOUND = pygame.mixer.Sound("sounds/ErrorSound.mp3")
COIN_GAIN_SOUND = pygame.mixer.Sound("sounds/CoinGainSound.mp3")
COIN_SPEND_SOUND = pygame.mixer.Sound("sounds/CoinSpendSound.wav")
DRIVING_SOUND = pygame.mixer.Sound("sounds/carDrivingSound.mp3")

CLICK_SOUND.set_volume(0.5)
DRIVING_SOUND.set_volume(0.2)


# --- UI GREY TRANSPARENT BG ---
TRANSPARENT_GREY = pygame.Surface((1280, 1024), pygame.SRCALPHA)
TRANSPARENT_GREY.fill((33, 33, 33, 170))  # Grey with 50% transparency

WIN = pygame.display.set_mode((1280,1024))
pygame.display.set_caption("2Delivery")

# ------------------- MAIN CODE -------------------

# --- CAR STATS ---

carNames=[]
carMaxSpeeds=[]
carCapacity = []
CarDeliveryMultiplier = []
carPrices = []
carAccelerations = []
carRotations = []

carNumber = 0

csv_file = open('CarStats.csv','r') 
for line in csv_file:                  
    name,speed,capacity,multiplier,price,accelerations,rotations=line[:-1].split(',')  
    carNames.append(name)
    carMaxSpeeds.append(float(speed))
    carCapacity.append(int(capacity))
    CarDeliveryMultiplier.append(float(multiplier))
    carPrices.append(int(price))
    carAccelerations.append(float(accelerations))
    carRotations.append(float(rotations))
csv_file.close()  

carImages = [MOPED, PICKUP, VAN, LORRY, SPORTSCAR]

print(carNames)
print(carMaxSpeeds)
print(carCapacity)
print(CarDeliveryMultiplier)
print(carPrices)

# --- COINS SYSTEM --- 

startingCoins = 5000

playerCoins = startingCoins

# Volume
volumeBool = True

carImage = carImages[0]


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
    def __init__(self, max_vel, rotation_vel, start_pos, acceleration):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = start_pos 
        self.acceleration = acceleration
        self.mask = pygame.mask.from_surface(self.img)  # Original mask

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

    def get_rotated_mask(self):
        # Rotate the image and get the new rect
        rotated_image, new_rect = blit_rotate_centre(None, self.img, (self.x, self.y), self.angle)
    
        # Create a mask from the rotated image
        return pygame.mask.from_surface(rotated_image), new_rect.topleft

    def collide(self, mask, x=0, y=0):
        car_mask, mask_pos = self.get_rotated_mask()
        offset = (int(mask_pos[0] - x), int(mask_pos[1] - y))
        poi = mask.overlap(car_mask, offset)
        return poi

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

class playerCar(AbstractCar):
    def __init__(self, max_vel, rotation_vel, car_image, acceleration):
        self.IMG = car_image  # Set the car image dynamically
        self.START_POS = (648, 720)  # Define the starting position
        #self.START_POS = (80, 80) # TESTING

        super().__init__(max_vel, rotation_vel, self.START_POS, acceleration)  # Pass START_POS to the parent class

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

def get_current_delivery_location(player_car):
    delivery_collisions = {
        "CS": CARSHOPCOLLISION,
        "WH": WAREHOUSECOLLISION,
        "A1": A1, "A2": A2, "A3": A3, "A4": A4, "A5": A5,
        "C1": C1, "C2": C2, "C3": C3,
        "H1": H1, "H2": H2, "H3": H3, "H4": H4, "H5": H5, "H6": H6, "H7": H7, "H8": H8, "H9": H9, "H10": H10, "H11": H11, "H12": H12, "H13": H13, "H14": H14,
        "M1": M1, "M2": M2, "M3": M3, "M4": M4, "M5": M5, "M6": M6, "M7": M7, "M8": M8, "M9": M9, "M10": M10
    }

    for location_name, mask in delivery_collisions.items():
        if player_car.collide(mask) is not None:
            return location_name  # Return the collision file name if a collision is detected

    return None  # Return None if no collision is found

# Warehouse - Give parcels button function
def giveParcels(capacity):
    deliveryLocations = ["A1", "A2", "A3", "A4", "A5", # Apartments
                        "C1", "C2", "C3", # Cabins
                        "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14", # Houses
                        "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10" # Modern Houses
                        ]

    currentParcels = [""] * capacity

    for x in range(capacity):
        # Generate a random index within the range of deliveryLocations
        random_index = random.randint(0, len(deliveryLocations) - 1)
        
        # Assign the randomly selected location to the currentParcels list
        currentParcels[x] = deliveryLocations[random_index]
    
    return currentParcels

# Pay player after delivery function
def payPlayer(playerMoney, deliveryLocation, carMultiplier):

    randomNum = random.randint(75,100) # Create random payout number between 75-100

    moneyGain = 0
    
    if deliveryLocation[0:1] == "H":
        moneyGain = randomNum*carMultiplier
        playerMoney += moneyGain
    elif deliveryLocation[0:1] == "M":
        moneyGain = (2*randomNum)*carMultiplier
        playerMoney += moneyGain
    elif deliveryLocation[0:1] == "A":
        moneyGain = (2.5*randomNum)*carMultiplier
        playerMoney += moneyGain
    else:
        moneyGain = (1.5*randomNum)*carMultiplier
        playerMoney += moneyGain

    global coin_gain_text, coin_gain_time
    coin_gain_text = str(int(moneyGain))
    coin_gain_time = pygame.time.get_ticks()
    
    return playerMoney, moneyGain

# -- CLOCK -- 

FPS = 60
clock = pygame.time.Clock()

# -- IMAGES --

images = [(UIBACKGROUND, (244.5,0)), (MAP, (0,0))] 

menuImages = [(MAINMENU, (0,0))]

# -- PLAYER CAR --

player_car = playerCar(carMaxSpeeds[carNumber], carRotations[carNumber], carImages[carNumber], carAccelerations[carNumber])
gameInfo = GameInfo()


# --- BUTTONS ---
# menu buttons
quit_Button = Button(1048, 880, QUIT_BUTTON)
volumeOnButton = Button(1048, 780, VOLONBUTTON)
volumeOffButton = Button(1048, 780, VOLOFFBUTTON)
mapButton = Button(1048, 680, MAPBUTTON)
helpButton = Button(1048, 580, HELPBUTTON)

# menu buttons
play_button = Button(575, 627, PLAY_BUTTON)
volumeOnButtonMenu = Button(1070, 20, VOLONBUTTON)
volumeOffButtonMenu = Button(1070, 20, VOLOFFBUTTON)
quit_button_menu = Button(1070,895, QUIT_BUTTON)
menuHelpButton = Button(1070, 130, HELPBUTTON)

# ui quit buttons
uiQuitButton = Button(860, 200, UIEXITBUTTON)
ButtonUIQuitButton = Button(865, 55, UIEXITBUTTON)
menuHelpQuitButton = Button(965, 55, UIEXITBUTTON)

# car shop buttons
carShopQuitButton = Button(860, 200, UIEXITBUTTON)
BuyButton = Button(500, 585, BUYBUTTON)
GreyDrawButton = Button(500, 585, GREYBUYBUTTON)

#warehouse buttons
warehouseQuitButton = Button(860, 200, UIEXITBUTTON)
parcelButton = Button(300, 400, PARCELBUTTON)


# Variables
run = True

car_shop_exited = False  # Track if the player has exited the Car Shop UI
warehouse_exited = False # Track if the player has exited the Warehouse UI
exit_time = 0  # Timestamp when the player exited
cooldown_duration = 2000  # cooldown duration for driving actuated ui elements
map_cooldown_duration = 1000 # cooldown duration for map ui

currentParcels = []

map_ui_open = False
map_ui_open_temp = False
tempMapSound = False
help_ui_open = False
menuHelpButtonOpen = False
car_ui_open = False
wh_ui_open = False

is_driving_sound_playing = False

coin_gain_time = 0
coin_gain_duration = 2500
coin_gain_text = ""





# ------------ EVENT LOOP ---------------
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

        # Menu quit button
        quit_button_menu.drawButton()
        if quit_button_menu.clickButton(events):
            pygame.time.wait(250)
            run = False
            break
        
        # Menu play button
        play_button.drawButton()


        if volumeBool:
            volumeOnButtonMenu.drawButton()
        else:
            volumeOffButtonMenu.drawButton()

        # Handle menu help button click
        menuHelpButton.drawButton()
        if menuHelpButton.clickButton(events):
            menuHelpButtonOpen = not menuHelpButtonOpen
        
        if menuHelpButtonOpen:
            WIN.blit(HELPUI, (175, 75))  # Draw the help UI
            menuHelpQuitButton.drawButton()

            # Handle quit button click for the help UI
            if menuHelpQuitButton.clickButton(events):
                menuHelpButtonOpen = False  # Close the help UI

        

        # Menu Music
        if not pygame.mixer.music.get_busy() and volumeBool:
            pygame.mixer.music.load("sounds/Menu Music.mp3")
            pygame.mixer.music.play(-1, 0.0)

        # Check if play button is clicked
        if play_button.clickButton(events) or keys[pygame.K_SPACE]:

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
        
        # Update Menu ONCE every frame
        pygame.display.update()

        continue  # Skip game logic while in the menu

    current_location = get_current_delivery_location(player_car)

    # Game logic begins after start
    moved = False

    # W Keybind
    if keys[pygame.K_w]:
        player_car.move_forward()
        moved = True
        if not is_driving_sound_playing:
            DRIVING_SOUND.play(-1)  # Loop the driving sound
            is_driving_sound_playing = True

    # S Keybind
    if keys[pygame.K_s]:
        player_car.move_backward()
        moved = True
        if not is_driving_sound_playing:
            DRIVING_SOUND.play(-1)  # Loop the driving sound
            is_driving_sound_playing = True

    # A Keybind
    if keys[pygame.K_a] and player_car.vel != 0:
        player_car.rotate(left=True)

    # D Keybind
    if keys[pygame.K_d] and player_car.vel != 0:
        player_car.rotate(right=True)

    # Gradually slowing stop for player car
    if not moved:
        player_car.reduce_speed()
        if is_driving_sound_playing:
            DRIVING_SOUND.stop()
            is_driving_sound_playing = False

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

    # --- DRAW BUTTONS ---
    helpButton.drawButton()
    mapButton.drawButton()

    # --- UI GREY BG ---
    if map_ui_open or map_ui_open_temp or help_ui_open or car_ui_open or wh_ui_open:
        WIN.blit(TRANSPARENT_GREY, (0, 0))  # Draw the transparent grey surface

    # --- MAP BUTTON ---

    # Handle Q key for temporary map UI
    if keys[pygame.K_q]:
        map_ui_open_temp = True  # Temporary map UI when Q is held down
        if not tempMapSound:
            CLICK_SOUND.play()
        tempMapSound = True
    else:
        map_ui_open_temp = False  # Close temporary map UI when Q is released
        tempMapSound = False

    # Handle map button click
    if mapButton.clickButton(events):
        map_ui_open = not map_ui_open  # Toggle map UI state

    map_ui_display = map_ui_open or map_ui_open_temp

    # Draw the map UI if it should be displayed
    if map_ui_display:
        WIN.blit(MAPUI, (75, 75))  # Draw the map UI
        ButtonUIQuitButton.drawButton()

        # Handle quit button click for the map UI
        if ButtonUIQuitButton.clickButton(events):
            map_ui_open = False  # Close the map UI

    # --- HELP BUTTON ---
    
    if helpButton.clickButton(events):  # Check if the map button is clicked
        help_ui_open = not help_ui_open  # Toggle the map UI state

    if help_ui_open:  # Only draw the map UI if it's open
        WIN.blit(HELPUI, (75, 75))  # Draw the map UI
        ButtonUIQuitButton.drawButton()

        # Quit button for map UI
        if ButtonUIQuitButton.clickButton(events):
            help_ui_open = False  # Close the map UI


    # Redraw Text
    coinsText = UI_FONT.render(str(int(playerCoins)), False, (0, 0, 0))
    WIN.blit(coinsText, (1120, 140))

    parcelsText = UI_FONT.render(str((len(currentParcels))) + " / " + str(carCapacity[carNumber]), False, (0, 0, 0))
    WIN.blit(parcelsText, (1120, 255))

    if currentParcels:
        deliveryLocationText = UI_FONT.render(currentParcels[0], False, (0, 0, 0))
    else:
        deliveryLocationText = UI_FONT.render("N/A", False, (0, 0, 0))

    WIN.blit(deliveryLocationText, (1120, 382))  # Always display the text

    nextDeliveryLocationText1 = SMALL_UI_FONT.render("Next Delivery", False, (0, 0, 0))
    WIN.blit(nextDeliveryLocationText1, (1120, 360))
    
    nextDeliveryLocationText2 = SMALL_UI_FONT.render("Location:", False, (0, 0, 0))
    WIN.blit(nextDeliveryLocationText2, (1120, 370))

    speedText = SPEED_UI_FONT.render(str(int(round(player_car.vel*20))) + "px/s", False, (0, 0, 0))
    WIN.blit(speedText, (1120, 485))

    # --- WAREHOUSE ---
    if current_location == "WH" and not warehouse_exited:
        print("Rendering Warehouse UI")  # Debug statement
        WIN.blit(WAREHOUSEUI, (75, 225))  # Draw the warehouse UI
        warehouseQuitButton.drawButton()  # Draw the quit button
        parcelButton.drawButton()  # Draw the parcel button
        wh_ui_open = True

        # Handle quit button click
        if warehouseQuitButton.clickButton(events):
            current_location = None
            warehouse_exited = True
            exit_time = pygame.time.get_ticks()

        # Handle parcel button click
        if parcelButton.clickButton(events):
            currentParcels = giveParcels(carCapacity[carNumber])
            print(f"Parcels Assigned: {currentParcels}")
            warehouse_exited = True
    else:
        wh_ui_open = False

    # Reset warehouse_exited after cooldown
    if warehouse_exited and current_location != "WH":
        current_time = pygame.time.get_ticks()
        if current_time - exit_time >= cooldown_duration:
            warehouse_exited = False
   

    # --- CAR SHOP ---
    if current_location == "CS" and not car_shop_exited:
        WIN.blit(CARSHOPUI, (75, 225))
        carShopQuitButton.drawButton()
        car_ui_open = True

        # Ensure carNumber is within the valid range
        if carNumber < len(carPrices) - 1:  # Check if there is a next car to buy
            next_car_price = carPrices[carNumber + 1]  # Get the price of the next car

            price_text = PRICE_UI_FONT.render(str(next_car_price), False, (0, 0, 0))

            speedStatsText = STATS_UI_FONT.render("Max Speed", False, (0, 0, 0))
            speedStatsText2 = UI_FONT.render(str(carMaxSpeeds[carNumber + 1]*20) + "px/s", False, (140, 25, 25))

            capactiyStats = STATS_UI_FONT.render("Capacity", False, (0, 0, 0))
            capacityStats2 = UI_FONT.render(str(carCapacity[carNumber + 1]), False, (140, 25, 25))

            carMultiplierStats = STATS_UI_FONT.render("Multiplier", False, (0, 0, 0))
            carMultiplierStats2 = UI_FONT.render(str(CarDeliveryMultiplier[carNumber + 1]) + "x", False, (140, 25, 25))

            carnameStats = LARGE_UI_FONT.render(str(carNames[carNumber + 1]), False, (0, 0, 0))

            if playerCoins >= next_car_price:
                BuyButton.drawButton()
                if BuyButton.clickButton(events):  # Check if the Buy button is clicked
                    # Store the current car's position
                    current_x, current_y = player_car.x, player_car.y

                    # Deduct the price from player's coins and move to the next car
                    playerCoins -= next_car_price

                    # Change car num
                    carNumber += 1

                    # Play spend sound
                    COIN_SPEND_SOUND.play()

                    # Update the car image
                    carImage = carImages[carNumber]

                    # Create a new player car with the updated stats and image
                    player_car = playerCar(carMaxSpeeds[carNumber], carRotations[carNumber], carImages[carNumber], carAccelerations[carNumber])

                    # Set the new car's position to the stored coordinates
                    player_car.x, player_car.y = current_x, current_y

                    print(f"Purchased {carNames[carNumber]}! Remaining coins: {playerCoins}, carNumber = {carNumber}")

                    car_shop_exited = True
            else:
                GreyDrawButton.drawButton()  # Draw the greyed-out buy button if the player can't afford the car
                if GreyDrawButton.clickButton(events):
                    # Play error sound
                    ERROR_SOUND.play()

        else:
            price_text = PRICE_UI_FONT.render("N/A", False, (0, 0, 0))
            speedStatsText2 = STATS_UI_FONT.render("N/A ", False, (140, 25, 25))
            capacityStats2 = STATS_UI_FONT.render("N/A", False, (140, 25, 25))                      
            carMultiplierStats2 = STATS_UI_FONT.render("N/A", False, (140, 25, 25))
            carnameStats = LARGE_UI_FONT.render("N/A", False, (0, 0, 0))
            WIN.blit((PRICE_UI_FONT.render("No Cars", False, (0, 0, 0))), (480, 580))
            WIN.blit((PRICE_UI_FONT.render("Available To", False, (0, 0, 0))), (400, 640))
            WIN.blit((PRICE_UI_FONT.render("Purchase!", False, (0, 0, 0))), (440, 700))

        # Display Max Speed Stats
        WIN.blit(speedStatsText, (140, 540))
        WIN.blit(speedStatsText2, (140, 560))
        # Display Capacity Stats
        WIN.blit(capactiyStats, (140, 600))
        WIN.blit(capacityStats2, (140, 620))
        # Display Car Multiplier Stats
        WIN.blit(carMultiplierStats, (140, 660))
        WIN.blit(carMultiplierStats2, (140, 680))
        # Display car name
        WIN.blit(carnameStats, (380, 348))
        # Display car price
        WIN.blit(price_text, (575, 467))

        if carShopQuitButton.clickButton(events):
            current_location = None
            car_shop_exited = True
            exit_time = pygame.time.get_ticks()

    else:
        car_ui_open = False

    if car_shop_exited and current_location != "CS":
        current_time = pygame.time.get_ticks()
        if current_time - exit_time >= cooldown_duration:
            car_shop_exited = False 

    # --- DELIVERYS ---
    if currentParcels:  # Check if there are parcels to deliver
        if current_location == currentParcels[0]:  # Check if the player is at the first delivery location
            playerCoins, coinsGain = payPlayer(playerCoins, currentParcels[0], CarDeliveryMultiplier[carNumber])
            currentParcels.pop(0)  # Remove the delivered location from the list
            print("Delivered! Remaining parcels: " + str(currentParcels))
            COIN_GAIN_SOUND.play()

            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - coin_gain_time


    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - coin_gain_time

    if elapsed_time < coin_gain_duration:
        # Calculate transparency (255 is fully opaque, 0 is fully transparent)
        alpha = max(0, 255 - int((elapsed_time / coin_gain_duration) * 255))
    
        # Create a surface for the text
        coin_gain_surface = PRICE_UI_FONT.render("+" + coin_gain_text, True, (20, 240, 80))  # Green text
        coin_gain_surface.set_alpha(alpha)  # Set transparency

        # Draw the text with the adjusted position
        WIN.blit(coin_gain_surface, (1000 - coin_gain_surface.get_width() , 130))
    else:
        # Clear the text after 5 seconds
        coin_gain_text = ""


    # Update display
    pygame.display.update()

pygame.quit()