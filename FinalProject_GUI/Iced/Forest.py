from tkinter import *
import Town
from Player import *
from Toad import *
import random
import Death
import Castle

class Forest:
  def __init__(self):
    if Player.toad_killed == 0:
      self.__bg = Canvas(width =800,height = 445)
      self.__bg.pack()
      self.__town_pic = PhotoImage(file = 'Bg\\toad.gif')
      self.__bg.create_image(0,0,image = self.__town_pic,anchor=NW)
      self.__bg.image = self.__town_pic
      self.HUD()
      
      self.__block_pic = PhotoImage(file = 'ToadText\\Toad1.gif')
      self.__block = Label(self.__bg,image = self.__block_pic)
      self.__block.place(x=200,y=300)
      self.__block.image= self.__block_pic
      self.__attack_button()
    else:
      self.__bg = Canvas(width =800,height = 445)
      self.__bg.pack()
      self.__town_pic = PhotoImage(file = 'Bg\\forest.gif')
      self.__bg.create_image(0,0,image = self.__town_pic,anchor=NW)
      self.__bg.image = self.__town_pic
      self.__fin = Button(self.__bg,text = 'Move on'\
                          ,command = self.__finish)
      self.__fin.place(x = 680, y = 390)
      self.__return = Button(self.__bg,text = 'Return to Town',\
                             command = self.__return_town)
      self.__return.place(x = 680, y = 340)
      self.HUD()

    

  def __attack_button(self):  
    self.__battack = Button(self.__bg, text = 'Attack!',\
                            command = self.__attack, bg = 'DodgerBlue3')
    self.__battack.place(x=680, y=340)
  def __attack(self):
    self.__battack.destroy()
    self.__block.destroy()
    self.__att_pic = PhotoImage(file = 'ToadText\\Toad3.gif')
    self.__att = Label(self.__bg,image = self.__att_pic)
    self.__att.place(x=200,y=300)
    self.__att.image= self.__att_pic
    self.__damage = 0
    self.__damage = int(random.choice(Player.dmg))
    Toad.currenthp -= self.__damage
    
    self.__next = Button(self.__bg,text = 'Next',command = self.__toad_attack)
    self.__next.place(x = 680, y = 390)
    self.HUD()
  def __toad_attack(self):
    if Toad.currenthp > 0:
      self.__next.destroy()
      self.__att.destroy()
      self.__t2_pic = PhotoImage(file = 'ToadText\\Toad2.gif')
      self.__t2 = Label(self.__bg,image = self.__t2_pic)
      self.__t2.place(x=200,y=300)
      self.__t2.image= self.__t2_pic
      
      self.__tdam = 0
      self.__dealdmg = int(random.choice(Toad.damage))
      self.__tdam = self.__dealdmg
      Player.hpcurrent -= self.__tdam
      self.HUD()
      if Player.hpcurrent < 1:
        self.__att.destroy()
        self.__t5_pic = PhotoImage(file = 'ToadText\\Toad5.gif')
        self.__t5 = Label(self.__bg,image = self.__t5_pic)
        self.__t5.place(x=200,y=300)
        self.__t5.image= self.__t5_pic
        self.__death = Button(self.__bg,text = 'Next'\
                             ,command = self.__death)
        self.__death.place(x = 680, y = 390)
      else:
        self.__turn=Button(self.__bg,text = 'Next',\
                           command = self.__attack_button)
        self.__turn.place(x = 680, y = 390)
        
    else:
      self.__t6_pic = PhotoImage(file = 'ToadText\\Toad6.gif')
      self.__t6 = Label(self.__bg,image = self.__t6_pic)
      self.__t6.place(x=200,y=300)
      self.__t6.image= self.__t6_pic
      Player.hpmax += 1
      Player.toad_killed = 1
      Player.gold += 50
      self.__fin = Button(self.__bg,text = 'Move on'\
                            ,command = self.__finish)
      self.__fin.place(x = 680, y = 390)
      self.__return = Button(self.__bg,text = 'Return to Town',\
                             command = self.__return_town)
      self.__return.place(x = 680, y = 340)
      self.HUD()

  def __finish(self):
    self.__bg.destroy()
    Castle.Castle()
  def __death(self):
    self.__bg.destroy()
    Death.Death()

  def __return_town(self):
    self.__bg.destroy()
    Town.Town()

  def HUD(self):
    if hasattr(Forest,'self.__hp'):
      self.__hp.destroy()
    if hasattr(Forest,'self.__gold'):
      self.__gold.destroy()

    self.__hp = Label(self.__bg,\
                      text = 'HP %s/%s'%(Player.hpcurrent,Player.hpmax),\
                      fg = 'blue', font =('Helvetica 8 bold'))
    self.__hp.place(x = 5, y = 5)
    self.__gold = Label(self.__bg,\
                        text = 'Gold: %s'%(Player.gold),\
                        font = ('Helvetica',8))
    self.__gold.place(x = 5, y = 28)

