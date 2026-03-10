import pygame
import sys

#initialize PyGame
pygame.init()

#Set the dimensions of the windows
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))

#Set the title of the window
pygame.display.set_caption('Rectangle Movement')

#Color
WHITE = (255,255,255)
BLUE = (0,0,255)

#player setting
player_width = 40
player_height = 40

#Start player at the center
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT // 2 - player_height // 2

speed = 5

clock = pygame.time.Clock()

#Game Loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #Get pressed keys
    keys = pygame.key.get_pressed()
    
    #movement control
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed
        
    #Screen Boundaries
    if player_x <= 0:
        player_x = 0
    if player_x >= WIDTH - player_width:
        player_x = WIDTH - player_width
    if player_y <= 0:
        player_y = 0
    if player_y >= HEIGHT - player_height:
        player_y = HEIGHT - player_height
        
    #Clear screen
    window.fill(WHITE)
    
    #Draw player rectangle
    pygame.draw.rect(window,BLUE,(player_x,player_y,player_width,player_height))
    
    #Update display
    pygame.display.update()
    
    #Control Frame Rate
    clock.tick(60)
    
#Quit Pygame
pygame.quit()
sys.exit()