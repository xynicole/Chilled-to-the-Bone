from tkinter import *
import Town
import Bar
import Guess
from Player import *

class Tavern:
  def __init__ (self):
    self.__spoken = 0
    self.__bg = Canvas(width =800,height = 445)
    self.__bg.pack()
    self.__tavern_pic = PhotoImage(file = 'Bg\\tavern.gif')
    self.__bg.create_image(0,0,image = self.__tavern_pic,anchor=NW)
    self.__bg.image = self.__tavern_pic
    
    self.__hp = Label(self.__bg,\
                      text = 'HP %s/%s'%(Player.hpcurrent,Player.hpmax),\
                      fg = 'blue', font =('Helvetica',8))
    self.__hp.place(x = 5, y = 5)
    self.__gold = Label(self.__bg,\
                        text = 'Gold: %s'%(Player.gold),\
                        font = ('Helvetica',8))
    self.__gold.place(x = 5, y = 28)
    
    self.__return_town = Button(self.__bg, text = 'Return to Town',\
                                command = self.__return_town)
    self.__return_town.place(x=650,y=350)
    self.__gambler = Button(self.__bg, text = 'Gambler',command=self.__gamble)
    self.__gambler.place(x = 150, y = 225)
    self.bartender = Button(self.__bg, text = 'Bartender',\
                              command = self.__bar)
    if Player.gold > 0:
      self.bartender.place(x=375,y=135)
      self.bartender.configure(state = 'disabled')
    else:
      self.bartender.place(x=375,y=135)
      
    mainloop()

  def __return_town(self):
    self.__bg.destroy()
    Town.Town()
  def __gamble(self):
    self.__bg.destroy()
    Guess.Guess()

  def __bar(self):
    Player.unlock_c = 1
    self.__bg.destroy()
    Bar.Bar()
    
    

