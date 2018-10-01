
from tkinter import *
import sys
import random
import re



class guess_GUI:
   
  def __init__(self):
    self.__win = Tk()
    self.__win.title('Guess Number!')
    self.__toplabel = Label (self.__win, text = \
                             'Enter any number from 0 to 50! ')
    self.__toplabel.grid(row=0, column=2)
    self.right_num = random.randint(0, 50)
  
    self.times = 0

#tip label
    self.__tip_status  = StringVar()
    self.__tip_status.set("")
    self.__lab_tip = Label(self.__win, textvariable = self.__tip_status)
    self.__lab_tip.grid(row =1, column=2)
    

#min num
    self.__min_label = Label(self.__win, text = 'Min:')                         
    self.__min_label.grid(row=3, column=1)
    self.__min_status = StringVar()
    self.__min_status.set("0")
    self.__lab_minsta = Label(self.__win, textvariable = self.__min_status)
    self.__lab_minsta.grid(row=4, column=1)

#max num
    self.__max_label = Label(self.__win, text = 'Max:')
    self.__max_label.grid(row=3, column=3)
    self.__max_status = StringVar()
    self.__max_status.set("50")
    self.__lab_maxsta = Label(self.__win, textvariable = self.__max_status)
    self.__lab_maxsta.grid(row=4, column=3)
    

#entry num box
    self.__num_entry = Entry(self.__win, width = 10)
    self.__num_entry.grid(row=3, column=2)
    self.__num_entry.bind('<Return>', self.get_input)
    
#guess button
    self.__button_guess = Button(self.__win, text = "Guess", \
                                 command = self.get_guess)
    self.__button_guess.grid(row=5, column=2)
    

# message
    self.__message = StringVar()
    self.__message.set('')
    self.__lab_message = Label(self.__win, textvariable = self.__message)
    self.__lab_message.grid(row=6, column=2)

#close button
    self.__button_close = Button(self.__win, text = 'Quit', \
                                 command = self.__win.destroy)
    self.__button_close.grid(row=7, column=2)


    mainloop()

  def get_input(self):
    return int(self.__num_entry.get())
  def get_tips(self):
    return(self.__tip_status)
  def get_result(self):
    return(self.__message)



  def get_guess(self):
    if self.get_input() in range(0,51):
      if self.get_input() == self.right_num:
        self.times +=1
        self.__tip_status.set('Congratulations!')
        self.__message.set(self.get_message())
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
      return 'Awesome!'
    elif self.times < 10:
      return 'Good Job! Times you tried: ' +str(self.times)
    elif self.times< 20:
      return 'Nice! Times you tried: ' +str(self.times)
    else:
      return 'Ok.. You have already tried more than 20 times.' \
               'Times you tried: ' +str(self.times)



guess_GUI()
    
