import numpy as np
from person import *
from Background import *
from obstacle import *
from colorama import Back,Fore,Style
from Background import *
import sys
class Game :
    def printarr(arr):
        for i in arr:
            for j in i[18:191]:
                if(j == 0):
                    print(Style.RESET_ALL,end="")
                    print(Fore.BLACK + Back.BLACK,end="")
                    print(j,end="")
                    print(Style.RESET_ALL,end="")
                    print(Fore.RED + Back.RED,end="")
                else:
                    print(j, end="")
            print()
        return 1
    def printBack(self,obj):
        skyarr = obj.sky()
        groundarr = obj.ground()
        bodyarr = obj.body()
        print("\033[0;0H", end="")
        print(Fore.BLUE,end="")
        Game.printarr(skyarr)
        print(Style.RESET_ALL,end="")
        print(Fore.RED + Back.RED,end="")
        Game.printarr(bodyarr)
        print(Style.RESET_ALL,end="")
        print(Fore.GREEN,end="")
        Game.printarr(groundarr)
        print(Style.RESET_ALL,end="")
        # print("\033[0;0H", end="")
            
    