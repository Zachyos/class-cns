import os
os.system('cls')
import calendar
from tkinter import *
def showCalender():
    gui = Tk() #Tk is from the tkinter module
    gui.config(background='blue')
    gui.title("Zac's Calendar") # This will allow me to put the name of my tab/gui as Zac's calendar
    gui.geometry("550x600")
    year = int(year_field.get()) #This will grab me the year and put it above the calendar
    gui_content= calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Consolas 10 bold")
    calYear.grid(row=7, column=1,padx=20) #Here you can set the size of each calendar
    gui.mainloop()
 
print('Preparing Calendar....')   
#if __name__=='__main__':
new = Tk()
new.config(background='white')
new.title("Calendar") #here is where you set up the Calendar tab that opens
new.geometry("250x140") # This is the size of the tab that opens
cal = Label(new, text="Calendar",bg='white',font=("Arial", 28, "bold")) #Here you can select font and size
#Label for enter year, so here you can enter what year you want to see via calendar
year = Label(new, text="Enter the year", bg='blue', fg='white')
#text box for year input
year_field=Entry(new)
button = Button(new, text='Show Calendar',fg='white',bg='Blue',command=showCalender)
#adjusting widgets in position and setting up the tab
cal.grid(row=0, column=2) #here is where I adjust the position of the widgets
year.grid(row=1, column=2) # This is all setup on a grid
year_field.grid(row=3, column=2)
button.grid(row=4, column=2)
new.mainloop()
