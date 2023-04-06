import pygame
import json
from Friend import Tower

pygame.init()

# loads in settings data from bin\settings.json and stores the information to their respective variables
# note: json files store all information as strings. make sure to convert any non-string type variables to their respective type (EX: screen_width = int(settings["screen_width"]))
with open("bin/settings.json") as file:
    settings = json.load(file)
screen_width = int(settings["screen_width"])
screen_height = int(settings["screen_height"])

# reads data about towers from bin\towers.json and loads it into all_tower_data
with open("bin/towers.json") as file:
    all_tower_data = json.load(file)


screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.Font("assets/HUD/Font/NormalFont.ttf",48)
pygame.display.set_caption("NinjaTD") #Window Name
icon = pygame.image.load("assets/MusicCover.png")
pygame.display.set_icon(icon) #Favicon


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
    button_rect.x = screen_width // 2 - button_width // 2
    button_rect.y = screen_height // 2 - button_height // 2

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


# description:  
# parameters:   
# return:       
def play(map_id, difficulty = 1):
    # 
    level_data = dict()
    match map_id:
        case 0:
            level_data = all_tower_data["one"]


# description:  Loads the map select screen. Has different picture buttons for the levels. When a button is clicked on, the play function is called. The map_id from the play button is sent into the play function.
# parameters:   none
# return:       none
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


title_screen()
pygame.quit()