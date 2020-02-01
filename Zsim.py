#Python

import tkinter
import os
import time
import PIL

from PIL import Image
from PIL import ImageTk

PATH = os.path.dirname(os.path.abspath(__file__))

class Application:
    def __init__(self, pwidth, pheight, title):
        self.window = tkinter.Tk()
        self.window.title(title)
        self.window.width = pwidth
        self.window.height = pheight
        self.window.wm_attributes("-topmost", 1)
        self.window.resizable(0, 0)

        self.canvas = tkinter.Canvas(self.window, width=pwidth, height=pheight)
        self.canvas.pack()

        self.axlecountergroup = []

        self.window.update()

    def loop(self):
        while 1:
            self.window.update_idletasks()
            self.window.update()
            time.sleep(0.01)

            for acounter in self.axlecountergroup:
                if Train1.rightx == acounter.x:
                    if acounter.targetright != None:
                        self.canvas.itemconfig(acounter.targetright.block, fill="red")

                if Train1.leftx == acounter.x:
                    if acounter.targetleft != None:
                        self.canvas.itemconfig(acounter.targetleft.block, fill="green")

            Train1.move()

class Objects(Application):
    def __init__(self, objtype, sim):
        self.type = objtype
        self.sim = sim

class Track(Objects):
    def __init__(self, x, y, sim):
        Objects.__init__(self, "Track", sim)
        sim.canvas.create_line(x, y, sim.window.width, y, width=3)

class Train(Objects):
    def __init__(self, sim, trntype, trnimage, x, y):
        Objects.__init__(self, "Train", sim)
        self.trntype = trntype
        self.trnimage = trnimage
        self.leftx = x
        self.rightx = self.leftx+112
        self.y = y
        self.trn = self.sim.canvas.create_image(x, y, image=trnimage, anchor="sw")

    def move(self):
        self.sim.canvas.move(self.trn, 1, 0)
        self.leftx += 1
        self.rightx += 1

class AxleCounter(Objects):
    def __init__(self, x, targetleft, targetright, sim):
        Objects.__init__(self, "AxleCounter", sim)
        self.x = x
        self.targetleft = targetleft
        self.targetright = targetright
        self.line = sim.canvas.create_line(self.x, 75, self.x, 125, width=2, fill="red")


class Signals(Objects):
    def __init__(self, sigtype):
        self.sigtype = sigtype

class Block(Objects):
    def __init__(self, x1, y1, x2, y2, sim):
        Objects.__init__(self, "Block", sim)
        self.block = self.sim.canvas.create_rectangle(x1, y1, x2, y2, fill="green")

Simulation = Application(1000, 500, "Simulation")

Train1Img = ImageTk.PhotoImage(Image.open(PATH+"/1144.gif").resize((112, 41), Image.ANTIALIAS))
Train1 = Train(Simulation, "Electric", Train1Img, 0, 100)
MainTrack = Track(0, 100, Simulation)
Block1 = Block(200, 100, 700, 125, Simulation)
ACounter1 = AxleCounter(200, None, Block1 ,Simulation)
ACounter2 = AxleCounter(700, Block1, None, Simulation)

Simulation.axlecountergroup.append(ACounter1)
Simulation.axlecountergroup.append(ACounter2)

Simulation.loop()