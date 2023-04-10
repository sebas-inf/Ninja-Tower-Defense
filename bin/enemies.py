import pygame
from math import sqrt

class Enemies:
    def __init__(self, level, x, y, vx, vy):
        self.__health = level
        self.__speed = level * 2
        self.__x = x
        self.__y = y
        self.__vx = vx
        self.__vy = vy
    