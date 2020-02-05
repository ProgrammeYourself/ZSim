#Python

import tkinter
import os
import time
import PIL
import io
import requests
import base64
import urllib.request
import _thread

from PIL import Image
from PIL import ImageTk



PATH = os.path.dirname(os.path.abspath(__file__))

image_urls = []
images = []

image_urls.append("https://raw.githubusercontent.com/ProgrammeYourself/Data/master/ZSim/TrainSprites/lok-1144.gif")
image_urls.append("https://raw.githubusercontent.com/ProgrammeYourself/Data/master/ZSim/Tempomat.png")




class Application:
    def __init__(self, pwidth, pheight, title):
        self.window = tkinter.Tk()
        self.window.title(title)
        self.window.width = pwidth
        self.window.height = pheight
        #self.window.wm_attributes("-topmost", 1)
        self.window.resizable(0, 0)

        self.canvas = tkinter.Canvas(self.window, width=pwidth, height=200)
        self.canvas.pack()

        self.display_canvas = tkinter.Canvas(self.window, width=455, height=500, bg="#282828")
        self.display_canvas.pack()

        self.axlecountergroup = []
        self.objectgroup = []

        self.window.update()

        self.mcoords = tkinter.Label(self.window, width=35)
        self.mcoords.pack()
        self.display_canvas.bind("<Motion>", self.display_coords)

    def display_coords(self, event):
        self.mcoords["text"] = str(event.x) + ", " + str(event.y)
        
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
            Train1.brake()

            if Train1.leftx >= 1500:
                self.canvas.delete(Train1.train)
                Train1.train = self.canvas.create_image(0, 100, image=Train1.trnimage, anchor="sw")
                Train1.x = 0
                Train1.leftx = 0
                Train1.rightx = 112
                
            Train1.move()


            for item in LZB_Display.v_ist_line_map.items():
                if str(int(Train1.v_ist*32.7)) == item[0]:
                    self.display_canvas.delete(LZB_Display.v_ist_zeiger)
                    LZB_Display.v_ist_zeiger = self.display_canvas.create_line(item[1][0],
                                                                        item[1][1], item[1][2], item[1][3], fill="#E8E8E8", width=7)

            #check v_ist and display in text object
            LZB_Display.display_canvas.itemconfig(LZB_Display.v_ist_text, text=str(int(Train1.v_ist*32.7)))

