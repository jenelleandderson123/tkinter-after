import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text="Product: " + str(product))
    except:
        result_label.config(text="Enter valid numbers")

window = tk.Tk()
window.title("Product Calculator")
window.geometry("300x200")

tk.Label(window, text="Enter first number").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Enter second number").pack()
entry2 = tk.Entry(window)
entry2.pack()

tk.Button(window, text="Calculate", command=calculate_product).pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()