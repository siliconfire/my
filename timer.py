# imports - do not touch

import time     # Import time module for sleep function to delay the program execution.
import sys      # Import sys module for exit function.

# end of imports

##################################################
#   welcome to pomodoro timer!                   #
#   this is a simple timer that will count down  #
#  and give you break times.                     #
#                                                #
#   github.com/trashbin7                         #
##################################################

##########################
# settings for the timer #
##########################
    
# how long should the timer be? (default: 25 minutes)
timer_duration = 25
# how long should the timer wait between each working thing? (default: 5 minutes)
timer_break = 5
# how many times should the timer be repeated? (default: 4)
timer_repeats = 2

# note: the times are in minutes.

##########################
#    end of settings     #
##########################

print("------------------------------------------------------") # welcome message
print("Welcome to the pomodoro timer!")     
print("this timer will count down and give you break times so you can focus on your work.") 
print("you can set the timer duration and break times in the settings section.") 
print("------------------------------------------------------") #welcome message end
print("")
print("")
print("")
input("(!) Press ENTER to start timer...")        # press enter to start timer
print("")
print("")
print("(!) you can fullscreen this window by pressing F11")
print("")
print("loading...")     # timer going to start in 5 seconds
timer_duration = timer_duration * 60
oldtimer_duration = timer_duration
timer_break = timer_break * 60
oldtimer_break = timer_break
oldtimer_repeats = timer_repeats
print("loaded.")
print("")
print("(!) Timer will start in 5 seconds...")
time.sleep(5)
while timer_repeats > 0:
    while timer_duration > 0:
        print(f"{timer_duration} seconds left.")
        timer_duration = timer_duration - 1
        time.sleep(1)
    timer_duration = oldtimer_duration
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("It's time for a break!")
    print("")
    print("")
    input("(!) Press ENTER to start break...")
    while timer_break > 0:
        print(f"{timer_break} seconds left.")
        timer_break = timer_break - 1
        time.sleep(1)
    timer_break = oldtimer_break
    print("")
    print("")
    input("(!) Press ENTER to continue...")
    print("")
    print("")
    timer_repeats = timer_repeats - 1
print("Timer ended!")
print("")
print("")
print("")
print("")
print("")
print("")
input("(!) Press ENTER to continue.")
print("")
print("------------------------------------------------------") # goodbye message
print("Thanks for using the pomodoro timer!")
print("")
print("check out some cool stuff at:")
print("github.com/trashbin7")
print("------------------------------------------------------") #goodbye message end
print("")
print("")
print("")
print("")
input("(!) press ENTER to exit.")
exit
