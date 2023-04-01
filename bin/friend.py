import pygame
pygame.init()
from math import sqrt

class FriendT:
    def __init__(self, towerID):
        match towerID:
            case 0:
                self.__damage = 1
                self.__fireRate = 1
                self.__range = range
                self.__projectiles = 0
                self.__hitType = 0
                self.__tier = 0
                self.__cost = 300
                self.__x = 0
                self.__y = 0
                self.__placeMode = True
                self.__canShoot = True
            case 1:
                self.__damage = 2
                self.__fireRate = 1
                self.__range = range
                self.__projectiles = 0
                self.__hitType = 0
                self.__tier = 0
                self.__cost = 350
                self.__x = 0
                self.__y = 0
                self.__placeMode = True
                self.__canShoot = True
                
            case 2:
                self.__damage = 2
                self.__fireRate = 1
                self.__range = range
                self.__projectiles = 0
                self.__hitType = 0
                self.__tier = 0
                self.__cost = 400
                self.__x = 0
                self.__y = 0
                self.__placeMode = True
                self.__canShoot = True

            case 3:
                self.__damage = 1
                self.__fireRate = 1
                self.__range = range
                self.__projectiles = 0
                self.__hitType = 0
                self.__tier = 0
                self.__cost = 450
                self.__x = 0
                self.__y = 0
                self.__placeMode = True
                self.__canShoot = True

            case 4:
                self.__damage = 3
                self.__fireRate = 1
                self.__range = range
                self.__projectiles = 0
                self.__hitType = 0
                self.__tier = 0
                self.__cost = 500
                self.__x = 0
                self.__y = 0
                self.__placeMode = True
                self.__canShoot = True

    def __move__(self, x ,y):
        self.__x = x
        self.__y = y

    def __shoot__(self, targetx, targety, time):
        directionX = targetx - self.__x
        directionY = targety - self.__y

        self.__time = time

        directionLength = sqrt(directionX ** 2 + directionY ** 2)

        if directionLength != 0:
            directionX /= directionLength
            directionY /= directionLength

        
    
        
