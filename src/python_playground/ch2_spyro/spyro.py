from math import cos, gcd, radians, sin
from turtle import Turtle


class Spiro:
    def __init__(self, xc, yc, col, R, r, l):
        self.t = Turtle()
        self.t.shape("turtle")
        self.step = 5
        self.drawingComplete = False
        self.setparams(xc, yc, col, R, r, l)
        self.restart()

    def setparams(self, xc, yc, col, R, r, l):
        self.xc = xc
        self.yc = yc
        self.col = col
        self.R = R
        self.r = r
        self.l = l
        self.nRot = self.r // gcd(self.r, self.R)
        self.k = r / float(R)
        self.t.color(*col)

    def restart(self):
        self.drawingComplete = False
        self.t.showturtle()
        self.t.up()
        self.a = 0
        self.move()
        self.t.down()

    def move(self):
        a = radians(self.a)
        x = self.R * ((self.l - self.k) * cos(a) + self.l * self.k * cos((self.l - self.k) * a / self.k))
        y = self.R * ((self.l - self.k) * sin(a) + self.l * self.k * sin((self.l - self.k) * a / self.k))
        self.t.setpos(self.xc + x, self.yc + y)

    def draw(self):
        for i in range(0, 360 * self.nRot + 1, self.step):
            self.a = i
            self.move()
        self.t.hideturtle()

    def update(self):
        if self.drawingComplete:
            return
        self.a += self.step
        self.move()
        if self.a >= 360 * self.nRot:
            self.drawingComplete = True
            self.t.hideturtle()

    def clear(self):
        self.t.clear()
