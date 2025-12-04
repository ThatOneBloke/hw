from tkinter import *
window = Tk()
window.geometry("600x600")
window.title("food ordering app")
window.config(bg = "red")

email = Label(window, text = "Email Address: ", font = ("Ariel", 8))
email.place(x = 50, y = 50)
password = Label(window, text = "Password: ", font = ("Ariel", 8))
password.place(x = 50, y = 75)
FPlabel = Label(window, text = "What would you like? Chicken Sanwich, B.L.T, Veg Sandwitch or Nothing", font = ("Ariel", 8))
FPlabel.place(x = 90, y = 110)

EmailEntry = Entry(window, width = 40, fg = "red")
EmailEntry.place(x = 180, y = 50)
PasswordEntry = Entry(window, width = 40, fg = "red")
PasswordEntry.place(x = 180, y = 75)

FirstPick1 = Spinbox(window, values = ("Chicken Sandwitch", "B.L.T", "Veg Sandwitch", "None"))
FirstPick1.place(x = 110, y = 140)
FirstPick2 = Spinbox(window, from_ = 1, to = 999)
FirstPick2.place(x = 260, y = 140)

window.mainloop()