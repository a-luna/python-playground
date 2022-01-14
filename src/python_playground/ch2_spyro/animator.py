import turtle
from random import randint, random, uniform

from python_playground.ch2_spyro.spyro import Spiro


class SpiroAnimator:
    def __init__(self, N):
        self.deltaT = 10
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        self.spiros = [Spiro(*self.genRandomParams()) for _ in range(N)]
        turtle.ontimer(self.update, self.deltaT)

    def restart(self):
        for spiro in self.spiros:
            spiro.clear()
            rparams = self.genRandomParams()
            spiro.setparams(*rparams)
            spiro.restart()

    def genRandomParams(self):
        xc = randint(-self.width // 2, self.width // 2)
        yc = randint(-self.height // 2, self.height // 2)
        R = randint(50, min(self.width, self.height) // 2)
        r = randint(10, 9 * R // 10)
        l = uniform(0.1, 0.9)
        col = (random(), random(), random())
        return (xc, yc, col, R, r, l)

    def update(self):
        nComplete = 0
        for spiro in self.spiros:
            spiro.update()
            if spiro.drawingComplete:
                nComplete += 1
        if nComplete == len(self.spiros):
            self.restart()
        turtle.ontimer(self.update, self.deltaT)

    def toggleTurtles(self):
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()
