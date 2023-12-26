import tkinter as tk
import csv

class NumberConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Kalkulator Konversi Bilangan")

        self.label_decimal = tk.Label(master, text="Decimal:")
        self.entry_decimal = tk.Entry(master)
        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.import_button = tk.Button(master, text="Import",command=self.save_results_to_txt)

        self.binary_label = tk.Label(master, text="Binary:")
        self.binary_result = tk.StringVar()
        self.binary_result_label = tk.Label(master, textvariable=self.binary_result)

        self.octal_label = tk.Label(master, text="Octal:")
        self.octal_result = tk.StringVar()
        self.octal_result_label = tk.Label(master, textvariable=self.octal_result)

        self.hex_label = tk.Label(master, text="Hexadecimal:")
        self.hex_result = tk.StringVar()
        self.hex_result_label = tk.Label(master, textvariable=self.hex_result)

        self.layout_widgets()

    def layout_widgets(self):
        self.label_decimal.grid(row=0, column=0, pady=10)
        self.entry_decimal.grid(row=0, column=1, pady=10)
        self.convert_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.import_button.grid(row=1, column=0, columnspan=1, pady=10)

        self.binary_label.grid(row=2, column=0, pady=5)
        self.binary_result_label.grid(row=2, column=1, pady=5)
        self.octal_label.grid(row=3, column=0, pady=5)
        self.octal_result_label.grid(row=3, column=1, pady=5)
        self.hex_label.grid(row=4, column=0, pady=5)
        self.hex_result_label.grid(row=4, column=1, pady=5)

    def convert(self):
        try:
            decimal_value = int(self.entry_decimal.get())
            self.binary_result.set(bin(decimal_value)[2:])
            self.octal_result.set(oct(decimal_value)[2:])
            self.hex_result.set(hex(decimal_value)[2:])
        except ValueError:
            self.binary_result.set("Invalid Input")
            self.octal_result.set("Invalid Input")
            self.hex_result.set("Invalid Input")
    
    def save_results_to_txt(self):
        try:
            decimal_value = int(self.entry_decimal.get())
            binary_value = bin(decimal_value)[2:]
            octal_value = oct(decimal_value)[2:]
            hex_value = hex(decimal_value)[2:]

            with open("hasil.txt", 'a') as txtfile:
                txtfile.write(f"Decimal: {decimal_value}\n")
                txtfile.write(f"---------------\n")
                txtfile.write(f"Binary: {binary_value}\n")
                txtfile.write(f"Octal: {octal_value}\n")
                txtfile.write(f"Hexadecimal: {hex_value}\n\n")

            print("SAVE SUCCES TO 'hasil.txt'")
        except ValueError:
            print("Invalid Input")
            

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberConverterApp(root)
    root.mainloop()
