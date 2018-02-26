#!/usr/bin/env python3
# coding: utf-8
# File: turtle_demo.py
# Author: lxw
# Date: 12/4/17 2:52 PM

# coding: utf-8
import turtle as tl
import time


def star():
    tl.color("green", "yellow")
    tl.begin_fill()
    tl.pensize(10)
    tl.home()
    tl.speed(0)
    for i in range(5):
        tl.forward(200)
        tl.right(144)
    tl.up()
    tl.goto(-60, -200)
    tl.end_fill()


def trunk(length, level, colorList, colorLen):
    # exit
    if level == 0:
        return

    # main body
    distance = length * level * 0.05
    tl.pensize(level * 0.3)
    tl.pencolor(colorList[level % colorLen])
    tl.fd(distance)

    # left sub-body
    tl.left(30)
    trunk(length, level - 1, colorList, colorLen)

    # right sub-body
    tl.right(60)
    trunk(length, level - 1, colorList, colorLen)
    tl.left(30)

    # main body
    tl.pencolor(colorList[level % colorLen])
    tl.bk(distance)


def drawTrunk():
    tl.pu()
    tl.home()
    tl.speed(0)
    tl.delay(0)    # Set or return the drawing delay in milliseconds. (This is approximately the time interval between two consecutive canvas updates.)
    tl.color("red", "purple")
    tl.lt(90)
    tl.bk(100)
    tl.pd()

    # colorList = ["red", "black", "blue", "green", "orange", "purple"]
    colorList = ["black"]
    colorLen = len(colorList)
    trunk(200, 12, colorList, colorLen)
    return
    """
    # 树的倒影
    tl.pu()
    tl.home()
    tl.rt(90)
    tl.fd(40)
    tl.pd()
    trunk(100, 6, colorList, colorLen)
    """


def drawHafTaiChi():
    tl.begin_fill()
    tl.circle(-150, 180)
    tl.circle(-300, 180)
    tl.rt(180)
    tl.circle(150, 180)
    tl.end_fill()


def drawTaiChi():
    tl.home()
    tl.speed(6)
    tl.lt(180)
    tl.pd()
    tl.color("black", "black")
    drawHafTaiChi()
    tl.home()
    tl.color("black", "white")
    drawHafTaiChi()

    tl.pu()
    tl.goto(0, 100)
    tl.seth(0)
    tl.pd()
    tl.begin_fill()
    tl.circle(50)
    tl.end_fill()

    tl.pu()
    tl.goto(0, -100)
    tl.seth(0)
    tl.pd()
    tl.color("black", "black")
    tl.begin_fill()
    tl.circle(-50)
    tl.end_fill()
    tl.ht()


# tl.goto(0, -100)

def drawCircle():
    tl.speed(0)
    tl.color("green", "yellow")
    tl.home()
    tl.pd()
    # tl.begin_fill()
    for i in xrange(36):
        tl.circle(-100)
        tl.rt(10)
        tl.fd(10)
    tl.ht()


# tl.end_fill()

def drawCircle1():
    tl.speed(0)
    tl.color("green", "yellow")
    tl.pensize(2)
    tl.home()
    tl.pd()
    # tl.begin_fill()
    for i in xrange(36):
        tl.pd()
        tl.circle(-200, 297)
        tl.pu()
        tl.circle(-200, 63)
        tl.rt(10)
        tl.fd(10)
    tl.ht()


# tl.end_fill()

def pythonLogoUp():
    tl.fd(30)
    tl.lt(90)
    tl.fd(150)
    tl.rt(90)
    tl.fd(100)

    tl.rt(15)
    tl.circle(-100, 30)
    tl.rt(5)
    tl.circle(-180, 40)
    tl.seth(0)
    tl.fd(32)
    tl.circle(-180, 40)
    tl.rt(5)
    tl.circle(-100, 30)
    tl.seth(270)

    tl.fd(220)
    tl.circle(-60, 90)
    tl.fd(230)
    tl.circle(60, 90)
    tl.fd(90)
    tl.rt(90)
    tl.fd(80)

    tl.rt(15)
    tl.circle(-100, 30)
    tl.rt(5)
    tl.circle(-180, 40)
    tl.seth(90)
    tl.fd(18)
    tl.circle(-180, 40)
    tl.rt(5)
    tl.circle(-100, 30)
    tl.seth(0)
    tl.fd(266)


def pythonLogoDown():
    tl.fd(30)
    tl.lt(90)
    tl.fd(150)
    tl.rt(90)
    tl.fd(100)

    tl.rt(15)
    tl.circle(-100, 30)
    tl.rt(5)
    tl.circle(-180, 40)
    tl.seth(180)
    tl.fd(32)
    tl.circle(-180, 40)
    tl.rt(5)
    tl.circle(-100, 30)
    tl.seth(90)

    tl.fd(220)
    tl.circle(-60, 90)
    tl.fd(230)
    tl.circle(60, 90)
    tl.fd(90)
    tl.rt(90)
    tl.fd(80)

    tl.rt(15)
    tl.circle(-100, 30)
    tl.rt(5)
    tl.circle(-180, 40)
    tl.seth(270)
    tl.fd(18)
    tl.circle(-180, 40)
    tl.rt(5)
    tl.circle(-100, 30)
    tl.seth(180)
    tl.fd(266)


def drawPythonLogo():
    tl.speed(0)
    tl.color("white", "blue")
    tl.pensize(2)
    tl.home()
    tl.pd()
    tl.seth(90)
    tl.pu()
    tl.fd(160)
    tl.pd()
    tl.begin_fill()
    pythonLogoUp()
    tl.end_fill()
    tl.pu()
    tl.home()
    tl.color("white", "yellow")
    tl.seth(270)
    tl.fd(160)
    tl.pd()
    tl.begin_fill()
    pythonLogoDown()
    tl.end_fill()

    tl.pu()
    tl.goto(-90, 230)
    tl.pd()
    tl.color("white", "white")
    tl.begin_fill()
    tl.circle(-40)
    tl.end_fill()
    tl.seth(0)
    tl.pu()
    tl.goto(90, -230)
    tl.pd()
    tl.begin_fill()
    tl.circle(-40)
    tl.end_fill()
    """
    tl.pensize(10)
    tl.write("Guo Congmin, I love you!")
    """

    tl.ht()


def drawCube():
    tl.speed(10)
    tl.color("green", "yellow")
    tl.pensize(10)
    tl.pu()
    tl.home()
    tl.pd()
    for i in range(72):
        tl.fd(200)
        tl.rt(90)
        tl.fd(200)
        tl.rt(90)
        tl.fd(200)
        tl.rt(90)
        tl.fd(200)
        tl.rt(90)

        tl.rt(5)
    tl.ht()


if __name__ == '__main__':
    """
    star()
    time.sleep(3)
    tl.clear()
    drawTrunk()
    time.sleep(3)
    tl.clear()
    drawTaiChi()
    # drawTrunk()
    time.sleep(30)
    tl.clear()
    drawCircle()
    time.sleep(3)
    tl.clear()
    drawCircle1()
    time.sleep(3)
    tl.clear()
    drawPythonLogo()
    time.sleep(3)
    tl.clear()
    """
    drawCube()
    time.sleep(3)
