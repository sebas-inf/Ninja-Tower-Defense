import pygame
pygame.init()
import math

class FriendT:
    def __init__(self, damage, fireRate, range, projectiles, hitType, towerID, tier, cost):
        self.__damage = damage
        self.__fireRate = fireRate
        self.__range = range
        self.__projectiles = projectiles
        self.__hitType = hitType
        self.__towerID = towerID
        self.__tier = tier
        self.__cost = cost
        self.__x = 0
        self.__y = 0
        self.__placeMode = True
        self.__canShoot = True

    def __move__(self, x ,y):
        self.__x = x
        self.__y = y

    

