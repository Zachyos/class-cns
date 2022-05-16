import os
from re import A
os.system('cls')

print("Your Name: ")
name = input("")

input("\n\nPress the {enter key}")

import random

print("your cards: ")
card1 = random.randint(1, 12)
card2 = random.randint(1, 12)
player_cards = card1, card2
print(player_cards)

table1 = random.randint(1, 12)
table2 = random.randint(1, 12)
table3 = random.randint(1, 12)
table_full = table1, table2, table3
print("the first table cards are:")
print(table_full)

print("put in the amount you would like to bet")
bet1 = input("")

table4 = random.randint(1, 12)
print("full table is now: ")
table = table1, table2, table3, table4
print(table)

print("put in the amount you would like to bet")
bet2 = input("")

table5 = random.randint(1, 12)
print("full table is now: ")
table12345 = table1, table2, table3, table4, table5
print(table12345)

print("player2 had: ")
card12 = random.randint(1, 12,)
card22 = random.randint(1, 12,)
player2 = card12, card22
print(player2)

print("this is the full table now")
print(player_cards)
print(table12345)
print(player2)


play = input("do you want to play again")
if play == "yes":
    exec(open("./pokerface.py").read())
else:
        exit()