from tkinter import *
import Entrance
import Greenhouse
from Player import *

class West:
  def __init__(self):
    self.__bg = Canvas(width =800,height = 445)
    self.__bg.pack()
    self.__foyer_pic = PhotoImage(file = 'Bg\\library.gif')
    self.__bg.create_image(0,0,image = self.__foyer_pic,anchor=NW)
    self.__bg.image = self.__foyer_pic

    self.__return_entrance = Button(self.__bg,text = 'Return to Entrance',\
                                    command = self.__return_entrance)
    self.__return_entrance.place(x=270,y=110)

    self.__bgreen = Button(self.__bg,text = 'Greenhouse',\
                           command = self.__greenhouse)
    self.__bgreen.place(x=550,y=215)
    
  def __greenhouse(self):
    self.__bg.destroy()
    Greenhouse.Greenhouse()
  def __return_entrance(self):
    self.__bg.destroy()
    Entrance.Entrance()

  def HUD(self):
    self.__hp = Label(self.__bg,\
                      text = 'HP %s/%s'%(Player.hpcurrent,Player.hpmax),\
                      fg = 'blue', font =('Helvetica',8))
    self.__hp.place(x = 5, y = 5)
    self.__gold = Label(self.__bg,\
                        text = 'Gold: %s'%(Player.gold),\
                        font = ('Helvetica',8))
    self.__gold.place(x = 5, y = 28)


