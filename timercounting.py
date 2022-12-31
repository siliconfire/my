import time
import os
counter = 0
os.system('cls' if os.name == 'nt' else 'clear')
input("--------------------------------------------------\n(!) Başlamak için [ENTER] tuşuna basın.\n\nmade by github.com/TrashBin7\n--------------------------------------------------")
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"--------------------------------------------------\nbu program {counter} saniyedir çalışıyor.\n\nmade by github.com/TrashBin7\n--------------------------------------------------")
    time.sleep(0.99)
    counter = counter + 1