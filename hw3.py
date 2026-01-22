from tkinter import *
import tkinter.messagebox
import random
window = Tk()
window.geometry("1000x600")
window.title("Game")
window.config(background = "blue")

Number1 = random.randint(1, 25)
Number2 = random.randint(1, 25)
Total = Number1 + Number2

def submit1():
    myName = NameEntry.get()
    tkinter.messagebox.showinfo("Welcome " + myName, "This is my game. You will have to guess the product of 2 number between 1 and 25, meaning the total will be between 1 and 50. Enter it in the bottom box, and click submit to send it through. Guess it right, and you win!")

def submit2():
    myGuess = int(GuessEntry.get())
    if myGuess < Total:
        tkinter.messagebox.showinfo("Oops!", "The number was too low! Try again")
    elif myGuess > Total:
        tkinter.messagebox.showinfo("Oops!", "The number was too high! Try again")
    if myGuess == Total:
        tkinter.messagebox.showinfo("You did it!", "well done for guessing the number. You won!")

Title = Label(window, text = "Welcome to my game", font = ("Ariel", 50))
Name = Label(window, text = "Enter your name: ", font = ("Ariel", 15))
Guess = Label(window, text = "Enter your Guess: ", font = ("Ariel", 15))

NameEntry = Entry(window, width = 45, fg = "red")
GuessEntry = Entry(window, width = 44, fg = "red")

SubmitButton1 = Button(window, text = "submit", bg = "green", fg = "white", command = submit1)
SubmitButton2 = Button(window, text = "submit", bg = "green", fg = "white", command = submit2)

Title.place(x = 330, y = 80)
Name.place(x = 400, y = 180)
Guess.place(x = 400, y = 260)
NameEntry.place(x = 570, y = 185)
GuessEntry.place(x = 577, y = 265)
SubmitButton1.place(x = 850, y = 185)
SubmitButton2.place(x = 850, y = 265)

window.mainloop()