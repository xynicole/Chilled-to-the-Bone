
from tkinter import *
import sys
import random
import re
from Player import *
import Tavern



#CONSTANTS
NUMBER = random.randint(0,50)
NUM = 0
NUM_MAX = 50
NUM_MIN = 0


class Guess:
   
  def __init__(self):
    self.__bg = Canvas(width =800,height = 445)
    self.__bg.pack()
    self.__gam_pic = PhotoImage(file = 'Bg\\wood.gif')
    self.__bg.create_image(0,0,image = self.__gam_pic,anchor=NW)
    self.__bg.image = self.__gam_pic
    self.HUD()
    self.right_num = random.randint(0, 50)
    self.__guess = Label('')
    self.__next1 = Button('')
    self.__i = 1
    self.times = 0
    self.__message = ''
    self.__gnog()
    
    
  def __gnog(self):
    if Player.gold >25:
      self.__next()
    else:
      self.__nogold = PhotoImage(file = 'GuessText\\NoGold.gif')
      self.__lnogold = Label(self.__bg,image = self.__nogold)
      self.__lnogold.place(x=200,y=300)
      self.__lnogold.image = self.__nogold
      self.__bleave = Button(self.__bg,text = 'Leave',command= self.__leave)
      self.__bleave.place(x=630,y=390)
             
    
  def __next(self):
    while self.__i < 6:
      self.__next1.destroy()
      self.__guess.destroy()
      self.__guess1 = PhotoImage(file = 'GuessText\\Guess%s.gif'%(self.__i))
      self.__guess = Label(self.__bg, image = self.__guess1)
      self.__guess.place(x=200,y=300)
      self.__guess.image = self.__guess1
      self.__dialogue()
      break
    else:
      self.__guess.destroy()
      self.__next1.destroy()
      self.__play = Button(self.__bg,  text = 'Play',\
                           command = self.__play)
      self.__play.place(x=630,y=300)
      self.__bleave = Button(self.__bg,text = 'Leave',command= self.__leave)
      self.__bleave.place(x=630,y=390)
  def __dialogue(self):
    
    self.__i += 1
    self.__next1 = Button(self.__bg, text = 'Next', command = self.__next)
    self.__next1.place(x = 630, y = 340)
    
  def __play(self):
    self.HUD()
    self.__play.destroy()
    self.__bleave.destroy()
    self.__tip_status  = StringVar()
    self.__tip_status.set('')
    self.__lab_tip = Label(self.__bg, textvariable = self.__tip_status)
    self.__lab_tip.place(x=390,y=175)
    

#min num
    self.__min_label = Label(self.__bg, text = 'Min:')                         
    self.__min_label.place(x=200, y=200)
    self.__min_status = StringVar()
    self.__min_status.set("0")
    self.__lab_minsta = Label(self.__bg, textvariable = self.__min_status)
    self.__lab_minsta.place(x=230,y=200)

#max num
    self.__max_label = Label(self.__bg, text = 'Max:')
    self.__max_label.place(x=550,y=200)
    self.__max_status = StringVar()
    self.__max_status.set("50")
    self.__lab_maxsta = Label(self.__bg, textvariable = self.__max_status)
    self.__lab_maxsta.place(x=580,y=200)
    

#entry num box
    self.__num_entry = Entry(self.__bg, width = 10)
    self.__num_entry.place(x=390,y=250)
    self.__num_entry.bind('<Return>', self.get_input)
    
#guess button
    self.__button_guess = Button(self.__bg, text = "Guess", \
                                 command = self.get_guess)
    self.__button_guess.place(x=390, y=270)
    

# message


#close button
##    self.__button_close = Button(self.__bg, text = 'Quit', \
##                                 command = self.__bg.destroy)
##    self.__button_close.place(row=7, column=2)


  def get_input(self):
    return int(self.__num_entry.get())
  def get_tips(self):
    return(self.__tip_status)




  def get_guess(self):
    if self.get_input() in range(0,51):
      if self.get_input() == self.right_num:
        self.times +=1
        self.__tip_status.set('Congratulations!')
        self.get_message()
        self.__num_entry.delete(0,END)
      elif self.get_input() < self.right_num:
        self.__min_status.set(str(self.get_input()))
        self.times +=1
        self.__tip_status.set('Too small')
        self.__num_entry.delete(0,END)
      elif self.get_input() > self.right_num:
        self.__max_status.set(str(self.get_input()))
        self.times +=1
        self.__tip_status.set('Too large')
        self.__num_entry.delete(0,END)
    else:
        self.__tip_status.set('Wrong number, please enter correct number')
        self.__num_entry.delete(0,END)
      
              

    
  def get_message(self):
    if self.times == 1:
      self.__button_guess.destroy()
      self.__onetry = PhotoImage(file = 'GuessText\\Oneguess.gif')
      self.__lonetry = Label(self.__bg,image = self.__onetry)
      self.__lonetry.place(x=200,y=300)
      self.__lonetry.image = self.__onetry
      Player.gold += 100
      self.__bleave = Button(self.__bg,text = 'Leave',command= self.__leave)
      self.__bleave.place(x=630,y=390)
      self.HUD()
    elif self.times < 6:
      self.__button_guess.destroy()
      self.__fivetry = PhotoImage(file = 'GuessText\\Reward1.gif')
      self.__lfivetry = Label(self.__bg,image = self.__fivetry)
      self.__lfivetry.place(x=200,y=300)
      self.__lfivetry.image = self.__fivetry
      Player.gold += 25
      self.__bleave = Button(self.__bg,text = 'Leave',command= self.__leave)
      self.__bleave.place(x=630,y=390)
      self.HUD()
    elif self.times < 8:
      self.__button_guess.destroy()
      self.__sevtry = PhotoImage(file = 'GuessText\\None1.gif')
      self.__lsevtry = Label(self.__bg,image = self.__sevtry)
      self.__lsevtry.place(x=200,y=300)
      self.__lsevtry.image = self.__sevtry
      self.__bleave = Button(self.__bg,text = 'Leave',command= self.__leave)
      self.__bleave.place(x=630,y=390)
      self.HUD()
    else:
      self.__button_guess.destroy()
      self.__losetry = PhotoImage(file = 'GuessText\\Lose1.gif')
      self.__llosetry = Label(self.__bg,image = self.__losetry)
      self.__llosetry.place(x=200,y=300)
      self.__llosetry.image = self.__losetry
      Player.gold -= 25
      self.__bleave = Button(self.__bg,text = 'Leave',command= self.__leave)
      self.__bleave.place(x=630,y=390)
      self.HUD()
      
    

  def __leave(self):
    self.__bg.destroy()
    Tavern.Tavern()
  def HUD(self):
    if hasattr(Guess,'self.__gold'):
      self.__gold.destroy()

    self.__gold = Label(self.__bg,\
                        text = 'Gold: %s'%(Player.gold),\
                        font = ('Helvetica',15))
    self.__gold.place(x = 5, y = 28)




