import time
import os
counter = 0
loop = 1
os.system('cls' if os.name == 'nt' else 'clear')
while loop == 1:
	print(f"--------------------------------------------------\nYour counter is at {counter}.\n\nType a number to add.\nType 0 to reset.\nType exit to leave.\n\ngithub.com/TrashBin7\n--------------------------------------------------")
	print("\n")
	add = input()
	os.system('cls' if os.name == 'nt' else 'clear')
	if add == "0":
		counter = 0
	elif add == "easteregg":
		print("github.com/TrashBin7")
		print()
		print("(!) going to the main menu in 3 seconds...")
		time.sleep(3)
	elif add == "exit":
		print("Goodbye | Made by github.com/TrashBin7")
		print()
		print("(!) Going to exit in 3 seconds...")
		time.sleep(3)
		loop = 0
	elif add == "":
		print("empty text, ignoring...")
		time.sleep(1)
	else:
		add = int(add)
		counter = counter + add
		add = 0
	os.system('cls' if os.name == 'nt' else 'clear')