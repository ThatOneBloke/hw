from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
window = Tk()
window.geometry("800x600")
window.title("address book")
window.config(bg = "grey")

AddressBook = {}

def add():
    value1 = NameEntry.get()
    value2 = RollNumberEntry.get()
    value3 = MathsMarkEntry.get()
    value4 = MathsMarkEntry.get()
    value5 = PercentageEntry.get()
    AddressBook[value1] = (value2, value3, value4, value5)
    List.insert(END, value1)
    NameEntry.delete(0, END)
    RollNumberEntry.delete(0, END)
    ScienceMarkEntry.delete(0, END)
    MathsMarkEntry.delete(0, END)
    PercentageEntry.delete(0, END)
    messagebox.showinfo("success", "item has been added to list!")

def delete():
    selectedPortion = List.curselection()
    for i in selectedPortion[::-1]:
        List.delete(i)
    
def edit():
    SelectedEntry = List.get(List.curselection())
    ContactInfo = AddressBook[SelectedEntry]
    NameEntry.insert(0, SelectedEntry)
    RollNumberEntry.insert(0, ContactInfo[0])
    ScienceMarkEntry.insert(0, ContactInfo[1])
    MathsMarkEntry.insert(0, ContactInfo[2])
    PercentageEntry.insert(0, ContactInfo[3])

def Save():
    FileOne = asksaveasfile(defaultextension = ".txt")
    for i in List.get(0, END):
        print(i, file = FileOne)
        List.delete(0, END)
    
def open():
    FileOne = askopenfile(title = "open")
    List.delete(0, END)
    items = FileOne.readlines()
    for i in items:
        List.insert(END, i)

heading = Label(window, text = "Student reports", bg = "black", fg = "white", font = ("Ariel", 30))
Name = Label(window, text = "Name: ", bg = "black", fg = "white", font = ("Ariel", 10))
RollNumber = Label(window, text = "Roll Number: ", bg = "black", fg = "white", font = ("Ariel", 10))
ScienceMark = Label(window, text = "Science marks: ", bg = "black", fg = "white", font = ("Ariel", 10))
MathsMark = Label(window, text = "Maths marks: ", bg = "black", fg = "white", font = ("Ariel", 10))
Percentage = Label(window, text = "Percentage: ", bg = "black", fg = "white", font = ("Ariel", 10))
NameEntry = Entry(window, width = 30, fg = "red")
RollNumberEntry = Entry(window, width = 30, fg = "red")
ScienceMarkEntry = Entry(window, width = 30, fg = "red")
MathsMarkEntry = Entry(window, width = 30, fg = "red")
PercentageEntry = Entry(window, width = 30, fg = "red")
AddButton = Button(window, text = "add", bg = "grey", fg = "white", command = add)
EditButton = Button(window, text = "edit", bg = "grey", fg = "white", command = edit)
DeleteButton = Button(window, text = "delete", bg = "grey", fg = "white", command = delete)
SaveButton = Button(window, text = "save", bg = "grey", fg = "white", command = Save)
OpenButton = Button(window, text = "open", bg = "grey", fg = "white", command = open)

List = Listbox(window, width = 50, height = 20)
heading.place(x = 50, y = 10)
Name.place(x = 360, y = 70)
RollNumber.place(x = 360, y = 140)
ScienceMark.place(x = 360, y = 210)
MathsMark.place(x = 360, y = 280)
Percentage.place(x = 360, y = 350)
NameEntry.place(x = 470, y = 71)
RollNumberEntry.place(x = 470, y = 141)
MathsMarkEntry.place(x = 470, y = 211)
ScienceMarkEntry.place(x = 470, y = 282)
PercentageEntry.place(x = 470, y = 352)
List.place(x = 50, y = 70)
AddButton.place(x = 460, y = 415)
EditButton.place(x = 500, y = 415)
DeleteButton.place(x = 50, y = 415)
SaveButton.place(x = 180, y = 415)
OpenButton.place(x = 318, y = 415)

window.mainloop()