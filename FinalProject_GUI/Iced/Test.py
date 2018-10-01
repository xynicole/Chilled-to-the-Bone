from tkinter import *
import Intro
class Test:
  def __init__(self):
    self.__bg = Canvas(width =800,height = 445)
    self.__bg.pack()
    self.__button_tavern = Button(self.__bg,\
                                  text = 'intro',\
                                  command =self.open_intro)
    self.__button_tavern.place(x=100,y=325)

  def open_intro(self):
    self.__bg.destroy()
    Intro.Intro()

Test()
