from tkinter import *
import Town
from Player import *
class Shop:
  def __init__(self):
    
    self.__bg = Canvas(width =800,height = 445)
    self.__bg.pack()
    self.__shop_pic = PhotoImage(file = 'Bg\\shop.gif')
    self.__bg.create_image(0,0,image = self.__shop_pic,anchor=NW)
    self.__bg.image = self.__shop_pic
#   HUD
    self.HUD()

    self.__return_town = Button(self.__bg, text = 'Return to Town',\
                                command = self.__return_town)
    self.__return_town.place(x=650,y=300)
#   Text
    self.__shop1 = PhotoImage(file = 'ShopText\\Shop1.gif')
    self.__greet = Label(self.__bg, image = self.__shop1)
    self.__greet.place(x=200,y=300)
    self.__greet.image = self.__shop1
#   Weap/Armor
    self.__weap_label = Label(self.__bg, text = 'Weapons',\
                             font = 'Times 10 bold',bg='light slate gray')
    self.__weap_label.place(x = 250, y = 25)
    
    self.__bdagger = Button(self.__bg, text = 'Dagger 50g',\
                            command = self.__dagger,bg='thistle4')
    self.__bdagger.place(x = 250, y = 50)

    self.__bshortsword =Button(self.__bg, text = 'Shortsword 100g',\
                               command = self.__shortsword,bg = 'green4')
    self.__bshortsword.place(x= 250, y = 80)

    self.__blsword = Button(self.__bg, text = 'Longsword 150g',\
                            command = self.__lsword,bg='DeepSkyBlue2')
    self.__blsword.place(x = 250, y = 110)

    self.__bmsword = Button(self.__bg, text = 'Meteorite Sword 200g',\
                            command = self.__msword,bg='DarkOrchid3')
    self.__bmsword.place(x = 250, y = 140)
    
    self.__arm_label = Label(self.__bg, text = 'Armor',\
                             font = 'Times 10 bold', bg = 'light slate gray')
    self.__arm_label.place(x = 400, y = 25)

    self.__bleather = Button(self.__bg, text = 'Leather Armor 50g',\
                             command = self.__leather,bg = 'thistle4')
    self.__bleather.place(x=400, y = 50)

    self.__bmail = Button(self.__bg, text = 'Chainmail 100g',\
                          command = self.__chainmail,bg = 'green4')
    self.__bmail.place(x=400, y = 80)

    self.__bplate = Button(self.__bg, text = 'Platemail 150g',\
                           command = self.__plate,bg='DarkOrchid3')
    self.__bplate.place(x = 400, y = 110)
    
    if Player.dmg[0] == '2':
      self.__bdagger.configure(state = 'disabled')
    if Player.dmg[0] == '3':
      self.__bdagger.configure(state = 'disabled')
      self.__bshortsword.configure(state = 'disabled')
    if Player.dmg[0] == '5':
      self.__bdagger.configure(state = 'disabled')
      self.__bshortsword.configure(state = 'disabled')
      self.__blsword.configure(state = 'disabled')
    if Player.dmg[0] == '9':
      self.__bdagger.configure(state = 'disabled')
      self.__bshortsword.configure(state = 'disabled')
      self.__blsword.configure(state = 'disabled')
      self.__bmsword.configure(state = 'disabled')

    
    if Player.hpmax == 13:
      self.__bleather.configure(state = 'disabled')
    if Player.hpmax == 15:
      self.__bleather.configure(state = 'disabled')
      self.__bmail.configure(state = 'disabled')
    if Player.hpmax == 20:
      self.__bleather.configure(state = 'disabled')
      self.__bmail.configure(state = 'disabled')
      self.__bplate.configure(state = 'disabled')
      
    
    
    mainloop()

  def HUD(self):
    if hasattr(Shop,'self.__hp'):
      self.__hp.destroy()
    if hasattr(Shop,'self.__gold'):
      self.__gold.destroy()

    
    self.__hp = Label(self.__bg,\
                      text = 'HP %s/%s'%(Player.hpcurrent,Player.hpmax),\
                      fg = 'blue', font =('Helvetica',8))
    self.__hp.place(x = 5, y = 5)
    self.__gold = Label(self.__bg,\
                        text = 'Gold: %s'%(Player.gold),\
                        font = ('Helvetica',8))
    self.__gold.place(x = 5, y = 28)



  def __dagger(self):
    if Player.gold < 50:
      self.__greet.destroy()
      self.__lowgold = PhotoImage(file = 'ShopText\\Shop3.gif')
      self.__low1 = Label(self.__bg, image = self.__lowgold)
      self.__low1.place(x=200,y=300)
      self.__low1.image = self.__lowgold
    else:
      self.__greet.destroy()
      self.__shop2 = PhotoImage(file = 'ShopText\\Shop2.gif')
      self.__bought = Label(self.__bg, image = self.__shop2)
      self.__bought.place(x=200,y=300)
      self.__bought.image = self.__shop2
      Player.gold = Player.gold - 50
      self.__bdagger.configure(state = 'disabled')
      Player.dmg = [2,3,4]
      self.HUD()
      
      
  def __shortsword(self):
    if Player.gold < 100:
      self.__greet.destroy()
      self.__lowgold = PhotoImage(file = 'ShopText\\Shop3.gif')
      self.__low1 = Label(self.__bg, image = self.__lowgold)
      self.__low1.place(x=200,y=300)
      self.__low1.image = self.__lowgold
    else:
      self.__greet.destroy()
      self.__shop2 = PhotoImage(file = 'ShopText\\Shop2.gif')
      self.__bought = Label(self.__bg, image = self.__shop2)
      self.__bought.place(x=200,y=300)
      self.__bought.image = self.__shop2
      Player.gold = Player.gold - 100
      self.__bshortsword.configure(state = 'disabled')
      Player.dmg = [3,4,5,6]
      self.HUD()
      
  def __lsword(self):
    if Player.gold < 150:
      self.__greet.destroy()
      self.__lowgold = PhotoImage(file = 'ShopText\\Shop3.gif')
      self.__low1 = Label(self.__bg, image = self.__lowgold)
      self.__low1.place(x=200,y=300)
      self.__low1.image = self.__lowgold
    else:
      self.__greet.destroy()
      self.__shop2 = PhotoImage(file = 'ShopText\\Shop2.gif')
      self.__bought = Label(self.__bg, image = self.__shop2)
      self.__bought.place(x=200,y=300)
      self.__bought.image = self.__shop2
      Player.gold = Player.gold - 150
      self.__blsword.configure(state = 'disabled')
      Player.dmg = [5,6,7,8]
      self.HUD()
      
  def __msword(self):
    if Player.gold < 200:
      self.__greet.destroy()
      self.__lowgold = PhotoImage(file = 'ShopText\\Shop3.gif')
      self.__low1 = Label(self.__bg, image = self.__lowgold)
      self.__low1.place(x=200,y=300)
      self.__low1.image = self.__lowgold
    else:
      self.__greet.destroy()
      self.__shop2 = PhotoImage(file = 'ShopText\\Shop2.gif')
      self.__bought = Label(self.__bg, image = self.__shop2)
      self.__bought.place(x=200,y=300)
      self.__bought.image = self.__shop2
      Player.gold = Player.gold - 200
      self.__bmsword.configure(state = 'disabled')
      Player.dmg = [9,10,11]
      self.HUD()
      
  def __leather(self):
    if Player.gold < 50:
      self.__greet.destroy()
      self.__lowgold = PhotoImage(file = 'ShopText\\Shop3.gif')
      self.__low1 = Label(self.__bg, image = self.__lowgold)
      self.__low1.place(x=200,y=300)
      self.__low1.image = self.__lowgold
    else:
      self.__greet.destroy()
      self.__shop2 = PhotoImage(file = 'ShopText\\Shop2.gif')
      self.__bought = Label(self.__bg, image = self.__shop2)
      self.__bought.place(x=200,y=300)
      self.__bought.image = self.__shop2
      Player.gold = Player.gold - 50
      self.__bleather.configure(state = 'disabled')
      Player.hpmax = 13
      Player.hpcurrent = 13
      self.HUD()
      
  def __chainmail(self):
    if Player.gold < 100:
      self.__greet.destroy()
      self.__lowgold = PhotoImage(file = 'ShopText\\Shop3.gif')
      self.__low1 = Label(self.__bg, image = self.__lowgold)
      self.__low1.place(x=200,y=300)
      self.__low1.image = self.__lowgold
    else:
      self.__greet.destroy()
      self.__shop2 = PhotoImage(file = 'ShopText\\Shop2.gif')
      self.__bought = Label(self.__bg, image = self.__shop2)
      self.__bought.place(x=200,y=300)
      self.__bought.image = self.__shop2
      Player.gold = Player.gold - 100
      self.__bmail.configure(state = 'disabled')
      Player.hpmax = 15
      Player.hpcurrent = 15
      self.HUD()
      
  def __plate(self):
    if Player.gold < 150:
      self.__greet.destroy()
      self.__lowgold = PhotoImage(file = 'ShopText\\Shop3.gif')
      self.__low1 = Label(self.__bg, image = self.__lowgold)
      self.__low1.place(x=200,y=300)
      self.__low1.image = self.__lowgold
    else:
      self.__greet.destroy()
      self.__shop2 = PhotoImage(file = 'ShopText\\Shop2.gif')
      self.__bought = Label(self.__bg, image = self.__shop2)
      self.__bought.place(x=200,y=300)
      self.__bought.image = self.__shop2
      Player.gold = Player.gold - 150
      self.__bplate.configure(state = 'disabled')
      Player.hpmax = 20
      Player.hpcurrent = 20
      self.HUD()
      
  def __return_town(self):
    self.__bg.destroy()
    Town.Town()




