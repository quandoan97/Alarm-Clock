import vlc
import time
import datetime

#this will be the current time 
now = datetime.datetime.now()

instance = vlc.Instance()

am_pm = "am"
#this will get the current hour  
def hour():
    hour = now.hour 
    if hour > 12:
        hour = hour - 12
        am_pm = "pm"
    #this is for the case of when it is 12 am 
    elif hour == 0:
        hour = 12
        am_pm = "am"
    return hour

#this will get the current minute
def minute():
    minute = now.minute
    return minute

#this function will be able to play the sound of the time 
def play(command):
    
    #Interpreting the 
    if command == "hour":
        file_Path = str(hour()) + ".wav"
    elif command == "tens_minute":
        tens_minute = str(minute())
        file_Path = tens_minute[0]+ "0" + ".wav"
    elif command == "ones_minute":
        ones_minute = str(minute())
        file_Path = ones_minute[1] + ".wav"
    elif command == "its":
        file_Path = "its.wav"
    elif command == "o":
        file_Path = "o.wav"
    elif command == "am":
        file_Path = "am.wav"
    elif command == "pm":
        file_Path = "pm.wav"

    #Create a MediaPlayer with the default instance
    player = instance.media_player_new()

    #Load the media file
    media = instance.media_new(file_Path)

    #Add the media to the player
    player.set_media(media)

    player.play()
    time.sleep(1)

def main():
    
    play("its")
    play("hour")
    play("tens_minute")
    play("ones_minute")
    play(am_pm)

main()