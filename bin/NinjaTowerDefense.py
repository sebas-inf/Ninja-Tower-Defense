import pygame
from Friend import FriendT
pygame.init()


display_width, display_height = 896,672 # this is a 4:3 aspect ratio, and both the width and the height are divisible by 16 (the map grid is in 16x16 tiles)
screen = pygame.display.set_mode((display_width, display_height))
font = pygame.font.Font("assets/HUD/Font/NormalFont.ttf",48)
pygame.display.set_caption("NinjaTD") #Window Name
icon = pygame.image.load("assets/MusicCover.png")
pygame.display.set_icon(icon) #Favicon



def play(map_id, difficulty = 1):
    pass

def map_select():
    pass

#Displays losing message
def lost():
    button_width = 200
    button_height = 100
    button_surface = pygame.Surface((button_width, button_height))
    button_surface.fill((122,45,48))
    text = font.render("You Lost", True, (255,255,255))
    text_rect = text.get_rect(center = (button_width // 2, button_height // 2))
    button_surface.blit(text, text_rect)

#Displays winning message
def won():
    button_width = 200
    button_height = 100
    button_surface = pygame.Surface((button_width, button_height))
    button_surface.fill((65,135,145))
    text = font.render("You Won", True, (255,255,255))
    text_rect = text.get_rect(center = (button_width // 2, button_height // 2))
    button_surface.blit(text, text_rect)

#Starts a new game
def new_game():
    button_width = 200
    button_height = 100
    button_surface = pygame.Surface((button_width, button_height))
    button_surface.fill((65,135,145))
    text = font.render("Start a New Game?", True, (255,255,255))
    text_rect = text.get_rect(center = (button_width // 2, button_height // 2))
    button_surface.blit(text, text_rect)

#Loads previous saved game
def load():
    button_width = 200
    button_height = 100
    button_surface = pygame.Surface((button_width, button_height))
    button_surface.fill((65,135,145))
    text = font.render("Load Game", True, (255,255,255))
    text_rect = text.get_rect(center = (button_width // 2, button_height // 2))
    button_surface.blit(text, text_rect)

#Ends the game and closes the window
def quit():
    button_width = 200
    button_height = 100
    button_surface = pygame.Surface((button_width, button_height))
    button_surface.fill((65,135,145))
    text = font.render("Quit", True, (255,255,255))
    text_rect = text.get_rect(center = (button_width // 2, button_height // 2))
    button_surface.blit(text, text_rect)

#Saves the current game
def save():
    button_width = 200
    button_height = 100
    button_surface = pygame.Surface((button_width, button_height))
    button_surface.fill((65,135,145))
    text = font.render("Save Game", True, (255,255,255))
    text_rect = text.get_rect(center = (button_width // 2, button_height // 2))
    button_surface.blit(text, text_rect)


#Starting menu
def title_screen():
    button_width = 200
    button_height = 100
    button_surface = pygame.Surface((button_width, button_height))
    button_surface.fill((65,135,145))
    button_rect = button_surface.get_rect(center = (button_width // 2, button_height // 2))
    text = font.render("START", True, (255,255,255))
    text_rect = text.get_rect(center = (button_width // 2, button_height // 2))
    button_surface.blit(text, text_rect)
    button_rect.x = display_width // 2 - button_width // 2
    button_rect.y = display_height // 2 - button_height // 2
    

    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # check for left mouse button click
                if button_rect.collidepoint(event.pos):
                    map_select()

        screen.fill((255,255,255)) # draw background color for menu
        screen.blit(button_surface, button_rect) # draw play button

        pygame.display.flip() #Updates the game screen

title_screen()