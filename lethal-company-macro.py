import keyboard
from time import sleep
import threading
macroOn = False
def macroThread():
    global macroOn
    while True:
        if macroOn:
            for i in ('b3','c1','c2','c7','d6','f2','h5','i1','j6','k9','l0','m6','m9','o5','p1','r2','r4','t2','u2','u9','v0','x8','y9','z3'):
                [keyboard.press_and_release(o) for o in i]
                keyboard.press_and_release(" ")
            keyboard.press_and_release("enter")
            sleep(0.5)
        sleep(0.1)
def listeningThread():
    global macroOn
    while True:
        if keyboard.is_pressed("`"):
            macroOn = not macroOn
        sleep(0.1)
threading.Thread(target=macroThread).start()
threading.Thread(target=listeningThread).start()