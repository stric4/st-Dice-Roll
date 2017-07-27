#! /usr/bin/python
#Simulates rolling one dice with user input to continue

#Module for random number
import random

print('Welcome to Dice Roller')

#Prompt user to continue
choice = input('Would you like to roll?:Y (Y/N)')

count=0

while choice == 'y' or choice == 'Y':
	print(random.randint(0,6))
	count+=1
	choice = input('Would you like to roll?:Y (Y/N)')
print('Goodbye')
print('You rolled', count, 'times.')