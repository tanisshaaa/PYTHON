import time
currentTime=time.time()
totalSec=int(currentTime)
currentSec=totalSec%60
totalMin=totalSec//60
currentMin=totalMin%60
totalHour=totalMin//60
currentHour=totalHour%24

print(currentHour,currentMin,currentSec)


