
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
        # self.__gravity = 
    def heroground(self):
        person = np.array([[1,1,0,1,1],[1,0,0,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,1,1,0]])
        # person = np.full((5,5),0)
        return person
    def herofly(self):
        person = np.array([[1,1,0,1,1],[1,0,0,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,1]])
        # person = np.full((5,5),0)
        return person
    def heroShield(self):
        person = np.array([[1,1,0,1,0],[1,0,0,0,0],[0,1,0,1,0],[1,0,1,0,0],[0,1,0,1,0]])
        return person
    def moveR(self, obj):
        if(self.__y < 181):
            unslice = np.full((5,5),1)
            if(len(np.where(obj.arr[self.__x : self.__x + 5 , self.__y + 1 : self.__y + 6] == 2 )[1].tolist()) == 0  or obj.shield ):
                obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = unslice
                self.__y += 1
                if(obj.shield == False):
                    obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = Hero.heroground(self)
                else:
                    obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = Hero.heroShield(self)
                return 1
            else:
                return -1
        return 0
    def moveL(self, obj):
        if(self.__y > 18):
            unslice = np.full((5,5),1)
            if(len(np.where(obj.arr[self.__x : self.__x + 5 , self.__y - 1 : self.__y + 4] == 2 )[1].tolist()) == 0 or obj.shield ):
                obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = unslice
                self.__y -= 1
                if(obj.shield == False):
                    obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = Hero.heroground(self)
                else:
                    obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = Hero.heroShield(self)
                    
                return 1
            else:
                return -1
        return 0
    def moveU(self, obj):
        if(self.__x > 0):
            unslice = np.full((5,5),1)
            obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = unslice
            if(len(np.where(obj.arr[self.__x -1  : self.__x + 4 , self.__y : self.__y + 5] == 2 )[1].tolist()) == 0 or obj.shield ):
                obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = unslice
                self.__x -= 1
                if(obj.shield == False):
                    obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = Hero.heroground(self)
                else:
                    obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = Hero.heroShield(self)
                    
                return 1
            else:
                return -1
        return 0
    def gravity(self,obj,acc):
        if(self.__x < 34):
            unslice = np.full((5,5),1)
            if(len(np.where(obj.arr[self.__x +1  : self.__x + 6 , self.__y : self.__y + 5] == 2 )[1].tolist()) == 0 or obj.shield):
                obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = unslice

                self.__x += 1
                if(obj.shield == False):
                    obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = Hero.heroground(self)
                else:
                    obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = Hero.heroShield(self)                    
                return acc+1
            else:
                return -1
        return 2
    def get_current_x(self):
        return self.__x
    def get_current_y(self):
        return self.__y
        
            


class Enemy(Person):
    def __init__(self,x,y):
        self.__name = 'Thanos'
        self.__x = x
        self.__y = y
    def enemyarr(self):
        enemy = np.array([[1,1,0,1,1],[1,0,0,0,1],[1,0,0,0,1],[0,0,1,0,0],[0,0,1,0,0]])
        return enemy

        
    