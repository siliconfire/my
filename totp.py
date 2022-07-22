import pyotp
import time
import os
####################
#     settings     #
####################

#totp kodunuzu bir alttaki satıra girin.
totp_code = "jgc5sre7eshuskuc"
#totp kodunuzu bir üstteki satıra girin.

####################
#     settings     #
####################


#code start
totp = pyotp.TOTP(totp_code)
print("----------------------------------------------------")
print("Doğrulama kodunuzu kimseyle paylaşmayınız.")
print("")
print("[KODU GORMEK ICIN ENTER BASIN]")
print("")
print("")
print("")
print("made by github.com/trashbin7")
print("----------------------------------------------------")
input("")
os.system("cls")

while True:

    print("----------------------------------------------------")
    print("Doğrulama kodunuzu kimseyle paylaşmayınız.")
    print("")
    print(totp.now() + " " + "time_remaining")      #note to myself: remove the "" before fixing
    print("(kodu yenilemek için ENTER basın.)")
    print("")
    print("")
    print("made by github.com/trashbin7")
    print("----------------------------------------------------")
    time.sleep(1)
    os.system("cls")

#code end