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
input("(!) doğrulama kodunuzu görmek için ENTER basınız.")
os.system("cls")
print("----------------------------------------------------")
print("Mineland için doğrulama kodunuzu kimseyle paylaşmayınız.")
print("")
print(" " + totp.now())
print("")
print("made by github.com/trashbin7")
print("----------------------------------------------------")
print("")
print("")
input("(!) bir kere daha doğrulama kodu almak için ENTER basın.")
os.system("cls")
print("----------------------------------------------------")
print("Mineland için doğrulama kodunuzu kimseyle paylaşmayınız.")
print("")
print(" " + totp.now())
print("")
print("made by github.com/trashbin7")
print("----------------------------------------------------")
print("")
print("")
input("(X) çıkmak için ENTER basın.")
os.system("cls")

#code end