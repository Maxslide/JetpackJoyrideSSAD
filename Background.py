import numpy as np
from colorama import Fore,Back,Style

class backgroud:
    
    def __init__(self):
        self.arr = np.full((39,213),1) 
    def sky(self):
        arr = np.full((5, 213),'+')
        return arr
    def ground(self):
        arr = np.full((5, 213),'$')
        return arr
    def body(self):
        return self.arr
    
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



 
        