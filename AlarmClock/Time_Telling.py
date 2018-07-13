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
    #Case for when there is no 10's place in the time
    if len(str(minute)) < 2:
        minute = "0" +str(minute)
    return minute

#this function will be able to play the sound of the time 
def play(command):
    
    #Interpreting the 
    if command == "hour":
        file_Path = str(hour()) + ".wav"
    elif command == "tens_minute":
        tens_minute = str(minute())
        #this will check for numbers between 11-19
        if tens_minute[0] == "0":
            play("o")
        elif tens_minute == "11":
            file_Path = "11.wav"
        elif tens_minute == "12":
            file_Path = "12.wav"
        elif tens_minute == "13":
            file_Path = "13.wav"
        elif tens_minute == "14":
            file_Path = "14.wav"
        elif tens_minute == "15":
            file_Path = "15.wav"
        elif tens_minute == "16":
            file_Path = "16.wav"
        elif tens_minute == "17":
            file_Path = "17.wav"
        elif tens_minute == "18":
            file_Path = "18.wav"
        elif tens_minute == "19":
            file_Path = "19.wav"
        else:
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
    if minute() >= 20:
        play("ones_minute")
    play(am_pm)

main()