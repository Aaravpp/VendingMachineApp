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

window = Tk()

app = VendingMachineApp(window)

window.mainloop()