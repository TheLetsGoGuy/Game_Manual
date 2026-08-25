import pygame

#initialize PyGame
pygame.init()

#Set the dimensions of the windows
window = pygame.display.set_mode((800, 600))

#Creating an additional surface
my_surface = pygame.Surface((200,200)) #200X200 pixels
my_surface.fill((0, 128, 255)) #Filling surface with a blue color

#Main loop to display surfaces
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Blit (draw) the surface onto the main display surface
    window.fill((255,255,255)) #Clear the screen
    window.blit(my_surface,(300,200)) #Position the surface at (300,200)
    
    #Update the screen
    pygame.display.flip()

#Quit Pygame    
pygame.quit()