#Number display module

def getClockSymbolesStr(number, minwidth=0):
    number = str(number).zfill(minwidth)
    
    rows =  ['','','']
