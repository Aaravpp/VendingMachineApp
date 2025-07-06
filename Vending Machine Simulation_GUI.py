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
        pass

window = Tk()

app = VendingMachineApp(window)

window.mainloop()