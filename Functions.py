import pygame


#--- Image Scale Function ---

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


#--- Image Rotate Function ---

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

# --- Draw Text Sub-Program ---

def drawText(win, text, font, colour, x, y):
    text_surface = font.render(str(text), True, colour)  # Use `True` for antialiasing
    win.blit(text_surface, (x, y))