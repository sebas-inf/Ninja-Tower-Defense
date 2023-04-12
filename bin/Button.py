import pygame

# description:  creates a button object with text that can be drawn on the screen and check for click events
class Button:
    # description:  initializes the button variables
    # parameters:   x and y position (top left corner of button)
    #               width and height
    #               text
    #               button_color and text_color (r, g, b)
    #               font size
    # return:       none
    def __init__(self, x, y, width, height, text, button_color, text_color, font_size):
        self.__rect = pygame.Rect(x, y, width, height)
        self.__text = text
        self.__text_color = text_color
        self.__button_color = button_color
        self.__font_size = font_size
        self.__font = pygame.font.Font("assets/HUD/Font/NormalFont.ttf", self.__font_size)
    

    # description:  renders the button on the screen
    # parameters:   screen surface
    # return:       none
    def draw(self, screen):
        pygame.draw.rect(screen, self.__button_color, self.__rect)
        text_surface = self.__font.render(self.__text, True, self.__text_color)
        text_rect = text_surface.get_rect(center=(self.__rect.center[0], self.__rect.center[1] - 6))
        screen.blit(text_surface, text_rect)


    # description:  checks to see if the user clicked on the button
    # parameters:   mouse position (pygame.mouse.get_pos())
    #               mouse button (pygame.mouse.get_pressed())
    # return:       True if button was clicked
    #               False if button was not clicked
    def is_clicked(self, mouse_pos, mouse_button):
        if self.__rect.collidepoint(mouse_pos) and mouse_button[0]:
            return True
        else:
            return False