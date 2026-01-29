from tkinter import *
import time
from tkinter import messagebox
window = Tk()
window.geometry("500x200")
window.title("counter stopwatch")

Hour = StringVar()
Minute = StringVar()
Second = StringVar()

Hour.set("00")
Minute.set("00")
Second.set("00")

def stopwatch():
    global Hour, Minute, Second
    HEntry.config(state = DISABLED)
    MEntry.config(state = DISABLED)
    SEntry.config(state = DISABLED)
    TimeInS = int(Hour.get()) * 3600 + int(Minute.get()) * 60 + int(Second.get())
    while TimeInS > -1:
        M,S = divmod(TimeInS, 60)
        H = 00
        if M > 60:
            H,M = divmod(M, 60)
        Hour.set(H)
        Minute.set(M)
        Second.set(S)
        window.update()
        time.sleep(1)
        if TimeInS == 0:
            messagebox.showinfo("Countdown has finished!", "The time you have chosen has ended.")
        TimeInS -= 1

heading = Label(window, text = "Stopwatch ", bg = "black", fg = "white", font = ("Ariel", 30))
name1 = Label(window, text = "H", font = ("Ariel", 15))
name2 = Label(window, text = "M", font = ("Ariel", 15))
name3 = Label(window, text = "S", font = ("Ariel", 15))

HEntry = Entry(window, width = 3, fg = "red", textvariable = Hour)
MEntry = Entry(window, width = 3, fg = "red", textvariable = Minute)
SEntry = Entry(window, width = 3, fg = "red", textvariable = Second)
SubmitButton = Button(window, text = "submit", bg = "purple", fg = "white", command = stopwatch)
SubmitButton.place(x = 50, y = 450)

heading.place(x = 160, y = 50)
name1.place(x = 100, y = 120)
name2.place(x = 250, y = 120)
name3.place(x = 400, y = 120)

HEntry.place(x = 100, y = 160)
MEntry.place(x = 250, y = 160)
SEntry.place(x = 400, y = 160)

SubmitButton.place(x = 280, y = 230)

window.mainloop()