import pygame


#------------------- IMAGE SCALE FUNCTION -------------------

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


#------------------- IMAGE ROTATE FUNCTION -------------------

def blit_rotate_centre(win, image, top_left, angle):
    # Rotate the image
    rotated_image = pygame.transform.rotate(image, angle)
    
    # Calculate the new rect's center based on the original image's center
    original_rect = image.get_rect(topleft=top_left)
    new_rect = rotated_image.get_rect(center=original_rect.center)
    
    # Draw the rotated image
    if win:
        win.blit(rotated_image, new_rect.topleft)
    
    return rotated_image, new_rect