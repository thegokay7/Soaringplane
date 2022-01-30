import time
import turtle
import random
from turtle import Turtle

pencere = turtle.Screen()
pencere.title('Soaring Plane - Süzülen Uçak')
pencere.bgcolor('white')
pencere.bgpic('background.gif')
pencere.setup(width=600, height=780)

pencere.tracer(0)

pencere.register_shape('plane.gif')

plane: Turtle = turtle.Turtle()
plane.speed(0)
plane.color('black')
plane.shape('plane.gif')
plane.penup()
plane.goto(-180, 0)
plane.dx = 0
plane.dy = 1

puan = 100
yaz = turtle.Turtle()
yaz.speed(0)
yaz.color('black')
yaz.shape('square')
yaz.hideturtle()
yaz.penup()
yaz.goto(0, 300)
yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'bold'))


yercekimi = -0.3

def plane_up(x, y):
    plane.dy = plane.dy + 8

    if plane.dy > 8:
        plane.dy = 8

sutunlar = []
pencere.listen()
pencere.onscreenclick(plane_up)

starting_time = time.time()
while True:
    time.sleep(0.02)
    pencere.update()

    plane.dy = plane.dy + yercekimi

    if (time.time() - starting_time > random.randint(5, 15)):
        starting_time = time.time()
        sutun_ust = turtle.Turtle()

        sutun_ust.speed(0)
        sutun_ust.color('blue')
        sutun_ust.shape('square')
        sutun_ust.h = random.randint(10, 20)
        sutun_ust.shapesize(sutun_ust.h, 2, outline=None)
        sutun_ust.penup()
        sutun_ust.goto(300, 250)
        sutun_ust.dx = -2
        sutun_ust.dy = 0

        sutun_alt = turtle.Turtle()
        sutun_alt.speed(0)
        sutun_alt.color('blue')
        sutun_alt.shape('square')
        sutun_alt.h = 40 - sutun_ust.h - random.randint(1, 10)
        sutun_alt.shapesize(sutun_alt.h, 2, outline=None)
        sutun_alt.penup()
        sutun_alt.goto(300, -250)
        sutun_alt.dx = -2
        sutun_alt.dy = 0

        sutunlar.append((sutun_ust, sutun_alt))

    y = plane.ycor()
    y = y + plane.dy
    plane.sety(y)
    if len(sutunlar) > 0:
        for sutun in sutunlar:
            x = sutun[0].xcor()
            x = x + sutun[0].dx
            sutun[0].setx(x)
            x = sutun[1].xcor()
            x = x + sutun[1].dx
            sutun[1].setx(x)
            if sutun[0].xcor() < -350:
                sutun[0].hideturtle()
                sutun[1].hideturtle()
                sutunlar.pop(sutunlar.index((sutun)))
            if (plane.xcor()+10>sutun[0].xcor()-20) and (plane.xcor()-10<sutun[0].xcor()+20):
                if (plane.ycor()+10>sutun[0].ycor()-sutun[0].h*10) or (plane.ycor()-10<sutun[1].ycor()+sutun[1].h*10):
                    puan = puan - 1
                    yaz.clear()
                    yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'bold'))

    if puan < 0:
        yaz.clear()
        yaz.write('Kaybettiniz'.format(puan), align='center', font=('Courier', 24, 'bold'))


