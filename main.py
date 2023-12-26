import tkinter as tk

def convert():
    try:
        decimal_value = int(entry_decimal.get())
        binary_result.set(bin(decimal_value)[2:])
        octal_result.set(oct(decimal_value)[2:])
        hex_result.set(hex(decimal_value)[2:])
    except ValueError:
        binary_result.set("Invalid Input")
        octal_result.set("Invalid Input")
        hex_result.set("Invalid Input")

window = tk.Tk()
window.title("Kalkulator Konversi Bilangan")

label_decimal = tk.Label(window, text="Decimal:")
entry_decimal = tk.Entry(window)
convert_button = tk.Button(window, text="Convert",command=convert)
import_button = tk.Button(window, text="Import")


binary_label = tk.Label(window, text="Binary:")
binary_result = tk.StringVar()
binary_result_label = tk.Label(window, textvariable=binary_result)

octal_label = tk.Label(window, text="Octal:")
octal_result = tk.StringVar()
octal_result_label = tk.Label(window, textvariable=octal_result)

hex_label = tk.Label(window, text="Hexadecimal:")
hex_result = tk.StringVar()
hex_result_label = tk.Label(window, textvariable=hex_result)

label_decimal.grid(row=0, column=0, pady=10)
entry_decimal.grid(row=0, column=1, pady=10)
convert_button.grid(row=1, column=0, columnspan=2, pady=10)
import_button.grid(row=1, column=0, columnspan=1, pady=10)

binary_label.grid(row=2, column=0, pady=5)
binary_result_label.grid(row=2, column=1, pady=5)
octal_label.grid(row=3, column=0, pady=5)
octal_result_label.grid(row=3, column=1, pady=5)
hex_label.grid(row=4, column=0, pady=5)
hex_result_label.grid(row=4, column=1, pady=5)

window.mainloop()