# Show an animtated clock that counts down
# Idea by Al sweigart, changed and created by Tobias Widell

import sys
import time
import ClockSymbols as clock

secondsBeforeExplosion = 20

try:  
    print('***** Press Ctrl-C to end countdown *****')  
    while True:
        
        hours =  str(secondsBeforeExplosion // 3600)
        minutes = str((secondsBeforeExplosion % 3600) // 60)
        seconds = str(secondsBeforeExplosion % 60)
        
        hourDigits = clock.getClockSymbolesStr(hours , 2)
        hoursTop, hoursMiddle, hoursBottom = hourDigits.splitlines()
        
        minutesDigits = clock.getClockSymbolesStr(minutes, 2)
        minutesTop, minutesMiddle, minutesBottom = minutesDigits.splitlines()
        
        secondsDigits = clock.getClockSymbolesStr(seconds, 2)
        secondsTop, secondsMiddle, secondsBottom = secondsDigits.splitlines()
        
        print(hoursTop + '   ' + minutesTop + '   ' + secondsTop)
        print(hoursMiddle + ' * ' + minutesMiddle + ' * ' + secondsMiddle)
        print(hoursBottom + ' * ' + minutesBottom + ' * ' + secondsBottom)
        
        if secondsBeforeExplosion == 0:
            print('***** BOOM *****')
            break
        
        
        time.sleep(0.5)
        
        secondsBeforeExplosion -= 1
except KeyboardInterrupt:
    print('Goodbye')
    sys.exit()
        
        
#number = ClockSymbols.getClockSymbolesStr(44,3)
#print(number)
