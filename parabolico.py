"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

Integrantes:
Karen Lizette Rodríguez Hernández - A01197734
Jorge Eduardo Arias Arias - A01570549
Hernán Salinas Ibarra - A01570409

15/09/2021

Exercises marked by ***ejercicio realizado***

"""

from random import randrange
from turtle import *
from typing import Sized

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
gravity = 25
s = 200
targets = []
count = 0


def changeGravity(value):
    global gravity
    gravity = value

def changeSpeed(sp):                                # ***Exercise 4: change speed***
    global s
    s = sp

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / gravity
        speed.y = (y + 200) / gravity


def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5
        target.y -= 0.5                             # ***Exercise 3: add gravity to targets***

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
    draw()
    
    if len(dupe) != len(targets):
        global count
        diferencia = len(dupe)-len(targets)
        count += diferencia
        style = ('Courier', 30, 'bold')
        write(count, font=style, align='right')

    for target in targets:
        if not inside(target):
            return

    ontimer(move, s)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
listen()
onkey(lambda: changeGravity(50), 'a')
onkey(lambda: changeGravity(25), 's')
onkey(lambda: changeGravity(12), 'd')
onkey(lambda: changeSpeed(100), 'q')
onkey(lambda: changeSpeed(50), 'w')
onkey(lambda: changeSpeed(25), 'e')
onscreenclick(tap)
move()
done()