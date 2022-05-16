"# class-cns" 


import os
os.system('cls')

from tkinter import *

from colored import fg, bg, attr
import runpy

def menu_choice():

  def print_menu():  
  
      print('%s%s ------------  Menu  ------------ %s' % (fg(231), bg(92), attr(4)))
        print('%s%s1. Covert minutes to seconds %s' % (fg(92), bg(231), attr(4)))
        print("%s%s2. Calander %s" % (fg(92), bg(231), attr(4)))
        print("%s%s3. How long have you been alive? %s" % (fg(92), bg(231), attr(4)))
        print("%s%s4. Convert Tempature%s" % (fg(92), bg(231), attr(4)))
      
      print("%s%s5. Next Page  %s" % (fg(92), bg(231), attr(4)))
        print("%s%s6. Exit  %s" % (fg(92), bg(231), attr(0)))
        print("%s%s -------------------------------- %s" % (fg(231), bg(92), attr(1)))
    loop = True
    int_choice = -1
    
    while loop:          # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        choice = input("%s%sEnter your choice! [1-6]: %s" % (fg(11), bg(0), attr(1)))
        


        if choice == '1':
            print (" Here is how old you are: ")
            runpy.run_path("Time.py")
            while len(choice) == 0:
             loop = False


        elif choice == '2':
            print (" Calander : ")
            runpy.run_path("RPS.py")
            while len(choice) == 0:
             loop = False


        elif choice == '3':
            print (" How long have you been alive? : ")
            runpy.run_path("Date and Time.py")
            while len(choice) == 0:
             loop = False


        elif choice == '4':
            print (" Converting Celcius to Fahrenheit: ")
            runpy.run_path("F to C.py")
            while len(choice) == 0:
             loop = False 

        elif choice == '5':
            print('Next Page')
            runpy.run_path("Page 2.py")

        elif choice == '6':
            print("Exiting")
            loop=False  # This will end the loop

        else:
            # else will give an error message if the wrong input is entered
            input("Wrong menu selection. ")
    return [int_choice, choice]


print(menu_choice())

import os
os.system('cls')
from tkinter import *
from colored import fg, bg, attr

 #this is a clear-host command, yes in python
import runpy

def menu_choice():
    
    def print_menu():       # the menu itself
        
        print('%s%s ------------  Menu Pg2  ------------ %s' % (fg(231), bg(92), attr(4)))
        print('%s%s1. Create a Log File %s' % (fg(92), bg(231), attr(4)))
        print("%s%s2. Tik Tac Toe %s" % (fg(92), bg(231), attr(4)))
        print("%s%s3. GUI Calender %s" % (fg(92), bg(231), attr(4)))
        print("%s%s4. Password Generator %s" % (fg(92), bg(231), attr(4)))
        print("%s%s5. 5 %s" % (fg(92), bg(231), attr(4)))
        print("%s%s6. << Go Back  %s" % (fg(92), bg(231), attr(0)))
        print("%s%s ------------------------------------ %s" % (fg(231), bg(92), attr(1)))

    loop = True
    int_choice = -1

    while loop:          # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        choice = input("%s%sEnter your choice! [1-6]: %s" % (fg(11), bg(0), attr(0)))
        


        if choice == '1':
            print (" Creating a Log File: ")
            runpy.run_path("Log File.py")
            while len(choice) == 0:
             loop = False


        elif choice == '2':
            print (" Playing Tic Tac Toe : ")
            runpy.run_path("tictactoe.py")
            while len(choice) == 0:
             loop = False


        elif choice == '3':
            print ("Upgrading Calender : ")
            runpy.run_path("GUI Calender.py")
            while len(choice) == 0:
             loop = False


        elif choice == '4':
            print (" Password Generator: ")
            runpy.run_path("Random Password.py")
            while len(choice) == 0:
             loop = False 

        elif choice == '5':
            print('Next Page')
            runpy.run_path("")

        elif choice == '6':
            print("Exiting")
            loop = False  # This will end the loop

        else:
            # else will give an error message if the wrong input is entered
            input("Wrong menu selection. ")
    return [int_choice, choice]


print(menu_choice())
