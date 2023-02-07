import time

def countdown(t):
    s = t * 60
    while s:
        mins, secs = divmod(s, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        s -= 1

    print ('times up!')