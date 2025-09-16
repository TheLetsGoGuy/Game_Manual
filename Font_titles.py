import pygame

#initialize PyGame
pygame.init()

#Set the dimensions of the windows
window = pygame.display.set_mode((800, 600))

#Set the title of the window
pygame.display.set_caption('Basic PyGame Window')

#Set up the font and size
font = pygame.font.Font(None, 74)

#Render the text
text = font.render('Hello, Pygame!', True, (255,255,255))

#Main loop to keep the window open
running = True
while running:
    #Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Fill the screen with a color
    window.fill((0,0,0))
    
    #Display the text
    window.blit(text,(250,250))
    
    #Update the screen
    pygame.display.update()

#Quit Pygame    
pygame.quit()