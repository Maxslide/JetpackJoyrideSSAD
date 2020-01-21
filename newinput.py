import sys 
from os import system
import select 
import tty 
import termios
from termios import tcflush,TCIFLUSH
import time
from game import *
from Background import *
from person import *
from obstacle import *
import random
from util import *
from coins import *

KEYS = NBInput()

try:
    clear()
    KEYS.nb_term()
    objback = backgroud()
    objper = Hero(5,5)
    mainobj = Game()
    obstacle = enemyallotment()
    Top = topbar()
    Top.assignboost()
    cur_time = lambda: int(round(time.time()*1000))
    prev_time = cur_time()
    flag = 0
    acc = 4
    T = 60
    while True:
        tt = cur_time()
        if(tt - prev_time > T):
            prev_time = tt
            sys.stdout.flush()
            mainobj.printBack(objback,Top)
            obst = list(range(4))
            v = 0
            if(Top.getboost() == 0):
                T = 60
            if(flag%400 == 0):
                obstacle.addobstacle(Magnet(181))
            if(flag % 40 == 0):
                s = random.choice(obst)
                if s == 0 :
                    obstacle.addobstacle(verticle(random.choice(list(range(22,24))),181))
                if s == 1 :
                    obstacle.addobstacle(horizontal(random.choice(list(range(5,39))),181))
                if s == 2 :
                    obstacle.addobstacle(diagonaldown(random.choice(list(range(0,22))),181))
                x = random.choice(list(range(5,39)))
                y=181
                # acc += 1    
                for i in range(7):
                    obstacle.addobstacle(coins(x,y))
                    y += 1
            if(flag%2 == 0):
                v = objper.gravity(objback,acc)
                if(v != -1):
                    acc = v
                    for i in range(int(acc / 5)):
                        objper.gravity(objback,acc)
            if(v == -1):
                obstacle.moveall(objback,Top,objper)
            else:
                v = obstacle.moveall(objback,Top,objper)
            c = ''
            if KEYS.kb_hit():
                c = KEYS.get_ch()
            if c == 'q':         # x1b is ESC
                break
            if c == 'd' :
                v = objper.moveR(objback)
            if c == 'a' :
                v = objper.moveL(objback)
            if c == 'w' :
                acc = 2
                v = objper.moveU(objback)
                if(v != -1):
                    v = objper.moveU(objback)
                # v = objper.moveU(objback)
                                 
            if c == 'p' :
                obstacle.addobstacle(bullet(objper.get_current_x()+2,objper.get_current_y()+4))
            if c == ' ':
                objback.shield = True
            if c == 's':
                T = 40
                Top.assignboost()
            if v == -1:
                break
            KEYS.flush()
            flag += 1
        
finally:
    clear()
    KEYS.flush()
    KEYS.or_term()
    print("Game Over.")
    