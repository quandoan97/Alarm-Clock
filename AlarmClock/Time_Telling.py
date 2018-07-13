import vlc
import time
import datetime

#this will be the current time 
now = datetime.datetime.now()

#this will get the current hour  
def hour():
    hour = now.hour 
    if hour > 12:
        hour = hour - 12
    #this is for the case of when it is 12 am 
    elif hour == 0:
        hour = 12
    return hour

#this will get the current minute
def minute():
    minute = now.minute
    return minute

#this function will be able to play the sound of the time 
def play(hour, minute):
    print(hour)

def main():
    
    play(hour(), minute())
    
main()