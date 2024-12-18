import pygame


#------------------- IMAGE SCALE FUNCTION -------------------

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


#------------------- IMAGE ROTATE FUNCTION -------------------

def blit_rotate_centre(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)

#def draw (win, images):
    #for img in images:
        #win.blit(img, pos)