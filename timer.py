import time
print('Timer')
minutes = int(input('Minutes: '))
seconds = int(input('Seconds: '))
timer = (minutes * 60) + seconds
x = seconds
y = minutes
while timer > 0:
    print(y, ':', x)
    time.sleep(1)
    x -= 1
    if x == 0 or x == -1:
        x = 59
        y -= 1
    timer -= 1


