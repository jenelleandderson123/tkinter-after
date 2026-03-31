import tkinter as tk

def convert():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text="Centimeters: " + str(cm))
    except:
        result_label.config(text="Enter a valid number")

window = tk.Tk()
window.title("Inches to Centimeters Converter")
window.geometry("300x200")

tk.Label(window, text="Enter length in inches").pack()
entry = tk.Entry(window)
entry.pack()

tk.Button(window, text="Convert", command=convert).pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()