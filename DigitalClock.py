import sys
import time
import ClockSymbols as clock

try:
    while True:
        CURRENT_TIME = time.localtime()
        hours = str(CURRENT_TIME.tm_hour)
        if(hours == '0'):
                hours == '24'
        minutes = str(CURRENT_TIME.tm_min)
        seconds = str(CURRENT_TIME.tm_sec)
        
        # Get the Seven-Segment Display Clock from Clocksymbols.py
        hoursDigits = clock.getClockSymbolesStr(hours, 2)
        hoursTop, hoursMiddle, hoursBottom = hoursDigits.splitlines()
        
        minutesDigits = clock.getClockSymbolesStr(minutes, 2)
        minutesTop, minutesMiddle, minutesBottom = minutesDigits.splitlines()
        
        secondsDigits = clock.getClockSymbolesStr(seconds, 2)
        secondsTop, secondsMiddle, secondsBottom = secondsDigits.splitlines()
                
        print(hoursTop + '   ' + minutesTop + '   ' + secondsTop)
        print(hoursMiddle + ' * ' + minutesMiddle + ' * ' + secondsMiddle)
        print(hoursBottom + ' * ' + minutesBottom + ' * ' + secondsBottom)
        print()
        # Press Ctrl-C to quit
        
        while True:
            time.sleep(0.1)
            if time.localtime().tm_sec != CURRENT_TIME.tm_sec:
                break
except KeyboardInterrupt:
    print('Goodbye')
    sys.exit()      