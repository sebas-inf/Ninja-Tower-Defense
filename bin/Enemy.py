import pygame
from math import sqrt

class Enemy:
    def __init__(self, level, x, y, vx, vy, grid_size):
        self.__health = level
        self.__speed = level * 2
        self.__x = x
        self.__y = y
        self.__vx = vx
        self.__vy = vy
        self.__size = grid_size
        
        self.__image = pygame.image.load("assets/Actor/Monsters/Mouse/SpriteSheet.png")

    
    def __move__(self):
        self.__x += self.__vx * self.__speed
        self.__y += self.__vy * self.__speed
    
    def __draw__(self):
        pass