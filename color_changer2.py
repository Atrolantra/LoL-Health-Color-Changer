#The League OF Legends Health Bar Color Changer
#By Eric Briese

#Todo:
#Add ability to change health and mana of allies, self and enemies on normal or colorblind. (And maybe other things)
#Set it out better. (Will be necessary if more functionality is added.)
#Possibly find a way to change the rgb printed text color when on a dark background.
#Devise a more elegant way for the program to find the necessary line to edit. 
#More comments.

import os
from re import *
from Tkinter import *
from tkMessageBox import *
from tkColorChooser import askcolor              
from tkFileDialog   import askopenfilename
from tkFileDialog   import askdirectory
import tkMessageBox as box
root = Tk()
root.title("League Health Color Changer")
#The color selection function.
def callback():
    global rgb
    (rgb, hx) = askcolor()
    e2.config(bg=hx)
    if rgb:
        d2.set(rgb)
#The directory selection function.
def browser():
    global dir1
    dir1 = askdirectory(initialdir="C:/")
    if dir1:
        d1.set(dir1)

#The part where it all comes together.
def apply_color():
    try:
        red = str(rgb[0])
        green = str(rgb[1])
        blue = str(rgb [2])
        address = ["C:/Riot Games", "/League of Legends", "/RADS", "/solutions", "/lol_game_client_sln", "/releases/"]
        for _ in range(5):
            if dir1 == "".join(address[0:_]):
                league_path = dir1 + "".join(address[_:7])
                break
        for subdirname in os.listdir(league_path):
            release = subdirname
        league_path = league_path + str(release) + "/deploy/DATA/menu/hud/"
        print "The League of Legends path is " + league_path
        for filename in os.listdir(league_path):
            if filename == "GeneralCharacterData.ini":
                with open(league_path + "GeneralCharacterData.ini", "r") as file:
                    data = file.readlines()
                champ_health = data.index("[HealthBarChampionSelfDefault]\n")

                data[champ_health + 6] = "HealthBarColor =" + red + " " + green + " " + blue + " " + "255\n"
                with open(league_path + "GeneralCharacterData.ini", "w") as file:
                    file.writelines( data )
                box.showinfo("Success", "Your changes have been saved.\nYour new color has been updated into line: \n" + data[champ_health + 6])
    except BaseException:
        return box.showerror("Error", "An error has occured. \nPlease make sure a color is selected \nand that the correct directory has been chosen.")

#Some Tkinter stuff.        
d1 = StringVar()
d2 = StringVar()
e1 = Entry(root, textvariable=d1, width = 40) 
e1.pack(fill=X) 
e2 = Entry(root, textvariable=d2, width = 40) 
e2.pack(fill=X) 



b1 = Button(root, text="Browse", command=browser, width = 40)
b1.pack(fill=X)


b2 = Button(text="Chose Color", command=callback, width = 40)
b2.pack(fill=X)

b3 = Button(text="Apply", command=apply_color, width = 40)
b3.pack(fill=X)

l = Label(text=
'''Welcome to the color changer.
Simply select your League Of Legends directory
Eg, C:\Riot Games
And the color you want.
''')
l.pack()
c = Canvas(root, height=100, width=200)
c.pack()

mainloop()






