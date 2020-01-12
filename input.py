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
def isData():
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

old_settings = termios.tcgetattr(sys.stdin)
try:
    tty.setcbreak(sys.stdin.fileno())
    system('clear')
    objback = backgroud()
    objper = Hero(5,5)
    mainobj = Game()
    while 1:
        mainobj.printBack(objback)
        sys.stdout.flush()
        if isData():
            tcflush(sys.stdin, TCIFLUSH) 
            c = sys.stdin.read(1)
            if c == 'q':         # x1b is ESC
                break
            if c == 'd' :
                objper.moveR(objback)
            if c == 'a' :
                objper.moveL(objback)
        time.sleep(0.0167)
finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)