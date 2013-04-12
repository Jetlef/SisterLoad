#!/usr/bin/env python

import os

def clear():
	if os.name == "posix": os.system("clear")
	else: os.system("cls")

command = raw_input("SisterLoad~ ")
while command != "exit":
	print "HUD GOES HERE"
	print "*"*22*80
	command = raw_input("SisterLoad~ ")
	clear()