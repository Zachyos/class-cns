from audioop import add
from fileinput import close
import os
from faulthandler import disable
from tkinter import *
import tkinter as tk
import random
from turtle import width


os.system('cls') 
RPS = tk.Tk()
RPS.geometry("750x450") # Here I am giving the GUI its dimensions, you can easily adjust these to whatever you'd like.
RPS.title("Rock, Paper, Scissors Game!") # Here I am assigning the title and background color of the GUI.
RPS.config(bg ='white')
photo = PhotoImage(file = "dad.png")  # This is the application image, "dad.png" is the name of the image I have used.
RPS.iconphoto(False, photo)
#here I actually run the command


# here I assign an array with multiple possible answers that the cpu will give while playing.
cpu_action = {
    "0":"Rock",
    "1":"Paper",
    "2":"Scissors"
}
 

# Here I assgned variables to each text, just to make my life a little easier.
win = "YOU WIN!"
lose = "You LOSE!"
tie = "You TIED"


#Here is the first function I will use, this will reset all of the buttons back to active, after being disabled.
def reset():
    rock_button["state"] = "active" 
    paper_button["state"] = "active" # [state] = active means that when the reset function is called, all of my buttons will be functionable again.
    scissor_button["state"] = "active"
    player_title.config(text = "Player        ") # This will reset the top of the screen, it will go from what was played, back to player vs cpu
    cpu_title.config(text = "CPU       ") 
    output_box.config(text = "")
 

# The disable command does exactly what its name implies
def disable():
    rock_button["state"] = "disable" 
    paper_button["state"] = "disable" # these will disable every button, except for the play again button, until a reset is queued.
    scissor_button["state"] = "disable"
 


def rock(): # This is where I will assign values to rock via function.
    c_a = cpu_action[str(random.randint(0,2))] # This will use the random import, make sure its a string, and randomize what the output will be. 
    if c_a == "Rock":               #Here I assign where to put the output for the cpus action/output
        result = tie # this is where I will determine what the cpu has and if I win lose or tie
    elif c_a == "Scissors":
        result = win
    else:
        result = lose
    output_box.config(text = result)  # Result is what will show up in the box, and will tell you if you won, lost or tied
    player_title.config(text = "Rock          ")
    cpu_title.config(text = c_a) #this is where the computers selection will be placed
    disable()
 #I then will run the disable command, so you cannot spam the buttons without clicking the replay button
 

def paper(): #Same thing here, excpet change it to paper
    c_a = cpu_action[str(random.randint(0,2))]
    if c_a == "Paper":
        result = tie
    elif c_a == "Scissors":
        result = lose
    else:
        result = win
    output_box.config(text = result)
    player_title.config(text = "Paper           ")
    cpu_title.config(text = c_a)
    disable()
 

def scissor(): # Same thing here again, except change it to scissors
    c_a = cpu_action[str(random.randint(0,2))]
    if c_a == "Scissors":
        result = tie
    elif c_a == "Rock":
        result = lose
    else:
        result = win
    output_box.config(text = result)
    player_title.config(text = "Scissors          ")
    cpu_title.config(text = c_a)
    disable()


frame = Frame(RPS)
frame.pack() #Here I switch from a grid style format for tkinter, to a pack style

header = Label(RPS, 
    text = "Rock Paper Scissors",
        font = "Century 20 bold", #Here I am starting to create the actual output onto the GUI
            fg = "blue",
                bg = "white").pack(side=TOP,pady = 20) #Here is how to adjust where your output/title is going to go


player_title = Label(frame,
    text = ("Player") + "             ",
        font = "Arial 15 bold",
            fg = "red",
                bg = "white")
 

vs_title = Label(frame,
    text = "VS             ",
        font = "Arial 15 bold",
            bg = "white")
   

cpu_title = Label(frame, 
    text = "CPU", 
        font = "Arial 15 bold",
            fg= "red",
                bg = "white")
 

player_title.pack(side = LEFT)
vs_title.pack(side = LEFT) #Here is where I adjust where the player/cpu output will be located
cpu_title.pack()
 

output_box = Label(RPS,
    text = "",
        font = "normal 20 bold",
            bg = "white",
                width = 15 ,
                    borderwidth = 1,
                        relief = "solid")
output_box.pack(pady = 20)
 

frame1 = Frame(RPS)
frame1.pack()
frame1.config(bg ='white')

# THis is where I will start to create my buttons inside my GUI
rock_button = Button(frame1, 
    text = "Rock",
        font = "Century 15",  #You make them just like text, excpet you use the button object instead of a label object.
            width = 8,
                fg = "red",
                    bg = "white",
                        command = rock) #Here I call the rock object, and call it a command, so every time the button is pressed it will call the function.
         
 
paper_button = Button(frame1, 
    text = "Paper ",
        font = "Century 15", 
            width = 8,
                fg = "red",
                    bg = "white",
                        command = paper)
           
 
scissor_button = Button(frame1, 
    text = "Scissors",
        font = "Century 15", 
            width = 8,
                fg = "red",
                    bg = "white",
                        command = scissor)
           
 
rock_button.pack(side = LEFT, padx = 10)
paper_button.pack(side = LEFT,padx = 10) # Here is where I assign the locations of the buttons, again no longer using a grid format.
scissor_button.pack(padx = 10)
 
frame2 = Frame(RPS) 
frame2.pack(fill=BOTH)
frame2.config(bg="white")


#here is where I set up the image that I will use for the Play again button
img = PhotoImage(file ='the.png') # the.png is the name of the image
img_button = Label(image=img)
#image is a built in object with tkinter, and I use it here to actually format it into the code

#This is the final button, the play again button
play_again = Button(frame2, image=img, #Here I added an image for the button, and it covers the text just below.
    text = "Play Again", 
        font = 10,
            fg = "white", #Here is where I adjust what the outline of the button will look like, even though you wont see it
                bg = "blue",
                    command = reset) #The reset command, will perform the function at line 53
play_again.pack(side = BOTTOM, padx= 20, pady=20)
 # Here is where I adjust the location of the button.


RPS.mainloop()
 # This is the loop that will create the GUI
