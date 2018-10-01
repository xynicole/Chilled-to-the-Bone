from tkinter import *
import Tavern
import Shop
import Forest
from Player import *
class Town:
  def __init__ (self):

    
    self.__bg = Canvas(width =800,height = 445)
    self.__bg.pack()
    self.__town_pic = PhotoImage(file = 'Bg\\town.gif')
    self.__bg.create_image(0,0,image = self.__town_pic,anchor=NW)
    self.__bg.image = self.__town_pic

    self.HUD()

    
    self.__bs_pic = PhotoImage(file = 'Buttons\\shopbutton.gif')
    self.__button_shop = Button(self.__bg, image = self.__bs_pic,\
                                command = self.__open_shop,bg = 'black')
    self.__button_shop.place(x=600,y=275)
    self.__button_shop.image = self.__bs_pic
    
    self.__bt_pic = PhotoImage(file = 'Buttons\\tavernbutton.gif')
    self.__button_tavern = Button(self.__bg,\
                                  image = self.__bt_pic,\
                                  command = self.__open_tavern,bg = 'black')
    self.__button_tavern.image = self.__bt_pic
    self.__button_tavern.place(x=100,y=325)
#   Unlock Castle Button
    if Player.unlock_c == 1:
      self.__bcastle = Button(self.__bg, text = 'Forest',\
                              command = self.__open_forest)
      self.__bcastle.place(x = 375, y = 200)
      self.__healer = Button(self.__bg,text = 'Healer',\
                             command = self.__heals)
      self.__healer.place(x=275,y = 275)
                           
    mainloop()
  def __heals(self):
    the_health = Player.hpmax
    Player.hpcurrent = the_health
    self.HUD()
    
  def __open_tavern(self):
    self.__bg.destroy()
    Tavern.Tavern()

  def __open_shop(self):
    self.__bg.destroy()
    Shop.Shop()

  def __open_forest(self):
    self.__bg.destroy()
    Forest.Forest()
    
  def HUD(self):
    if hasattr(Forest,'self.__hp'):
      self.__hp.destroy()
    if hasattr(Forest,'self.__gold'):
      self.__gold.destroy()

    else:
      self.__hp = Label(self.__bg,\
                        text = 'HP %s/%s'%(Player.hpcurrent,Player.hpmax),\
                        fg = 'blue', font =('Helvetica 8 bold'))
      self.__hp.place(x = 5, y = 5)
      self.__gold = Label(self.__bg,\
                          text = 'Gold: %s'%(Player.gold),\
                          font = ('Helvetica',8))
      self.__gold.place(x = 5, y = 28)

