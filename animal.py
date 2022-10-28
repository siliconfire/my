import pyautogui as pg
import time

counter = 0
print("yükleniyor...")
txt = ["Canidae",
    "Felidae",
    "Cat",
    "Cattle",
    "Dog",
    "Donkey",
    "Goat",
    "Guinea pig",
    "Horse",
    "Pig",
    "Rabbit",
    "Fancy rat varieties",
    "laboratory rat strains",
    "Sheep breeds",
    "Water buffalo breeds",
    "Chicken breeds",
    "Duck breeds",
    "Goose breeds"
]
time.sleep(0.1)
print("yüklendi.")
print("")
time.sleep(0.1)
print("(!) Çıkmak için ctrl+c basın.")
print("")
time.sleep(0.1)

name = input("isim girin: ")
time.sleep(0.1)
print("")
counter = input("kaç kere yazılsın: ")
time.sleep(0.1)
print("birazdan başlayacak...")
time.sleep(7.5)

while True:
    pg.write(str(name) + " Tam bir " + str(txt[counter]) + ".")
    pg.press("enter")
    print("Kalan: " + str(counter))
    counter = counter - 1
    time.sleep(0.5)
    if counter < 1:
        break
