import pygame
import json
from friend import Tower
from Button import Button
pygame.init()

# loads in settings data from bin/settings.json and stores the information to their respective variables
# note: json files store all information as strings. make sure to convert any non-string type variables to their respective type (EX: screen_width = int(settings["screen_width"]))
with open("bin/settings.json") as file:
    settings = json.load(file)
screen_width = int(settings["screen_width"])
screen_height = int(settings["screen_height"])

# reads data about towers from bin/towers.json and loads it into all_tower_data
with open("bin/towers.json") as file:
    all_tower_data = json.load(file)


screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.Font("assets/HUD/Font/NormalFont.ttf",48)
pygame.display.set_caption("NinjaTD") #Window Name
icon = pygame.image.load("assets/MusicCover.png")
pygame.display.set_icon(icon) #Favicon

#Starting menu
def title_screen():
    title_font = pygame.font.Font("assets/HUD/Font/NormalFont.ttf", int((screen_width / 28) * 2))
    title_text_surface = title_font.render("Ninja Tower Defense", True, (255, 255, 255))
    title_text_x = (screen_width - title_text_surface.get_size()[0]) // 2
    title_text_y = (screen_height - title_text_surface.get_size()[1]) // 2 - (screen_height / 21 * 5)

    # find the button dimensions based on screen size
    button_width = screen_width / 28 * 8    # screen_width / 28 gives the grid size of the screen
    button_height = screen_height / 21 * 2  # screen_height / 21 also gives the grid size of the screen
    button_gap = screen_width / 28 / 4
    # find font size based on screen size
    font_size = int(screen_width / 28 * 1.5)
    # find the x and y positions of the buttons    
    play_x = screen_width // 2 - button_width - (button_gap / 2)
    play_y = screen_height // 2
    options_x = play_x
    options_y = screen_height // 2 + button_height + button_gap
    quit_x = screen_width // 2 + (button_gap / 2) + (button_width // 3)
    quit_y = options_y
    # create button objects
    play_button = Button(play_x, play_y, (button_width * 2 + button_gap), button_height, "PLAY", (255, 255, 255), (0, 255, 0), font_size)
    options_button = Button(options_x, options_y, (button_width * 4 // 3), button_height, "OPTIONS", (255, 255, 255), (0, 0, 0), font_size)
    quit_button = Button(quit_x, quit_y, (button_width * 2 // 3), button_height, "QUIT", (255, 255, 255), (255, 0, 0), font_size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # render a black background
        screen.fill((0, 0, 0))

        # render the title text
        screen.blit(title_text_surface, (title_text_x, title_text_y))

        # render the buttons
        play_button.draw(screen)
        options_button.draw(screen)
        quit_button.draw(screen)

        # get updated mouse position and mouse button presses
        mouse_pos = pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()

        # check for button clicks
        if play_button.is_clicked(mouse_pos, mouse_button):
            map_select()
        if options_button.is_clicked(mouse_pos, mouse_button):
            options()
        if quit_button.is_clicked(mouse_pos, mouse_button):
            pygame.quit()
            quit()
        
        # update the display
        pygame.display.update()



# description:  
# parameters:   
# return:       
def play(map_id, difficulty = 1):
    # 
    level_data = {}
    match map_id:
        case 0:
            level_data = all_tower_data["one"]


# description:  Loads the map select screen. Has different picture buttons for the levels. When a button is clicked on, the play function is called. The map_id from the play button is sent into the play function.
# parameters:   none
# return:       none
def map_select():
    title_font = pygame.font.Font("assets/HUD/Font/NormalFont.ttf", int((screen_width / 28) * 2))
    title_text_surface = title_font.render("Map Select Screen", True, (150, 83, 64))
    title_text_x = (screen_width - title_text_surface.get_size()[0]) // 2
    title_text_y = (screen_height - title_text_surface.get_size()[1]) // 2 - (screen_height / 21 * 5)

def options():
    print("options screen")
    pygame.quit()
    quit()

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