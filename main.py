##############################################################################
# Author: Noah Harris
# Date Written: 10/2/23
# Assignment: Final Project
# Short Desc: This GUI application is designed to prompt a user to select what they would like to
# order from "Hailey's Diner". The program allows for the user to select items from
# the food menu and add these items to their current cart. Users can select items from the menu,
# sides and drinks, and desserts. They can view their current cart, checkout and leave a tip,
# clear their cart, or exit.
##############################################################################


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage

class RestaurantOrdering:
    def __init__(self, root):
        self.root = root
        self.root.title("Hailey's Diner")
        self.current_window = None
        self.cart = []
        self.tip = 0

        self.style = ttk.Style()

        # style for buttons
        self.style.configure("TButton", padding=(10, 5), font=("Helvetica", 12))

        # load images and resize them
        self.menu_image = PhotoImage(file="Images/menu.png")
        self.menu_image = self.menu_image.subsample(8)
        self.sides_image = PhotoImage(file="Images/drink.png")
        self.sides_image = self.sides_image.subsample(10)

        # Create buttons for navigation
        self.menu_button = tk.Button(root, text="Menu", command=self.show_menu, image=self.menu_image, compound=tk.LEFT)
        self.sides_button = tk.Button(root, text="Sides and Drinks", command=self.show_sides, image=self.sides_image, compound=tk.LEFT)
        self.desserts_button = tk.Button(root, text="Desserts", command=self.show_desserts)
        self.cart_button = tk.Button(root, text="Cart", command=self.show_cart)
        self.checkout_button = tk.Button(root, text="Checkout", command=self.show_checkout)
        self.clear_cart_button = tk.Button(root, text="Clear Cart", command=self.clear_cart)
        self.exit_button = tk.Button(root, text="Exit", command=root.quit)

        # add padding between buttons
        buttons = [
            self.menu_button,
            self.sides_button,
            self.desserts_button,
            self.cart_button,
            self.checkout_button,
            self.clear_cart_button,
            self.exit_button
        ]

        for button in buttons:
            button.pack(pady=5)

        # Pack buttons
        self.menu_button.pack()
        self.sides_button.pack()
        self.desserts_button.pack()
        self.cart_button.pack()
        self.checkout_button.pack()
        self.clear_cart_button.pack()
        self.exit_button.pack()

    # code to display menu window
    def show_menu(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = tk.Toplevel(self.root)
        self.current_window.title("Menu")

        # Create menu items
        menu_items = [
            {"name": "Burger", "price": 10},
            {"name": "Pizza", "price": 12},
            {"name": "Salad", "price": 6},
        ]

        for item in menu_items:
            item_label = tk.Label(self.current_window, text=f"{item['name']} - ${item['price']}")
            add_button = tk.Button(self.current_window, text="Add to Cart", command=lambda item=item: self.add_to_cart(item))
            item_label.pack()
            add_button.pack()

    # code to display sides window
    def show_sides(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = tk.Toplevel(self.root)
        self.current_window.title("Sides")

        # create Sides items
        sides_items = [
            {"name": "French Fries", "price": 2.50},
            {"name": "Potato Salad", "price": 1},
            {"name": "Macaroni Salad", "price": 1},
            {"name": "Tater Tots", "price": 2},
            {"name": "Large Coke", "price": 2},
            {"name": "Medium Coke", "price": 1.50},
            {"name": "Small Coke", "price": 1}
        ]

        for item in sides_items:
            item_label = tk.Label(self.current_window, text=f"{item['name']} - ${item['price']}")
            add_button = tk.Button(self.current_window, text="Add to Cart", command=lambda item=item: self.add_to_cart(item))
            item_label.pack()
            add_button.pack()

    # code to display desserts window
    def show_desserts(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = tk.Toplevel(self.root)
        self.current_window.title("Desserts")

        # create Dessert items
        desserts_items = [
            {"name": "Apple Pie", "price": 2},
            {"name": "Sugar Cream Pie", "price": 2},
            {"name": "Dirt Pudding", "price": 2.50},
            {"name": "Chocolate Chip Cookie", "price": .50},
            {"name": "Chocolate Chip Cookie (x6)", "price": 2},
            {"name": "Peach Cobbler", "price": 3},
            {"name": "Apple Cobbler", "price": 3}
        ]

        for item in desserts_items:
            item_label = tk.Label(self.current_window, text=f"{item['name']} - ${item['price']}")
            add_button = tk.Button(self.current_window, text="Add to Cart", command=lambda item=item: self.add_to_cart(item))
            item_label.pack()
            add_button.pack()

    # code to display cart window
    def show_cart(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = tk.Toplevel(self.root)
        self.current_window.title("Shopping Cart")

        # Display items in the cart
        for item in self.cart:
            item_label = tk.Label(self.current_window, text=f"{item['name']} - ${item['price']} x{item['quantity']}")
            item_label.pack()

    # function to add items to the user's cart
    def add_to_cart(self, item):
        self.cart.append({"name": item["name"], "price": item["price"], "quantity": 1})
        messagebox.showinfo("Added to Cart", f"{item['name']} has been added to your cart.")

    # code to display checkout window
    def show_checkout(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = tk.Toplevel(self.root)
        self.current_window.title("Checkout")

        total_cost = self.calculate_total_cost()

        # Labels for subtotal, tip, and total
        subtotal_label = tk.Label(self.current_window, text=f"Subtotal: ${sum(item['price'] * item['quantity'] for item in self.cart):.2f}")
        tip_label = tk.Label(self.current_window, text=f"Tip: ${self.tip:.2f}")
        total_label = tk.Label(self.current_window, text=f"Total Cost: ${total_cost:.2f}")

        subtotal_label.pack()
        tip_label.pack()
        total_label.pack()

        # option to leave tip
        tip_entry_label = tk.Label(self.current_window, text="Leave a Tip: ")
        tip_entry = tk.Entry(self.current_window)
        tip_entry.insert(0, str(self.tip))
        tip_entry_label.pack()
        tip_entry.pack()

        # create button to add tip to total cost
        apply_tip_button = tk.Button(self.current_window, text="Apply Tip", command=lambda: self.apply_tip(tip_entry, tip_label, total_label))
        apply_tip_button.pack()

    # apply tip amount to total cost
    def apply_tip(self, tip_entry, tip_label, total_label):
        try:
            self.tip = float(tip_entry.get())
            tip_label.config(text=f"Tip: ${self.tip:.2f}")
            total_label.config(text=f"Total Cost: ${self.calculate_total_cost():.2f}")
        except ValueError:
            messagebox.showerror("Invalid Tip Amount", "Please enter a valid tip amount.")

    # calculate total cost with tip
    def calculate_total_cost(self):
        return sum(item['price'] * item['quantity'] for item in self.cart) + self.tip

    # code to clear user's cart
    def clear_cart(self):
        self.cart = []
        messagebox.showinfo("Cart Cleared", "Your Cart has been cleared!")


if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrdering(root)
    root.mainloop()
