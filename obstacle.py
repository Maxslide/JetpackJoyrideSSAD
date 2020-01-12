import numpy as np
        
class verticle:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__arr = np.full((1,15), 2)
    def move(obj):
        if(self.__y > 0):
            unslice = np.full((1,15), 1)
            obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = unslice
            if(len(np.where(obj.arr[self.__x : self.__x - 1 , self.__y + 1 : self.__y + 6] == 0 )[1].tolist()) == 0 ):
                self.__y -= 1
                obj.arr[self.__x : self.__x + 5, self.__y : self.__y + 5] = Hero.heroground(self)
                return 1
            else:
                return -1
        return 0
            
def obstv(self):
    arr = np.full((1,15), 2)
    return arr
def obstvmove(self,obj):
    return
def obsth(self):
    arr = np.full((15,1), 2)
    return arr
def obstd(self):
    arr = np.full((15,15), 1)
    for i in range(15):
        arr[i,i] = 2
    return arr
