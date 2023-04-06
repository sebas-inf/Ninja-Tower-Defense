# fire rate is stored in milliseconds
# range is stored in pixel radius
import pygame
from math import sqrt
pygame.init()


class Tower:
    # description:  initializes the variables of the tower (note: automatically puts the tower in place mode)
    # parameters:   dictionary tower_data : stores information about the tower that is dependent upon which kind of tower it is (EX: tower_id, damage, firerate, etc)
    # return:       none
    def __init__(self, tower_data):
        self.__place_mode = True
        self.__time = 0
        self.__x = 0
        self.__y = 0
        self.__proj_damage = int(tower_data["proj_damage"])
        self.__proj_firerate = int(tower_data["proj_firerate"])
        self.__proj_range = int(tower_data["proj_range"])
        self.__proj_speed = float(tower_data["proj_speed"])
        self.__spec_damage = int(tower_data["spec_damage"])
        self.__spec_firerate = int(tower_data["spec_firerate"])
        self.__spec_range = int(tower_data["spec_range"])
        self.__spec_speed = int(tower_data["spec_speed"])
        self.__cost = int(tower_data["cost"])

    # description:  moves the tower to a specified x and y coordinate
    # parameters:   x and y coordinates of the destination
    # return:       none
    def __move__(self, x ,y):
        self.__x = x
        self.__y = y

    # description:  First checks if the current position is a valid placement (EX: not on the track or another tower)
    #               If it is a valid placement, set place_mode to false to 
    # parameters:   
    # return:       
    def __place__(self):
        pass

    # description:  renders the tower on screen (note: does not render the tower's projectiles)
    # parameters:   none
    # return:       none
    def __draw__(self):
        pass

    # description:  fires a projectile
    # parameters:   target x, target y, current game time
    # return 1:     able to fire
    # return 0:     unable to fire
    def __projectile__(self, target_x, target_y, time):
        # checks if enough time has passed to shoot again
        if (time - self.__time < self.__proj_firerate):
            return 0
        
        # checks if tower is in place mode
        if self.__place_mode:
            return 0
        
        # checks if targets inside tower radius
        dx = target_x - self.__x
        dy = target_y - self.__y
        direction_length = sqrt(dx ** 2 + dy ** 2)
        if (direction_length < self.__proj_range):
            return 0
        
        # normalizes the direction vector, updates tower's time, and spawns in projectile
        self.__time = time
        if direction_length != 0:
            dx /= direction_length
            dy /= direction_length
        # spawn projectile here, dependent upon self.__tower_id
        return 1