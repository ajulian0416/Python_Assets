from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
from random import randint
import numpy as np
import time

class RollTheDice():

    def _init_(self):

        self.main = pg.GraphicsWindow(title = 'Roll The Dice')
        self.main.showMaximized()

        self.win1 = self.main.addPlot(title = 'Die Rolls')
        self.win1.setXRange(1,6)
        self.win1.setYRange(0,.25)
        self.main.nextRow()
##        self.main.nextRow()
        self.win3 = self.main.addPlot(title = 'Dice Total')
        self.win3.setXRange(2,12)
        self.win3.setYRange(0,.25)
        self.setup()

##        print('Check Point 2')

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)
        

    def setup(self):
        
        self.die = [1,2,3,4,5,6]
        self.dice = [2,3,4,5,6,7,8,9,10,11,12]
        self.diceOne = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}
        self.PdiceOne = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}
        self.diceTwo = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}
        self.PdiceTwo = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}
        self.diceTotal = {'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,
                         '8':0,'9':0,'10':0,'11':0,'12':0}
        self.PdiceTotal = {'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,
                         '8':0,'9':0,'10':0,'11':0,'12':0}
        self.dieP = {'1':1/6,'2':1/6,'3':1/6,'4':1/6,'5':1/6,'6':1/6}
        self.diceP = {'2':1/36,'3':2/36,'4':3/36,'5':4/36,'6':5/36,'7':1/6,
                      '8':5/36,'9':4/36,'10':3/36,'11':2/36,'12':1/36}
        self.total = 0

        PdiceOne = list(self.PdiceOne.values())
        PdiceTwo = list(self.PdiceTwo.values())
        PdiceTotal = list(self.PdiceTotal.values())
        diceP = list(self.diceP.values())

        self.bg1 = pg.BarGraphItem(height = PdiceOne, x = self.die, width = 1, brush = (255,255,255,50))
        self.win1.addItem(self.bg1)
        self.bg2 = pg.BarGraphItem(height = PdiceTwo , x = self.die, width = 1, brush = (0,0,0,50))
        self.win1.addItem(self.bg2)

        self.bg3 = pg.BarGraphItem(height = PdiceTotal, x = self.dice, width = 1, brush = (255,255,255,25))
        self.win3.addItem(self.bg3)#,rowspan = 5,colspan = 5)
        self.bg4 = pg.BarGraphItem(height = diceP, x = self.dice, width = 1, brush = (255,0,0,50))
        self.win3.addItem(self.bg4)#,rowspan = 5,colspan = 5)
        self.samples = pg.TextItem(text = 'Pair of Dice Rolled: ' + str(self.total))
        self.samples.setPos(3,.25)
        self.win3.addItem(self.samples)

##        print('Check Point 1')

    def roll(self,loop):

##        print('Check Point 3')

        for x in range(0,loop+1):

            self.total += 1

            rand  = randint(1,6)
            Srand = str(rand)
            self.diceOne[Srand] += 1
            self.PdiceOne[Srand] = self.diceOne[Srand]/self.total
            rand2 = randint(1,6)
            Srand2 = str(rand2)
            self.diceTwo[Srand2] += 1
            self.PdiceTwo[Srand2] = self.diceTwo[Srand2]/self.total
            add = rand + rand2
            Sadd = str(add)
            self.diceTotal[Sadd] +=1
            self.PdiceTotal[Sadd] = self.diceTotal[Sadd]/self.total

        self.convergence()

    def convergence(self):

        count = 0

        for index in range(2,13):
            if abs(self.PdiceTotal[str(index)]-self.diceP[str(index)])/self.diceP[str(index)] < .15:
                count +=1
        if count == len(list(self.PdiceTotal.values())):
            self.bg4.setOpts(brush = (0, 255, 0,50))
        else:
            self.bg4.setOpts(brush = (255,0,0,50))


    def rollIt(self):

##        print('Check Point 4')

        if self.total < 250:

            self.roll(0)

        elif self.total < 1000:

            self.roll(10)

        elif self.total < 1500:

            self.roll(100)

        else:

            self.roll(1000)


    def update(self):

        self.rollIt()        

        PdiceOne = list(self.PdiceOne.values())
        PdiceTwo = list(self.PdiceTwo.values())
        PdiceTotal = list(self.PdiceTotal.values())

        self.bg1.setOpts(height = PdiceOne, x = self.die)
        self.bg2.setOpts(height = PdiceTwo, x = self.die)
        self.bg3.setOpts(height = PdiceTotal, x = self.dice)

        self.samples.setText('Pair of Dice Rolled: ' + str(self.total))

import sys
if(sys.flags.interactive != 1) or not hasattr(QtCore,'PYQT_VERSION'):
    app = QtGui.QApplication(sys.argv)
    RTD = RollTheDice()
    RTD._init_()
    app.instance().exec()
        
