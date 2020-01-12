from colorama import Fore,Back,Style
import sys
import numpy as np
import os
import time
from input import *
# os.system("mode con cols=200 lines=60")
# np.set_printoptions(threshold=sys.maxsize)

# person = np.array([[1,1,0,1,1],[1,0,0,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,1,1,0]])
# print(Back.RED + Fore.RED)
# i = 0
# while True:
#     arr[40:45,3+i:8+i] = person[:,:]
#     print(chr(27) + "[2J")
#     for i in range(47) : 
#         for j in range(173):
#             if arr[i,j] == 0:
#                 print(Style.RESET_ALL, end="")
#                 print(Back.BLACK + Fore.BLACK, end="")
#                 print(arr[i,j], end ="")
#                 print(Style.RESET_ALL, end="")
#                 print(Back.RED + Fore.RED, end="")
#             else:
#                 print(arr[i,j], end ="")
#         print()arr = np.full((47, 10000),1)
#     arr = np.full((47, 10000),1)
#     i += 1
#     time.sleep(1)
class test:
    def __init__(self):
        self.arr = np.full((10,10), 0)
        
    def printarr(self):
        print(self.arr)
class abc:
    def abc(self):
        print("bhaalu chutiya hai")
        
obj1 = abc()
obj1.abc()
def change(obj):
    obj.arr[0,0] = 1
obj = test()
obj.printarr()
change(obj)
obj.printarr()


# print(arr[:30, :50])
