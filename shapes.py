import pygame

#initialize PyGame
pygame.init()

#Set the dimensions of the windows
window = pygame.display.set_mode((800, 600))

#Set the title of the window
pygame.display.set_caption('Basic PyGame Window')

#Main loop to keep the window open
running = True
while running:
    #Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Fill the screen with a color
    window.fill((0,0,0))
    
    #Draw a line
    pygame.draw.line(window,(255,0,0),(0,0),(800,600),5)
    
    #Draw a rectangle
    pygame.draw.rect(window,(0,255,0),(100,100,200,150))
    
    #Draw a circle
    pygame.draw.circle(window,(0,0,255),(400,300),75)
    
    #Update the screen
    pygame.display.update()

#Quit Pygame    
pygame.quit()