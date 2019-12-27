import os, sys
from time import sleep
from playsound import playsound


def choosetime():
    worktime = input('Welcome to PomoPython!\nInsert work time(In minutes):\n')
    breaktime = input('Break time:')
    return [worktime, breaktime]

def breaktimer(time=1):
    userinput = input('Do you want to have a break? (y/n)')
    if userinput == 'y':
        timer(time, breaktime=True)
    elif userinput == 'n':
        timer()

# Plays an mp3 file for sound effects
def ding():
    playsound('definite.mp3')

def displayclock(minutes, seconds):
    if seconds in range(10):
        clock = f'{minutes}:0{seconds}'
    else:
        clock = f'{minutes}:{seconds}'
    print( f'''
*------------------------*
        {clock}
*------------------------*

Working..
    ''')

# Insert time in minutes
def timer(minutes=25, time4break=5, breaktime=False):
    seconds = 0
    clear()
    while True:
        if seconds == 0:
            if minutes == 0:
                ding()
                if breaktime:
                    x = input('Break is over, start working?(y)')
                else:
                    breaktimer()
            else:
                seconds = 60
                minutes -= 1
        seconds = seconds - 1
        displayclock(minutes, seconds)
        sleep(1)
        clear()

# Clears command line
def clear():
    os.system('cls')


def main(worktime=25, breaktime=5, soundeffect=True):
    userchoise = choosetime() # Lets user choose work and breaktime
    worktime = userchoise[0]
    breaktime = userchoise[1]
    timer(worktime, breaktime)


class Timer:
    def __init__(self):
        pass

if __name__ == '__main__':
    timer(1)
