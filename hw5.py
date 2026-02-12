from tkinter import *
from tkinter.ttk import Combobox
window = Tk()
window.geometry("600x600")
window.title("Times Table Generator")
pizzas = StringVar()
numberAmount = IntVar()
size = StringVar()

def order():
    global Pizza, Amount, Total
    pizza = Pizza.get()
    amount = Amount.get()
    Size = size.get()
    if pizza == "margharita":
        Total = 10 * int(amount)
    if pizza == "Veggie":
        Total = 15 * int(amount)
    if pizza == "meat monster":
        Total = 17 * int(amount)
    if pizza == "pepperoni":
        Total = 26 * int(amount)
    FullOrder = ("you ordered " + str(amount) + " " + str(Size) + " " + str(pizza) + " pizza(s) for " + str(Total))
    Orders.configure(text = FullOrder)
 
Title = Label(window, text = "Pizza deliver service ", font = ("Ariel", 30))
Pizzabox = Label(window, text = "Choose a pizza: ", font = ("Ariel", 15))
Amountbox = Label(window, text = "Choose an amount: ", font = ("Ariel", 15))
Orders = Label(window)

Pizza = Combobox(window, textvariable = pizzas)
Pizza["values"] = ["margharita", "Veggie", "meat monster", "pepperoni"]
Amount = Combobox(window, textvariable = numberAmount)
Amount["values"] = list(range(1, 15))

radio1 = Radiobutton(window, text = "Small", variable = size, value = "small")
radio2 = Radiobutton(window, text = "Medium", variable = size, value = "medium")
radio3 = Radiobutton(window, text = "Large", variable = size, value = "large")

SubmitButton = Button(window, text = "submit", bg = "purple", fg = "white", command = order)

Title.place(x = 100, y = 80)
Pizzabox.place(x = 60, y = 140)
Orders.place(x = 100, y = 300)
Pizza.place(x = 260, y = 146)
Amount.place(x = 260, y = 176)
radio1.place(x = 300, y = 420)
radio2.place(x = 300, y = 450)
radio3.place(x = 300, y = 480)
SubmitButton.place(x = 420, y = 144)

window.mainloop()