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
FPlabel = Label(window, text = "What would you liketo drink? Cola, Orange juice, water or Nothing", font = ("Ariel", 8))
FPlabel.place(x = 90, y = 210)
FPlabel = Label(window, text = "What would you like for desert? Ice cream, Ice loly, Chocolate cake or Nothing", font = ("Ariel", 8))
FPlabel.place(x = 90, y = 310)

EmailEntry = Entry(window, width = 40, fg = "red")
EmailEntry.place(x = 180, y = 50)
PasswordEntry = Entry(window, width = 40, fg = "red")
PasswordEntry.place(x = 180, y = 75)

FirstPick1 = Spinbox(window, values = ("Chicken Sandwitch", "B.L.T", "Veg Sandwitch", "None"))
FirstPick1.place(x = 110, y = 140)
FirstPick2 = Spinbox(window, from_ = 1, to = 999)
FirstPick2.place(x = 260, y = 140)

FirstPick5 = Spinbox(window, values = ("Cola", "Orange juice", "Water", "None"))
FirstPick5.place(x = 110, y = 240)
FirstPick6 = Spinbox(window, from_ = 1, to = 999)
FirstPick6.place(x = 260, y = 240)

FirstPick3 = Spinbox(window, values = ("Ice cream", "Ice loly", "Chocolate cake", "None"))
FirstPick3.place(x = 110, y = 340)
FirstPick4 = Spinbox(window, from_ = 1, to = 999)
FirstPick4.place(x = 260, y = 340)

SubmitButton = Button(window, text = "submit", bg = "purple", fg = "white", command = window.destroy)
SubmitButton.place(x = 300, y = 450)

window.mainloop()