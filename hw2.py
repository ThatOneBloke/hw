from tkinter import *
from time import strftime
window = Tk()
window.geometry("500x200")
window.title("digital clock")

window.config(background = "purple")
label1 = Label(window, font = ("Ariel", 30))
label2 = Label(window, font = ("Ariel", 30))
Label3 = Label(window, text = "Time in the UK:", font = ("Ariel", 35))
Label4 = Label(window, text = "calender:", font = ("Ariel", 35))

def clockAndCalender():
    timeformat = strftime("%I : %M : %S : %p")
    label1.configure(text = timeformat)
    label1.after(1000, clockAndCalender)
    dateformat = strftime("%A %d of %B %Y")
    label2.configure(text = dateformat)
    label2.after(1000, clockAndCalender)

label1.place(x = 50, y = 120)
label2.place(x = 50, y = 320)
Label3.place(x = 50, y = 60)
Label4.place(x = 50, y = 250)
clockAndCalender()


window.mainloop()