class Display():
    def __init__(self, sim):
        self.sim = sim
        self.display_canvas = sim.display_canvas
        self.v_ist_line_map = {"0": (242, 248, 297, 175),
                               "1": (240, 247, 297, 175),
                               "2": (238, 246, 297, 175),
                               "3": (236, 245, 297, 175),
                               "4": (234, 244, 297, 175),
                               "5": (232, 243, 297, 175),
                               "6": (230, 242, 297, 175),
                               "7": (228, 241, 297, 175),
                               "8": (226, 240, 297, 175),
                               "9": (224, 239, 297, 175),
                               "10": (222, 238, 297, 175),
                               "11": (220, 236, 297, 175),
                               "12": (218, 234, 297, 175),
                               "13": (216, 232, 297, 175),
                               "14": (214, 230, 297, 175),
                               "15": (212, 228, 297, 175),
                               "16": (210, 226, 297, 175),
                               "17": (208, 224, 297, 175),
                               "18": (206, 222, 297, 175),
                               "19": (204, 220, 297, 175),
                               "20": (202, 218, 297, 175)}

        self.draw_display()

    def draw_display(self):
        self.display_canvas.create_line(40, 300, 100, 300, width=2, fill="white")
        self.display_canvas.create_text(100, 302, anchor="se", text="0 m", font=("Arial", 12), fill="white")
        self.display_canvas.create_line(40, 283, 100, 283, width=2, fill="white")
        self.display_canvas.create_text(100, 283, anchor="se", text="100", font=("Arial", 6), fill="white")
        self.display_canvas.create_line(40, 270, 100, 270, width=2, fill="white")
        self.display_canvas.create_text(100, 272, anchor="se", text="250", font=("Arial", 12), fill="white")
        self.display_canvas.create_line(40, 240, 100, 240, width=2, fill="white")
        self.display_canvas.create_text(100, 242, anchor="se", text="500", font=("Arial", 12), fill="white")
        self.display_canvas.create_line(40, 210, 100, 210, width=2, fill="white")
        self.display_canvas.create_text(100, 212, anchor="se", text="750", font=("Arial", 12), fill="white")
        self.display_canvas.create_line(40, 180, 100, 180, width=2, fill="white")
        self.display_canvas.create_text(100, 182, anchor="se", text="1000", font=("Arial", 12), fill="white")
        self.display_canvas.create_line(40, 150, 100, 150, width=2, fill="white")
        self.display_canvas.create_text(100, 152, anchor="se", text="2000", font=("Arial", 12), fill="white")
        self.display_canvas.create_line(40, 120, 100, 120, width=2, fill="white")
        self.display_canvas.create_text(100, 122, anchor="se", text="3000", font=("Arial", 12), fill="white")
        self.display_canvas.create_line(40  , 90, 100, 90, width=2, fill="white")
        self.display_canvas.create_text(100, 92, anchor="se", text="4000", font=("Arial", 12), fill="white")

        self.display_canvas.create_line(40, 295, 42, 295, width=2, fill="white")
        self.display_canvas.create_line(40, 291, 42, 291, width=2, fill="white")
        self.display_canvas.create_line(40, 287, 42, 287, width=2, fill="white")

        self.display_canvas.create_line(40, 279, 45, 279, width=2, fill="white")
        self.display_canvas.create_line(40, 275, 45, 275, width=2, fill="white")

        self.display_canvas.create_line(40, 264, 45, 264, width=2, fill="white")
        self.display_canvas.create_line(40, 258, 45, 258, width=2, fill="white")
        self.display_canvas.create_line(40, 252, 45, 252, width=2, fill="white")
        self.display_canvas.create_line(40, 246, 45, 246, width=2, fill="white")

        self.display_canvas.create_line(40, 234, 45, 234, width=2, fill="white")
        self.display_canvas.create_line(40, 228, 45, 228, width=2, fill="white")
        self.display_canvas.create_line(40, 222, 45, 222, width=2, fill="white")
        self.display_canvas.create_line(40, 216, 45, 216, width=2, fill="white")

        self.display_canvas.create_line(40, 204, 45, 204, width=2, fill="white")
        self.display_canvas.create_line(40, 198, 45, 198, width=2, fill="white")
        self.display_canvas.create_line(40, 192, 45, 192, width=2, fill="white")
        self.display_canvas.create_line(40, 186, 45, 186, width=2, fill="white")

        self.display_canvas.create_line(40, 174, 60, 174, width=2, fill="white")
        self.display_canvas.create_line(40, 168, 60, 168, width=2, fill="white")
        self.display_canvas.create_line(40, 162, 60, 162, width=2, fill="white")
        self.display_canvas.create_line(40, 156, 60, 156, width=2, fill="white")

        self.display_canvas.create_line(40, 144, 60, 144, width=2, fill="white")
        self.display_canvas.create_line(40, 138, 60, 138, width=2, fill="white")
        self.display_canvas.create_line(40, 132, 60, 132, width=2, fill="white")
        self.display_canvas.create_line(40, 126, 60, 126, width=2, fill="white")

        self.display_canvas.create_line(40, 114, 60, 114, width=2, fill="white")
        self.display_canvas.create_line(40, 108, 60, 108, width=2, fill="white")
        self.display_canvas.create_line(40, 102, 60, 102, width=2, fill="white")
        self.display_canvas.create_line(40, 96, 60, 96, width=2, fill="white")
        
        self.lzb_targetrect = self.display_canvas.create_rectangle(10, 302, 32, 88, fill="#00CC00")

        #status: deactivated [all]
        self.pzb_55rect = self.display_canvas.create_rectangle(12, 340, 62, 390, fill="blue", width=0)
        self.pzb_70rect = self.display_canvas.create_rectangle(66, 340, 116, 390, fill="blue", width=0)
        self.pzb_85rect = self.display_canvas.create_rectangle(120, 340, 170, 390, fill="blue", width=0)
        self.lzb_Hrect = self.display_canvas.create_rectangle(174, 340, 224, 390, fill="#990000", width=0)
        self.lzb_E40rect = self.display_canvas.create_rectangle(228, 340, 280, 390, fill="#d1d1d1", width=0)
        self.lzb_Enderect = self.display_canvas.create_rectangle(282, 340, 334, 390, fill="#FFB319", width=0)
        self.lzb_Brect = self.display_canvas.create_rectangle(336, 340, 388, 390, fill="blue", width=0)
        self.lzb_Uerect = self.display_canvas.create_rectangle(390, 340, 442, 390, fill="blue", width=0)

        self.display_canvas.create_text(16, 346, anchor="nw", text="55", font=("Arial Bold", 24), fill="grey", width=50)
        self.display_canvas.create_text(70, 346, anchor="nw", text="70", font=("Arial Bold", 24), fill="grey", width=50)
        self.display_canvas.create_text(124, 346, anchor="nw", text="85", font=("Arial Bold", 24), fill="grey", width=50)
        self.display_canvas.create_text(185, 346, anchor="nw", text="H", font=("Arial Bold", 24), fill="grey", width=50)
        self.display_canvas.create_text(248, 348, anchor="nw", text="E", font=("Arial Bold", 12), fill="#595959", width=20)
        self.display_canvas.create_text(243, 364, anchor="nw", text="40", font=("Arial Bold", 12), fill="#595959", width=20)
        self.display_canvas.create_text(288, 366, anchor="nw", text="Ende", font=("Arial Bold", 12), fill="#595959", width=50)
        self.display_canvas.create_text(350, 346, anchor="nw", text="B", font=("Arial Bold", 24), fill="grey", width=50)
        self.display_canvas.create_text(404, 348, anchor="nw", text="Ü", font=("Arial Bold", 24), fill="grey", width=50)

        #second line

        self.pzb_B40rect = self.display_canvas.create_rectangle(12, 395, 62, 445, fill="#d1d1d1", width=0)
        self.pzb_Hz500rect = self.display_canvas.create_rectangle(66, 395, 116, 445, fill="#990000", width=0)
        self.pzb_Hz1000rect = self.display_canvas.create_rectangle(120, 395, 170, 445, fill="#FFB319", width=0)
        self.pzb_Grect = self.display_canvas.create_rectangle(174, 395, 224, 445, fill="#990000", width=0)
        self.pzb_ELrect = self.display_canvas.create_rectangle(228, 395, 280, 445, fill="blue", width=0)
        self.lzbV40rect = self.display_canvas.create_rectangle(282, 395, 334, 445, fill="#d1d1d1", width=0)
        self.lzb_Srect = self.display_canvas.create_rectangle(336, 395, 388, 445, fill="#990000", width=0)
        self.PrStrect = self.display_canvas.create_rectangle(390, 395, 442, 445, fill="#d1d1d1", width=0)

        
        self.display_canvas.create_image(150, 30, image=images[1], anchor="nw")

        self.display_canvas.create_oval(272, 150, 322, 200, fill="#E8E8E8", width=0)

        self.v_ist_zeiger = self.display_canvas.create_line(241, 247, 297, 175, fill="#E8E8E8", width=7)
        self.v_ist_text = self.display_canvas.create_text(289, 159, anchor="nw", text="0", font=("Arial Bold", 20), fill="#282828")

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
        self.v_ist = 0
        self.train = self.sim.canvas.create_image(x, y, image=trnimage, anchor="sw")

        self.sim.canvas.bind_all("<KeyPress-Right>", self.right)
        self.sim.canvas.bind_all("<KeyPress-Left>", self.left)
        self.sim.objectgroup.append(self)

    def right(self, event):
        self.v_ist += 0.005

    def left(self, event):
        if self.v_ist > 0:
            self.v_ist -= 0.01
        else:
            self.v_ist -= 0.03

    def brake(self):
        if self.v_ist > 0:
            self.v_ist -= 0.0005
        elif self.v_ist < 0:
            self.v_ist += 0.0005


    def move(self):
        self.sim.canvas.move(self.train, self.v_ist, 0)
        self.leftx += self.v_ist
        self.rightx += self.v_ist

class AxleCounter(Objects):
    def __init__(self, x, targetleft, targetright, sim):
        Objects.__init__(self, "AxleCounter", sim)
        self.x = x
        self.targetleft = targetleft
        self.targetright = targetright
        self.line = sim.canvas.create_line(self.x, 75, self.x, 125, width=2, fill="red")

        self.sim.objectgroup.append(self)
        self.sim.axlecountergroup.append(self)


class Signals(Objects):
    def __init__(self, sigtype):
        self.sigtype = sigtype

class Block(Objects):
    def __init__(self, x1, y1, x2, y2, sim):
        Objects.__init__(self, "Block", sim)
        self.block = self.sim.canvas.create_rectangle(x1, y1, x2, y2, fill="green")

Simulation = Application(1500, 500, "Simulation")

for url in image_urls:
    images.append(ImageTk.PhotoImage(Image.open(io.BytesIO(urllib.request.urlopen(url).read()))))

LZB_Display = Display(Simulation)


Train1 = Train(Simulation, "Electric", images[0], 0, 100)
MainTrack = Track(0, 100, Simulation)

Simulation.loop()