import numpy as np
from colorama import Fore,Back,Style
from person import *
class bullet:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__arr = np.full((1,1),5)
        self.__hit = False
    def move(self,obj):
        if(self.__y < 200):
            if(len(np.where(obj.arr[self.__x: self.__x + 1 , self.__y + 1 : self.__y+2] == 2 )[1].tolist()) == 0):
                obj.arr[self.__x,self.__y] = 1
                self.__y += 1
                obj.arr[self.__x,self.__y] = 5
            else:
                return -1                
        else:
            self.__arr = np.full((1,1),1)
            self.__hit = True
        return
    def bullet_hit(self):
        self.__hit = True
    def reset(self,obj):
        obj.arr[self.__x,self.__y] = 1
        return
class topbar:
    def __init__(self):
        self.__score = 0
        self.__coins = 0
        self.__speeedBoost = 0
        self.__Shield = 0
        self.__Shieldactive = False
    def updateShield(self):
        b = !(self.__Shieldactive)
        self.__Shieldactive =  b
    def updateShieldTime(self):
        self.__Shield = 3600
    def updateboost(self):
        if(self.__speeedBoost > 0):
            self.__speeedBoost -= 1
    def assignboost(self):
        self.__speeedBoost = 150
    def updatescore(self):
        self.__score += 1
    def updatecoins(self):
        self.__coins += 1
    def getscore(self):
        return self.__score
    def getcoins(self):
        return self.__coins
    def getboost(self):
        return self.__speeedBoost 

class backgroud:
    
    def __init__(self):
        self.arr = np.full((39,213),1)
        self.shield = False 
    def sky(self):
        arr = np.full((5, 213),'+')
        return arr
    def ground(self):
        arr = np.full((5, 213),'$')
        return arr
    def body(self):
        return self.arr
    
class enemyallotment:
    def __init__(self):
        self.__allot = []
        self.__flag = 0
    def moveall(self,obj,Top,person):
        v = 0
        removelist = []
        resetlist = []
        magnetx = np.where(obj.arr == 4)[0].tolist()
        magnety = np.where(obj.arr == 4)[1].tolist()
        if(len(magnetx) > 0 and self.__flag % 2 == 0):
            if(person.get_current_y() < magnety[1]):
                person.moveR(obj)
            else:
                person.moveL(obj)
            # if(person.get_current_x() > magnetx[1]):
            #     person.moveU(obj)
        for i in self.__allot :
            v = i.move(obj)
            
            if(v == -1):
                if(type(i) == bullet):
                    removelist.append(i)
                    resetlist.append(i)
                elif(obj.shield):
                    removelist.append(i)
                else:
                    return -1
            if v == -2 :
                resetlist.append(i)
                removelist.append(i)
            if(v == 2):
                Top.updatecoins()
                removelist.append(i)
            if(v == 3):
                removelist.append(i)
        for i in resetlist:
            i.reset(obj)
        for i in removelist:
            self.__allot.remove(i)
        self.__flag += 1    
    def addobstacle(self,obj):
        self.__allot.append(obj) 
    
# def printarr(arr):
#     for i in arr:
#         for j in i[18:191]:
#             print(j, end="")
#         print()    
# # code to print the background
# print("\033[0;0H", end="")
# obj = backgroud()
# skyarr = obj.sky()
# groundarr = obj.ground()
# bodyarr = obj.body()
# print(Fore.BLUE,end="")
# printarr(skyarr)
# print(Style.RESET_ALL,end="")
# # print(Fore.RED + Back.RED,end="")
# printarr(bodyarr)
# print(Style.RESET_ALL,end="")
# print(Fore.GREEN,end="")
# printarr(groundarr)
# print(Style.RESET_ALL,end="")
# # print("\033[5;0H This is just to test cursor movement", end="")



 
        