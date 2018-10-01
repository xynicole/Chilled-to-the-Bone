from tkinter import *
from Player import *
import Town
from Yuki import *
import Death
import End
import random

class Outside:
  def __init__(self):
    self.__bg = Canvas(width =800,height = 445)
    self.__bg.pack()
    self.__end_pic = PhotoImage(file = 'Bg\\final.gif')
    self.__bg.create_image(0,0,image = self.__end_pic,anchor=NW)
    self.__bg.image = self.__end_pic

    self.__next = Button(self.__bg,text = 'Next', command = self.__fight,\
                         bg='white')
    self.__next.place(x=395,y=400)
    self.HUD()

  def __fight(self):
    self.__next.destroy()
    self.__yuki1 = PhotoImage(file = 'YukiText\\Yuki1.gif')
    self.__lyuki1 = Label(self.__bg,image = self.__yuki1)
    self.__lyuki1.place(x=200,y=300)
    self.__lyuki1.image= self.__yuki1
    self.__begin_combat = Button(self.__bg,text = 'Attack',\
                           command = self.__attack)
    self.__begin_combat.place(x=680,y=390)
    if Player.necklace == 1:
      self.__button_necklace = Button(self.__bg,text = 'Bag',\
                                     command = self.__necklace)
      self.__button_necklace.place(x=680,y=360)
  def __attack(self):
    self.__begin_combat.destroy()
    self.__lyuki1.destroy()
    self.__att_pic = PhotoImage(file = 'YukiText\\Yuki2.gif')
    self.__att = Label(self.__bg,image = self.__att_pic)
    self.__att.place(x=200,y=300)
    self.__att.image= self.__att_pic
    self.__damage = 0
    self.__damage = int(random.choice(Player.dmg))
    Yuki.currenthp -= self.__damage
    
    self.__next = Button(self.__bg,text = 'Next',command = self.__yuki_attack)
    self.__next.place(x = 680, y = 390)
    self.HUD()
  def __yuki_attack(self):
    if Yuki.currenthp > 0:
      self.__next.destroy()
      self.__att.destroy()
      self.__t2_pic = PhotoImage(file = 'YukiText\\Yuki1.gif')
      self.__t2 = Label(self.__bg,image = self.__t2_pic)
      self.__t2.place(x=200,y=300)
      self.__t2.image= self.__t2_pic
      
      self.__tdam = 0
      self.__dealdmg = int(random.choice(Yuki.damage))
      self.__tdam = self.__dealdmg
      Player.hpcurrent -= self.__tdam
      self.HUD()
      if Player.hpcurrent < 1:
        self.__att.destroy()
        self.__t5_pic = PhotoImage(file = 'YukiText\\Yuki3.gif')
        self.__t5 = Label(self.__bg,image = self.__t5_pic)
        self.__t5.place(x=200,y=300)
        self.__t5.image= self.__t5_pic
        self.__death = Button(self.__bg,text = 'Next'\
                             ,command = self.__death)
        self.__death.place(x = 680, y = 390)
      else:
        self.__turn=Button(self.__bg,text = 'Next',\
                           command = self.__attack)
        self.__turn.place(x = 680, y = 390)
        
    else:
      self.__t6_pic = PhotoImage(file = 'YukiText\\Yuki8.gif')
      self.__t6 = Label(self.__bg,image = self.__t6_pic)
      self.__t6.place(x=200,y=300)
      self.__t6.image= self.__t6_pic
      Player.hpmax += 3
      Player.golem_killed = 1
      self.__fin = Button(self.__bg,text = 'Next'\
                            ,command = self.__end)
      self.__fin.place(x = 680, y = 390)
      self.HUD()
  def __necklace(self):
    self.__begin_combat.destroy()
    self.__button_necklace.destroy()
    self.__yuki4 = PhotoImage(file = 'YukiText\\Yuki4.gif')
    self.__lyuki4 = Label(self.__bg,image = self.__yuki4)
    self.__lyuki4.place(x=200,y=300)
    self.__lyuki4.image = self.__yuki4
    self.__next = Button(self.__bg,text = 'Next'\
                            ,command = self.__stops)
    self.__next.place(x = 680, y = 390)
  def __stops(self):
    self.__lyuki4.destroy()
    self.__next.destroy()
    self.__yuki5 = PhotoImage(file = 'YukiText\\Yuki5.gif')
    self.__lyuki5 = Label(self.__bg,image = self.__yuki5)
    self.__lyuki5.place(x=200,y=300)
    self.__lyuki5.image = self.__yuki5
    self.__next2 = Button(self.__bg,text = 'Next'\
                            ,command = self.__reach)
    self.__next2.place(x = 680, y = 390)
  def __reach(self):
    self.__lyuki5.destroy()
    self.__next2.destroy()
    self.__yuki6 = PhotoImage(file = 'YukiText\\Yuki6.gif')
    self.__lyuki6 = Label(self.__bg,image = self.__yuki6)
    self.__lyuki6.place(x=200,y=300)
    self.__lyuki6.image = self.__yuki6
    self.__next3 = Button(self.__bg,text = 'Next'\
                            ,command = self.__dissp)
    self.__next3.place(x = 680, y = 390)
  def __dissp(self):
    self.__lyuki6.destroy()
    self.__next3.destroy()
    self.__yuki7 = PhotoImage(file = 'YukiText\\Yuki7.gif')
    self.__lyuki7 = Label(self.__bg,image = self.__yuki7)
    self.__lyuki7.place(x=200,y=300)
    self.__lyuki7.image = self.__yuki5
    self.__next4 = Button(self.__bg,text = 'Next'\
                            ,command = self.__end)
    self.__next4.place(x = 680, y = 390)
    
  def HUD(self):
    if hasattr(Outside,'self.__hp'):
      self.__hp.destroy()
    if hasattr(Outside,'self.__gold'):
      self.__gold.destroy()

    self.__hp = Label(self.__bg,\
                      text = 'HP %s/%s'%(Player.hpcurrent,Player.hpmax),\
                      fg = 'blue', font =('Helvetica 8 bold'))
    self.__hp.place(x = 5, y = 5)
    self.__gold = Label(self.__bg,\
                        text = 'Gold: %s'%(Player.gold),\
                        font = ('Helvetica',8))
    self.__gold.place(x = 5, y = 28)
  def __death(self):
    self.__bg.destroy()
    Death.Death()
  def __end(self):
    self.__bg.destroy()
    End.End()


