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
    return hour

#this will get the current minute
def minute():
    minute = now.minute
    return minute

def main():
    
        
    
main()