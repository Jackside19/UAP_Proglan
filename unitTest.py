import unittest
import tkinter as tk
from tkinter import StringVar
import pandas as pd
from main import NumberConverterApp  
class TestNumberConverterApp(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = NumberConverterApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_convert_valid_input(self):
        self.app.entry_decimal.insert(0, "42")  
        self.app.convert()
        self.assertEqual(self.app.binary_result.get(), "101010")
        self.assertEqual(self.app.octal_result.get(), "52")
        self.assertEqual(self.app.hex_result.get(), "2a")

    def test_convert_invalid_input(self):
        self.app.entry_decimal.insert(0, "Invalid Input")  #
        self.app.convert()
        self.assertEqual(self.app.binary_result.get(), "Invalid Input")
        self.assertEqual(self.app.octal_result.get(), "Invalid Input")
        self.assertEqual(self.app.hex_result.get(), "Invalid Input")

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestNumberConverterApp))
