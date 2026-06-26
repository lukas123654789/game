from player import Player
from monster import *
import random



player_name = input("Enter your name: ")

monster1 = Danko()
monster2 = Vlado()
monster3 = Stefan()
monster4 = Klad()
monster5 = SorbyBarber()

player1 = Player(player_name)
monsters = [monster1, monster2, monster3, monster4]
enemy = monsters[random.randint(0,3)]
gane_on = True
while gane_on:
    break

print(enemy.ability)