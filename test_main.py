import unittest
from unittest.mock import patch
import tkinter as tk
from main import RestaurantOrdering  # Import your RestaurantOrdering class

class TestRestaurantOrdering(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = RestaurantOrdering(self.root)
        self.app.tip = 0

    def tearDown(self):
        self.root.destroy()

    @patch("tkinter.PhotoImage", side_effect=lambda file, **kwargs: file)
    def test_show_menu(self, mock_photoimage):
        self.app.show_menu()
        self.assertEqual(self.app.current_window.winfo_exists(), 1)

    @patch("tkinter.PhotoImage", side_effect=lambda file, **kwargs: file)
    def test_show_sides(self, mock_photoimage):
        self.app.show_sides()
        self.assertEqual(self.app.current_window.winfo_exists(), 1)

    @patch("tkinter.PhotoImage", side_effect=lambda file, **kwargs: file)
    def test_show_desserts(self, mock_photoimage):
        self.app.show_desserts()
        self.assertEqual(self.app.current_window.winfo_exists(), 1)

    def test_add_to_cart(self):
        item = {"name": "Burger", "price": 10}
        self.app.add_to_cart(item)
        self.assertEqual(len(self.app.cart), 1)
        self.assertEqual(self.app.cart[0]["name"], "Burger")

    def test_calculate_total_cost(self):
        item1 = {"name": "Burger", "price": 10, "quantity": 2}
        item2 = {"name": "Pizza", "price": 12, "quantity": 1}
        self.app.cart = [item1, item2]
        self.app.tip = 5
        total_cost = self.app.calculate_total_cost()
        self.assertEqual(total_cost, (10 * 2 + 12) + 5)

    def test_clear_cart(self):
        self.app.cart = [{"name": "Burger", "price": 10, "quantity": 2}]
        self.app.clear_cart()
        self.assertEqual(len(self.app.cart), 0)

if __name__ == "__main__":
    unittest.main()