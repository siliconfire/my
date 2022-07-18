import time
while True:
    print("YOUTUBE SIMULATOR")
    print("1. search a video")
    print("2. edit video")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("searching a video")
        time.sleep(2)
        print("video found")
        time.sleep(2)
        print("video loaded")
        time.sleep(2)
        print("video playing")
        time.sleep(2)
        print("video paused")
        time.sleep(2)
        print("video resumed")
        time.sleep(2)
        print("video stopped")
        time.sleep(2)
        print("video closed")
    elif choice == 2:
        print("editing a video")
        time.sleep(2)
        print("video edited")
        time.sleep(2)
        print("video closed")
    