import os
import time
import random

yellow = [-10, -5,-3, -2, -1, 0, 1, 2, 3, 4, 5, 7, 10, 15]
yellowrandom = 0
addpoint = 0
team1 = 0
team2 = 0
ended = False
rteam = 0
nteam = 0
picked = 0
randomtime = 0
yesorno = 0

def ptext(type):
    if type == "osb":           # osb = os border == border with os.system("cls")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--------------------------------------------------")
    if type == "b":             # b = border
        print("--------------------------------------------------")
    if type == "score":         # score
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--------------------------------------------------")
        print(f"|   TAKIM 1  --->  {team1}   |   TAKIM 2  --->  {team2}   |")
    if type == "oss":           # oss = os small border = small border with os.system("clear")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-------------------------")
    if type == "s":             # s = small border
        print("-------------------------")


ptext("osb")
print("Oyuna Hoş Geldin!\n\n\n\n\n(!) Oyuna başlamak için [ENTER] tuşuna bas.\n")
ptext("b")
input()
print("Takımların hazır olduğuna emin misin?")
input()
print("bir saniye...")

rteam = random.randint(1, 2)
if rteam == 1:
    nteam = "TAKIM 1"
if rteam == 2:
    nteam = "TAKIM 2"

time.sleep(0.5)

while ended == False:
    team1 = str(team1)
    team2 = str(team2)
    ptext("score")
    print(f"\nSıradaki takım: {nteam} \n\n\n\n")
    ptext("b")
    if nteam == "TAKIM 1":
        nteam = "TAKIM 2"
    elif nteam == "TAKIM 2":
        nteam = "TAKIM 1"



    picked = input()

    if picked == "1":
        print()
        picked = input("Takım: ")
        if picked == "1":
            addpoint = input("Puan: ")
            addpoint = int(addpoint)
            team1 = int(team1)
            team1 = team1 + addpoint
        elif picked == "2":
            addpoint = input("Puan: ")
            addpoint = int(addpoint)
            team2 = int(team2)
            team2 = team2 + addpoint
    elif picked == "2":
        ptext("score")
        print("\nrastgele bir rakam seçiliyor...")
        randomtime = random.randint(2, 5)
        time.sleep(randomtime)
        yellowrandom = random.choice(yellow)
        print(f"{yellowrandom}\n\n\n")
        ptext("b")
        time.sleep(2)
        if nteam == "TAKIM 2":
            yellowrandom = int(yellowrandom)
            team1 = int(team1)
            team1 = team1 + yellowrandom
        elif nteam == "TAKIM 1":
            yellowrandom = int(yellowrandom)
            team2 = int(team2)
            team2 = team2 + yellowrandom

    elif picked == "3":
        ptext("score")
        print("\n10 yada 0...")
        randomtime = random.randint(2, 5)
        time.sleep(randomtime)
        yesorno = random.randint(0, 1)
        if yesorno == 1:
            print("10 Puan eklendi!\n\n\n")
            ptext("b")
            if nteam == "TAKIM 2":
                team1 = int(team1)
                team1 = team1 + 10
            elif nteam == "TAKIM 1":
                team2 = int(team2)
                team2 = team2 + 10
            time.sleep(2)
        elif yesorno == 0:
            print("sana bir haberim var...")
            time.sleep(1)
            print("kazanamadın :(\n\n")
            time.sleep(2)


    else:
        input("sıradaki takıma geçiliyor...")
    
    yellowrandom = 0
    picked = 0
    randomtime = 0
    yesorno = 0