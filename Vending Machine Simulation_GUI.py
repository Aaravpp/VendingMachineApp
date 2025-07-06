from tkinter import *
from tkinter import messagebox

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
        window.geometry("400x600+550+130")

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

        self.selected_code = IntVar()
        self.quantity = StringVar()
        self.amount = StringVar()
        self.total_cost = StringVar(value="Total: ₹0")

        self.widgets()

    def widgets(self):

        Label(window, text="Vending Machine", font=("Helvetica", 18, "bold")).pack()
        
        canvas = Canvas(window, bg="white", height=250)
        scrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)
        self.products_frame = Frame(canvas, bg="white")

        self.products_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.products_frame      , anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, padx=10)
        scrollbar.pack(side="right", fill="y")
        self.product_button = []

        for code, product in self.products.items():

            status = f"{product.quantity} left" if product.quantity > 0 else "Out Of Stock"
            text = f"{product.name} - ₹{product.price}  ({status})"
            state = NORMAL if product.quantity > 0 else DISABLED

            button = Radiobutton(
                self.products_frame,
                text=text,
                variable=self.selected_code,
                value=code,
                bg="white",
                anchor="w",
                justify="left",
                state=state,
                disabledforeground="gray"
            )

            button.pack(anchor="w")
            self.product_button.append(button)

        Label(window, text="Quantity:").pack()
        quantity_box = Entry(window, textvariable=self.quantity)
        quantity_box.pack()
        quantity_box.bind("<KeyRelease>", self.update_total_cost)
 
        Label(window, text="Insert Money (₹):").pack()
        Entry(window, textvariable=self.amount).pack()

        Label(window, textvariable=self.total_cost).pack()

        Button(window, text="Purchase", command=self.purchase, bg="#4CAF50").pack()

    def update_total_cost(self, event=None):

        try:

            code = self.selected_code.get()
            quantity = int(self.quantity.get())
            product = self.products[code]

            if product and quantity > 0:

                total = product.price * quantity

                self.total_cost.set(total)

            else:

                self.total_cost.set(total = 0)

        except:
            self.total_cost.set(total = 0)

    def restock_alert(self):

        for product in self.products:

            if product.quantity <= 2:

                messagebox.showwarning("Low Stock Alert", "\n".join(f"[!] {product.name} has only {product.quantity} left"))

    def purchase(self):

        try:
            
            index = self.selected_code.get()
            quantity = int(self.quantity.get())
            amount = int(self.amount.get())

            product = self.products[index]

            if not product.is_available:

                messagebox.showinfo("Out Of Stock", f"Only {product.quantity} Available")

                return
            
            total = product.price * quantity

            if amount < total:

                messagebox.showerror("Error", f"Not enough money  Total: ₹{total}")

                return
            
            product.dispense(quantity)

            change = amount - total

            messagebox.showinfo("Success", f"Dispensed {quantity} {product.name} \n{change}\n Have a Nice Day!")

            self.restock_alert()
            self.update_total_cost()

        except:

            messagebox.showerror("Input Error", "Please enter valid numbers")


    def update_product(self):

         for idx, product in self.products:
            status = f"Out of Stock" if product.quantity == 0 else "Available"
            text = f"{product.name} - ₹{product.price} ({status})"
            state = DISABLED if product.quantity == 0 else NORMAL
            self.product_buttons[idx].config(text=text, state=state)

if __name__ == "__main__":
    window = Tk()

    app = VendingMachineApp(window)

    window.mainloop()