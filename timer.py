import os, sys
from time import sleep
from playsound import playsound


# Insert time in minutes
def timer(minutes=25, isbreaktime= False):
    clear()
    seconds = 0
    while True:
        if seconds == 0:
            minutes -= 1
            seconds = 60
        seconds = seconds - 1
        if isbreaktime:
            displayclock(minutes, seconds, isbreaktime=True)
        else:
            displayclock(minutes, seconds)
        sleep(1)
        clear()
        if minutes == 0 and seconds == 0:
            ding()  # Plays sound alert
            break


# The display format
def displayclock(minutes, seconds, isbreaktime=False):
    if seconds in range(10):
        clock = f'{minutes}:0{seconds}'
    else:
        clock = f'{minutes}:{seconds}'

    if isbreaktime == True:
        print( f'''
        |*------------------------*|
                  {clock}
        |*------------------------*|

    Break time!
        ''')
    else:

        print( f'''
        |*------------------------*|
                  {clock}
        |*------------------------*|

    Focus!
        ''')


def choosetime():
    while True:
        try:
            worktime = input('\nInsert work time(In minutes):\n')
            breaktime = input('Break time:\n')
        except Exception as e:
            print(e)
            continue
        break
    return [int(worktime), int(breaktime)]


def worktimer(time=25):
    timer(time)


def breaktimer(time=5):
    while True:
        userinput = input('Do you want to have a break? (y/n)\n')
        if userinput.lower() == 'y':
            timer(time, isbreaktime=True)
        elif userinput.lower() == 'n':
            pass
        else:
            print("I don't understand")
            continue
        break


# Plays an mp3 file for sound effects
def ding():
    playsound('definite.mp3')


# Clears command line
def clear():
    os.system('cls')


def printletterbyletter(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)
        # sleep(1)


# Main process
def main(worktime=25, breaktime=5, soundeffect=True):
    clear()
    printletterbyletter('Welcome to PomoPython!', delay=0.06)
    timeChoise = choosetime() # Askes user for work and break time
    worktime = timeChoise[0]
    breaktime = timeChoise[1]
    clear()
    try:
        while True:
            print('''
-------------------------------------------

            [s] to start timer
            [q] to quit
            [b] to change time
-------------------------------------------
            ''')
            userchoise = input('')
            if userchoise.lower() == 's':
                worktimer(worktime) # starts Work timer
                breaktimer(breaktime) # starts Break timer
            elif userchoise.lower() == 'q':
                printletterbyletter('Goodbye!', 0.03)
                sleep(0.5)
                break
            elif userchoise.lower() == 'b':
                main()
            else:
                print('I dont understand!')
                sleep(0.5)
                clear()
                pass
    except KeyboardInterrupt:
        printletterbyletter('Goodbye!')


if __name__ == '__main__':
    main()
