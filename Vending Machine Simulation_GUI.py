from tkinter import *

class product:

    def __init__(self, name, price, quantity):
        
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def is_available(self, quantity):

        return quantity <= self.quantity
    
    def dispense(self, quantity):

        if self.is_available(quantity):

            self.quantity -= quantity

            return True
        
        return False
    
class VendingMachineApp:

    def __init__(self, window):
        
        window.title("Vending Machine")
        window.geometry("400x500+550+130")

        self.products = {

            1: product("Lays", 50, 7),
            2: product("KurKure", 20, 10),
            3: product("Cheetos", 50, 5),
            4: product("Bingo", 20, 8),
            5: product("Kitkat", 35, 8),
            6: product("Dairy Milk Silk", 100, 6),
            7: product("Snickers", 50, 3),
            8: product("Galaxy", 80, 9),
            9: product("Munch", 30, 2),
            10: product("Kinder Joy", 50, 0),
            11: product("Sprite", 40, 3),
            12: product("Pepsi", 40, 6),
            13: product("Coca-Cola", 40, 7),
            14: product("Red Bull", 165, 7),
            15: product("Fanta", 40, 4)

        }

        self.widgets()

    def widgets(self):

        Label(window, text="Vending Machine", font=("Helvetica", 18, "bold")).pack()

        self.products = []

        for index, product in self.products:

            status = f"Out Of Stock" if product.quantity == 0 else "Available"
            text = f"{product.name} - ₹{product.price}  ({status})"
            state = DISABLED if product.quantity == 0 else NORMAL

            button = RADIOBUTTON(

                window,
                text = text,
                Variable = self.selected_code,
                value = index,
                ANCHOR = "w",
                justify = "left",
                state = state,
                disabledforground = "gray"

            )

            button.pack()
            self.products.append(button)

            self.selected_code = IntVar()
            self.quantity = StringVar()
            self.amount = StringVar()
            self.total_cost = StringVar(value="Total: ₹0")

        Label(window, text="Quantity:").pack()
        quantity_box = Entry(window, textvariable=self.quantity)
        quantity_box.pack()

        Label(window, text="Insert Money (₹):").pack()
        Entry(window, textvariable=self.amount).pack()

        Label(window, textvariable=self.total_cost).pack()

        Button(window, text="Purchase", command=self.purchase, bg="#4CAF50").pack()


window = Tk()

app = VendingMachineApp(window)

window.mainloop()