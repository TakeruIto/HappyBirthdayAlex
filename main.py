import turtle
import threading

import alphabet
from alphabet import *


SPEED = 1
SHAPE = "turtle"
PEN_WIDTH = 2
CHAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SCREEN_SIZE = (800, 600)
CHAR_SIZE = 100


def main():
    wn = turtle.Screen()

    line = "HAPPY BIRTHDAY\nALEX!!"
    line = line.upper()
    pos = getPosition(line)
    stream = []
    t = turtle.Turtle()
    init(t, wn)
    for char, p in zip(line, pos):
        if char in CHAR:
            cls = globals()[char]
            alph = cls(t, *p, CHAR_SIZE)

            alph.draw()
        elif char in "!":
            alph = alphabet.Exclamation(t, *p, CHAR_SIZE)
            alph.draw()
        elif char in "?":
            alph = alphabet.Question(t, *p, CHAR_SIZE)
            alph.draw()
    t.pu()
    angle = (360+(t.towards(min(SCREEN_SIZE)/2, 0)-t.heading())) % 360
    if angle < 180:
        t.left(angle)
    else:
        t.right(360-angle)
    t.goto(min(SCREEN_SIZE)/2, 0)
    t.left(90-t.heading())
    while True:
        t.circle(min(SCREEN_SIZE)/2)


def init(t, wn):
    t.speed(SPEED)
    t.shape(SHAPE)
    t.width(PEN_WIDTH)
    t.color((1., 0., 0.))
    wn.screensize(*SCREEN_SIZE)


def getPosition(line):
    global CHAR_SIZE
    i = 0
    num_br = 0
    tmp = []
    for char in line:
        if char in CHAR or char in " !?":
            i += 1
        elif char == "\n":
            tmp.append(i)
            i = 0

            num_br += 1
    tmp.append(i)

    if max(tmp)*CHAR_SIZE > SCREEN_SIZE[0]:
        CHAR_SIZE = SCREEN_SIZE[0]/max(tmp)
    if len(tmp)*CHAR_SIZE > SCREEN_SIZE[1]:
        CHAR_SIZE = SCREEN_SIZE[1]/len(tmp)

    pos = []
    tmp_br = 0
    for idx_y, tmpy in enumerate(tmp):
        y = (len(tmp)*CHAR_SIZE)/2-CHAR_SIZE*idx_y
        for idx_x in range(tmpy):
            x = -(tmpy*CHAR_SIZE)/2+CHAR_SIZE*idx_x
            pos.append((x, y))
        if tmp_br < num_br:
            pos.append(((tmpy*CHAR_SIZE)/2, y))
            tmp_br += 1
    return pos


if __name__ == "__main__":
    main()
