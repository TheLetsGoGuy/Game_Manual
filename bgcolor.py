import pygame

#initialize Pygame
pygame.init()

#set the window dimensions
screen = pygame.display.set_mode((800,600))

#set background color
background_color = (100,150,200)

#main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #fill the screen with the background color
    screen.fill(background_color)
    
    #Update the screen
    pygame.display.update()
    
#quit pygame
pygame.quit()