from tkinter import *
from Player import *
import West
import Courtyard
import Outside

class Greenhouse:
  def __init__(self):
    self.__bg = Canvas(width =800,height = 445)
    self.__bg.pack()
    self.__foyer_pic = PhotoImage(file = 'Bg\\greenhouse.gif')
    self.__bg.create_image(0,0,image = self.__foyer_pic,anchor=NW)
    self.__bg.image = self.__foyer_pic

    self.__bcourtyard = Button(self.__bg,text = 'Courtyard',\
                               command = self.__courtyard)
    self.__bcourtyard.place(x=650,y=250)
    self.__return= Button(self.__bg,text ='Return to Library',\
                          command = self.__leave)
    self.__return.place(x=390,y=400)

    self.__bdark = Button(self.__bg,text = 'Outside',\
                          command = self.__dark)
    self.__bdark.place(x=150,y=240)

  def __courtyard(self):
    if Player.key_have == 0:
      self.__lock =PhotoImage(file = 'CTexts\\Locked.gif')
      self.__llock = Label(self.__bg,image = self.__lock)
      self.__llock.place(x=210,y=310)
      self.__llock.image = self.__lock
      self.__next = Button(self.__bg,text='Back',command = self.__back)
      self.__next.place(x=680,y=400)
    if Player.key_have == 1:
      self.__unlock =PhotoImage(file = 'CTexts\\Unlock.gif')
      self.__lunlock = Label(self.__bg,image = self.__unlock)
      self.__lunlock.place(x=210,y=310)
      self.__lunlock.image = self.__unlock
      self.__next = Button(self.__bg,text='Back',command = self.__cy)
      self.__next.place(x=680,y=400)
  def __cy(self):
    self.__bg.destroy()
    Courtyard.Courtyard()
  def __leave(self):
    self.__bg.destroy()
    West.West()
  def __dark(self):
    self.__bg.destroy()
    Outside.Outside()
  def __back(self):
    self.__llock.destroy()
    self.__next.destroy()

