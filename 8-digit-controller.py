import common_anode_display as display
import time
from urllib import request
import json

print('big-8-digit starting up...')

with open("config.json") as file:
    config = json.load(file)

mode = ''
timertarget = ''

checkTimersIntervals = {
  'checkUrl': [config['checkUrlInterval'] * 1000, 0],
  'updateClock' : [250, 0]
}



display.init_display()

def checkTimers ():
    now = int(round(time.time() * 1000))
    for timer in checkTimersIntervals:
        if (now - checkTimersIntervals[timer][1] > checkTimersIntervals[timer][0]):
            if (timer == 'checkUrl'):
                checkUrl()                
            if (timer == 'updateClock' and mode == 'clock'):
                updateClock()
            if (timer == 'updateClock' and mode == 'timer'):
                updateTimer()
            checkTimersIntervals[timer][1] = now


def getUrl(url):
    file = request.urlopen(url)
    return file

def checkUrl():
    global mode
    global timertarget
    try:
        file = getUrl(config['url'])
        for line in file:        
            decoded_line = line.decode("utf-8")
            if (decoded_line[0] == '#'):
                pass # pass line because of comment
            elif ('clock' in decoded_line):
                mode = 'clock' # turn display into clock
            elif (decoded_line[0] == '>'):
                mode = 'timer' # turn display into timer mode
                timertarget = decoded_line[1:9]
            elif (decoded_line[0] == '%'): # if % is preceeding go to command mode
                if ('brightness' in decoded_line):
                    brightness = int(decoded_line[len(decoded_line)-3:len(decoded_line)-1])
                    display.brightness(brightness)
            else:
                mode = 'string'
                display.show_string(decoded_line)
    except:
        if (mode == ''): # if we have problems with fetching url go to clock mode 
            mode = 'clock'

def updateClock():
    now = time.localtime(time.time())    
    display.show_string("{0:02d}-{1:02d}-{2:02d}".format(now.tm_hour,now.tm_min,now.tm_sec))

def updateTimer():
    now = time.localtime(time.time())
    secsTimerTarget = int(timertarget[0:2]) * 3600 + int(timertarget[3:5]) * 60 + int(timertarget[6:8])
    secsToGo =  secsTimerTarget - (now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec)    
    m, s = divmod(secsToGo, 60) # break number of secs on base of 60 to minutes
    h, m = divmod(m, 60) # and again for hours
    if (h < 2):
        display.show_string("{0:02d}-{1:02d}".format(m + (h*60),s))
    else:
        display.show_string("{0:02d}o {1:02d}.{2:02d}".format(h,m,s))
    

while True:
    checkTimers()



