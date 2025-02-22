#!/usr/bin/env python3

import os
import time

def countdown_timer(minutes):
    total_seconds = minutes * 60
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        time_format = 'Countdown: {:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')
        time.sleep(1)
        total_seconds -= 1
    print("\n\nTimer Complete!\n")

if __name__ == "__main__":
    # Clear the screen (cross-platform)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("[Python Program Instructions]\n-------------------------------")
    print("Enter minutes, and press enter:\n-------------------------------\n")
    minutes = int(input("Minutes for countdown: "))
    print("")
    countdown_timer(minutes)

