# First install playsound through terminal by typing 'pip install playsound'
from playsound import playsound
from tkinter import *
from tkinter import messagebox
# Import time for counter
import time
import pygame

# Python ANSI codes
Clear = "\033[2J"  # For clearing everything on console
ClearAndReturn = "\033[H"  # For clearing everything, including spaces
Red = "\u001b[31m"  # Changes color of console text to red
Color_Off = "\033[0m"  # Changes color of console text to original color
pygame.mixer.init()

# Alarm function
def alarm(totSeconds):
    timeElapsed = 0

    global stopper
    stopper = False
    while timeElapsed < totSeconds:  # A loop that does the countdown until it reaches zero
        # (actually it is reverse countdown until it reaches the time user provides)
        time.sleep(1)
        timeElapsed += 1

        timeLeft = totSeconds - timeElapsed
        hoursLeft = int(timeLeft // 3600).__format__('02d')
        minutesLeft = int(timeLeft // 60).__format__('02d')
        secondsLeft = int(timeLeft % 60).__format__('02d')

        hrs.set(hoursLeft)
        mins.set(minutesLeft)
        secs.set(secondsLeft)
        root.update()

    if(timeLeft == 0):
        pygame.mixer.music.load("alarm.mp3")
        pygame.mixer.music.play(loops=0)
        secs.set("00")
        mins.set("00")
        hrs.set("00")
        root.update()


# Clock function
def clock():
    clockTime = time.strftime('%I:%M:%S %p')
    currentTime.config(text=clockTime)
    currentTime.after(1000, clock)

# Functions for start and stop
def setAlarm():
    totSeconds = (int(hrs.get())*3600) + (int(mins.get())*60) + int(secs.get())
    alarm(totSeconds)
def stopAlarm():
    global stopper
    stopper = True
    root.update()
    hrs.set("00")
    mins.set("00")
    secs.set("00")
    pygame.mixer.music.stop()

# Functions for different alarm times
def study():
    hrs.set("00")
    mins.set("25")
    secs.set("00")
def break1():
    hrs.set("00")
    mins.set("10")
    secs.set("00")
def break2():
    hrs.set("00")
    mins.set("15")
    secs.set("00")

# Initialising the tkiner window
root = Tk()
root.title("Alarm")
root.geometry("400x590")
root.config(bg="#000")
root.resizable(False,False)

heading = Label(root, text="Personal Alarm", font="arial 30 bold", bg="#ea3548")
heading.pack(pady=10)

Label(root, font=("arial", 15, "bold"), text="Current Time:", fg="Orange", bg="#000").place(x=65, y=70)

currentTime = Label(root, font=("arial", 15, "bold"), text="", fg="Orange", bg="#000")
currentTime.place(x=210, y=70)
clock()

Label(root, text="Please insert the alarm time:", font="arial 12", fg="white", bg="#000").pack(padx=5, pady=90)

hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font="arial 30", fg="white", bg="#000", bd=0).place(x=50, y=200)
hrs.set("00")
mins = StringVar()
Entry(root, textvariable=mins, width=2, font="arial 30", fg="white", bg="#000", bd=0).place(x=180, y=200)
mins.set("00")
secs = StringVar()
Entry(root, textvariable=secs, width=2, font="arial 30", fg="white", bg="#000", bd=0).place(x=300, y=200)
secs.set("00")

Label(root, text="Hours", font="arial 12", fg="white", bg="#000").place(x=50, y=250)
Label(root, text="Minutes", font="arial 12", fg="white", bg="#000").place(x=170, y=250)
Label(root, text="Seconds", font="arial 12", fg="white", bg="#000").place(x=290, y=250)

# Start and stop button
alarmButton = Button(root, text="Start Alarm", fg="white", bg="green", bd=0, font="arial 15 bold", width=10, height=2,
                     command=setAlarm)
stopButton = Button(root, text="Stop Alarm", fg="white", bg="green", bd=0, font="arial 15 bold", width=10, height=2,
                     command=stopAlarm)
alarmButton.pack(padx=5, pady=40, side=LEFT)
stopButton.pack(padx=5, pady=40, side=RIGHT)

# Different alarm times
studyButton = Button(root, text="Study 25 mins", fg="white", bg="Orange", bd=0, font="arial 10 bold", width=12,
                     height=2, command=study)
studyButton.place(x=30, y=350)
breakButton1 = Button(root, text="Break 10 mins", fg="white", bg="Orange", bd=0, font="arial 10 bold", width=12,
                      height=2,command=break1)
breakButton1.place(x=150, y=350)
breakButton2 = Button(root, text="Break 15 mins", fg="white", bg="Orange", bd=0, font="arial 10 bold", width=12,
                      height=2,command=break2)
breakButton2.place(x=270, y=350)

root.mainloop()
