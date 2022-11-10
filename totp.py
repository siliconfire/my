import datetime
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
# end of settings  #
####################


#code start
totp = pyotp.TOTP(totp_code)
print("clearing screen...")
time.sleep(0.2)
os.system('cls' if os.name == 'nt' else 'clear')
print("----------------------------------------------------")
print("Doğrulama kodunuz:")
print("")
print("")
print("XXXXXX (X)")
print("(!) Doğrulama kodunuzu görmek için ENTER basın.")
print("")
print("made by github.com/trashbin7")
print("----------------------------------------------------")
input("")
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    totp = pyotp.TOTP(totp_code)
    time_remaining = totp.interval - datetime.datetime.now().timestamp() % totp.interval
    rtime_remaining = round(time_remaining)
    print("----------------------------------------------------")
    print("Doğrulama kodunuz:")
    print("")
    print("")
    print(totp.now() + " ("+ str(rtime_remaining) +")")
    print("(X) Çıkmak için CTRL+C basın.")
    print("")
    print("made by github.com/trashbin7")
    print("----------------------------------------------------")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

#code end