import pygame

#initialize PyGame
pygame.init()

#Set the dimensions of the windows
window = pygame.display.set_mode((800, 600))

# Load an image and create a surface for it
my_image = pygame.image.load("C:/Users/USER/OneDrive/Desktop/TensorFlow/Game/Universe.jpg")
# Scaling the image
scaled_image = pygame.transform.scale(my_image, (50, 50))  # Resize to 50x50 pixels

#Main loop to display surfaces
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Rotating the image
    rotated_image = pygame.transform.rotate(my_image, 45)  # Rotate by 45 degrees
    # Displaying the image
    window.blit(my_image, (100, 100))  # Position the image at (100, 100)
    # Display transformed images
    window.blit(scaled_image, (200, 100))
    window.blit(rotated_image, (300, 100))
    # Make surface semi-transparent
    my_image.set_alpha(128)  # 128 for 50% transparency
    
    #Update the screen
    pygame.display.flip()

#Quit Pygame    
pygame.quit()