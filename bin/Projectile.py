import pygame
import json

# loads in settings data from bin\settings.json and stores the information to their respective variables
# note: json files store all information as strings. make sure to convert any non-string type variables to their respective type (EX: screen_width = int(settings["screen_width"]))
with open("bin/settings.json") as file:
    settings = json.load(file)
screen_width = int(settings["screen_width"])
screen_height = int(settings["screen_height"])

play_area_width = (screen_width / 28) * 16
play_area_height = (screen_height / 21) * 12
grid_size = screen_width / 28

class Projectile:
    def __init__(self, start_x, start_y, dx, dy, speed):
        self.__dx = dx
        self.__dy = dy
        self.__x = start_x
        self.__y = start_y
        self.__speed = speed


    # description:  moves x and y position of the projectile and then checks to see if it went out of bounds. ifso it removes itself
    # parameters:   list of projectiles from parent Tower
    # return:       none
    def __update__(self, projectiles):
        self.__x += self.__dx * self.__speed
        self.__y += self.__dy * self.__speed
        if (self.__x < -grid_size or self.__x > play_area_width + grid_size or self.__y < ((play_area_height / 12) * 9 - grid_size) or self.__y > play_area_height + grid_size):
            projectiles.pop(self)


    def __draw__(self):
        pass