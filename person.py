
import numpy as np
from colorama import Back,Fore,Style
from Background import *
class Person:
    def __init__(self,height,width):
        self.__height = height
        self.__width = width
        
class Hero(Person):
    def __init__(self,height,width):
        super().__init__(height,width)
        self.__name = 'Hulk'
        self.__x = 34
        self.__y = 18
    def heroground(self):
        person = np.array([[1,1,0,1,1],[1,0,0,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,1,1,0]])
        return person
    def herofly(self):
        person = np.array([[1,1,0,1,1],[1,0,0,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,1,0,1]])
        return person
    def moveR(self, obj):
        if(self.__y < 85):
            unslice = np.full((5,5),1)
            obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = unslice
            if(len(np.where(obj.arr[self.__x : self.__x + 5 , self.__y + 1 : self.__y + 6] == 2 )[1].tolist()) == 0 ):
                self.__y += 1
                obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = Hero.heroground(self)
                return 1
            else:
                return -1
        return 0
    def moveL(self, obj):
        if(self.__y > 18):
            unslice = np.full((5,5),1)
            obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = unslice
            if(len(np.where(obj.arr[self.__x : self.__x + 5 , self.__y - 1 : self.__y + 4] == 2 )[1].tolist()) == 0 ):
                self.__y -= 1
                obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = Hero.heroground(self)
                return 1
            else:
                return -1
        return 0
            
        
class Enemy(Person):
    def __init__(self,x,y):
        self.__name = 'Thanos'
        self.__x = x
        self.__y = y
    def enemyarr(self):
        enemy = np.array([[1,1,0,1,1],[1,0,0,0,1],[1,0,0,0,1],[0,0,1,0,0],[0,0,1,0,0]])
        return enemy

        
    