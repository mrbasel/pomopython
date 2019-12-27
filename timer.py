import os, sys
from time import sleep
from playsound import playsound


# Insert time in minutes
def timer(minutes=25, isbreaktime=False):
    clear()
    seconds = 0
    while True:
        if seconds == 0:
            minutes -= 1
            seconds = 60
        seconds = seconds - 1
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

    if isbreaktime:
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
            timer(time)
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


def typeLetterByLetter(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sleep(delay)
        sys.stdout.flush()
        # sleep(1)


# Main process
def main(worktime=25, breaktime=5, soundeffect=True):
    clear()
    typeLetterByLetter('Welcome to PomoPython!')
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
            [g] github page

-------------------------------------------
            ''')
            userchoise = input('')
            if userchoise.lower() == 's':
                worktimer(worktime) # starts Work timer
                breaktimer(breaktime, isbreaktime=True) # starts Break timer
            elif userchoise.lower() == 'q':
                typeLetterByLetter('Goodbye!', 0.05)
                sleep(0.5)
                break
            else:
                print('I dont understand!')
                sleep(0.5)
                clear()
                pass
    except KeyboardInterrupt:
        typeLetterByLetter('Goodbye!')

class Timer:
    def __init__(self):
        passn



if __name__ == '__main__':
    main()
