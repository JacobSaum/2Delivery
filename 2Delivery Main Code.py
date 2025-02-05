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
MOPED = scale_image(pygame.image.load("imgs/RedMoped.png"), 0.0027)
PICKUP = scale_image(pygame.image.load("imgs/OrangePickup.png"), 0.0035)
VAN = scale_image(pygame.image.load("imgs/BlueVan.png"), 0.003)
LORRY = scale_image(pygame.image.load("imgs/GreenLorry.png"), 0.004)
UFO = scale_image(pygame.image.load("imgs/Ufo.png"), 0.0025)

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
UI_FONT = pygame.font.Font("fonts/PixelifySans-SemiBold.ttf", 36)
SMALL_UI_FONT = pygame.font.Font("fonts/PixelifySans-SemiBold.ttf", 14)
# -- ANIMATIONS --

# -- SOUNDS --

CLICK_SOUND = pygame.mixer.Sound("sounds/blipSelect.wav")
CLICK_SOUND.set_volume(0.5)
ERROR_SOUND = pygame.mixer.Sound("sounds/ErrorSound.mp3")
COIN_GAIN_SOUND = pygame.mixer.Sound("sounds/CoinGainSound.mp3")
COIN_SPEND_SOUND = pygame.mixer.Sound("sounds/CoinSpendSound.wav")

WIN = pygame.display.set_mode((1280,1024))
pygame.display.set_caption("2Delivery")

# ------------------- MAIN CODE -------------------

# --- CAR STATS ---

carNames=[]
carMaxSpeeds=[]
carCapacity = []
CarDeliveryMultiplier = []
carPrices = []


carNumber = 0

csv_file = open('CarStats.csv','r') 
for line in csv_file:                  
    name,speed,capacity,multiplier,price=line[:-1].split(',')  
    carNames.append(name)
    carMaxSpeeds.append(float(speed))
    carCapacity.append(int(capacity))
    CarDeliveryMultiplier.append(float(multiplier))
    carPrices.append(int(price))
csv_file.close()  

carImages = [MOPED, VAN, PICKUP, LORRY, UFO]

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
    def __init__(self, max_vel, rotation_vel, start_pos):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = start_pos 
        self.acceleration = 0.05

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
    def __init__(self, max_vel, rotation_vel, car_image):
        self.IMG = car_image  # Set the car image dynamically
        self.START_POS = (75, 75)  # Define the starting position
        super().__init__(max_vel, rotation_vel, self.START_POS)  # Pass START_POS to the parent class

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
    deliveryLocations = ["A1", "A2", "A3", "A4", "A5",
                            "C1", "C2", "C3",
                            "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14",
                            "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10"
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
        moneyGain = (randomNum*1.5)*carMultiplier
        playerMoney += moneyGain
    
    return playerMoney, moneyGain

# -- CLOCK -- 

FPS = 60
clock = pygame.time.Clock()

# -- IMAGES --

images = [(UIBACKGROUND, (244.5,0)), (MAP, (0,0))] 

menuImages = [(MAINMENU, (0,0))]

# -- PLAYER CAR --

player_car = playerCar(carMaxSpeeds[carNumber], 2, carImages[carNumber])
gameInfo = GameInfo()

# --- BUTTONS ---
quit_Button = Button(1048, 875, QUIT_BUTTON)
volumeOnButton = Button(1048, 765, VOLONBUTTON)
volumeOffButton = Button(1048, 765, VOLOFFBUTTON)
mapButton = Button(1048,655,MAPBUTTON)

play_button = Button(575, 627, PLAY_BUTTON)
volumeOnButtonMenu = Button(1070, 20, VOLONBUTTON)
volumeOffButtonMenu = Button(1070, 20, VOLOFFBUTTON)
quit_button_menu = Button(1070,895, QUIT_BUTTON)

uiQuitButton = Button(860, 200, UIEXITBUTTON)

mapQuitButton = Button(865, 55, UIEXITBUTTON)

carShopQuitButton = Button(860, 200, UIEXITBUTTON)
BuyButton = Button(500, 585, BUYBUTTON)
GreyDrawButton = Button(500, 585, GREYBUYBUTTON)

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



# -- EVENT LOOP --
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

    current_location = get_current_delivery_location(player_car)

    # Game logic begins after start
    moved = False

    # W Keybind
    if keys[pygame.K_w]:
        player_car.move_forward()
        moved = True

    # S Keybind
    if keys[pygame.K_s]:
        player_car.move_backward()
        moved = True

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
    

    # --- MAP BUTTON ---
    mapButton.drawButton()
    if mapButton.clickButton(events):  # Pass events to check for clicks
        map_ui_open = True  # Open the map UI

    if map_ui_open:  # Only draw the map UI if it's open
        WIN.blit(MAPUI, (75, 75))  # Draw the map UI
        mapQuitButton.drawButton()

        # Quit button for map UI
        if mapQuitButton.clickButton(events):
            map_ui_open = False  # Close the map UI
   


    # --- CAR SHOP ---
    if current_location == "CS" and not car_shop_exited:
        WIN.blit(CARSHOPUI, (75, 225))
        carShopQuitButton.drawButton()

        # Ensure carNumber is within the valid range
        if carNumber < len(carPrices) - 1:  # Check if there is a next car to buy
            next_car_price = carPrices[carNumber + 1]  # Get the price of the next car

            # Display the correct price
            price_text = UI_FONT.render(f"Price: {next_car_price}", False, (0, 0, 0))
            WIN.blit(price_text, (300, 250))  # Adjust the position as needed

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
                    player_car = playerCar(carMaxSpeeds[carNumber], 2, carImages[carNumber])

                    # Set the new car's position to the stored coordinates
                    player_car.x, player_car.y = current_x, current_y

                    print(f"Purchased {carNames[carNumber]}! Remaining coins: {playerCoins}, carNumber = {carNumber}")

                    car_shop_exited = True
            else:
                GreyDrawButton.drawButton()  # Draw the greyed-out buy button if the player can't afford the car
                if GreyDrawButton.clickButton(events):
                    # Play error sound
                    ERROR_SOUND.play()

        if carShopQuitButton.clickButton(events):
            current_location = None
            car_shop_exited = True
            exit_time = pygame.time.get_ticks()

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

        

     # Redraw Text
    coinsText = UI_FONT.render(str(playerCoins), False, (0, 0, 0))
    WIN.blit(coinsText, (1120, 130))

    parcelsText = UI_FONT.render(str((len(currentParcels))) + " / " + str(carCapacity[carNumber]), False, (0, 0, 0))
    WIN.blit(parcelsText, (1120, 242))

    if currentParcels:
        deliveryLocationText = UI_FONT.render(currentParcels[0], False, (0, 0, 0))
    else:
        deliveryLocationText = UI_FONT.render("N/A", False, (0, 0, 0))

    WIN.blit(deliveryLocationText, (1120, 375))  # Always display the text

    nextDeliveryLocationText1 = SMALL_UI_FONT.render("Next Delivery", False, (0, 0, 0))
    WIN.blit(nextDeliveryLocationText1, (1120, 355))
    
    nextDeliveryLocationText2 = SMALL_UI_FONT.render("Location:", False, (0, 0, 0))
    WIN.blit(nextDeliveryLocationText2, (1120, 365))

    speedText = UI_FONT.render(str(round(player_car.vel, 1)) + "px/s", False, (0, 0, 0))
    WIN.blit(speedText, (1120, 470))
        
    # Update display
    pygame.display.update()

pygame.quit()