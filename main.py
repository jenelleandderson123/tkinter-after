import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        P = float(entry_principal.get())
        R = float(entry_rate.get())
        T = float(entry_time.get())
        N = float(entry_period.get())

        SI = (P * R * T) / 100

        CI = P * ((1 + (R / (100 * N))) ** (N * T)) - P

        result_label.config(
            text=f"Simple Interest: {SI:.2f}\nCompound Interest: {CI:.2f}"
        )

    except:
        messagebox.showerror("Error", "Enter valid numbers!")

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x300")

tk.Label(root, text="Principal Amount").pack()
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Rate of Interest (%)").pack()
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Time (years)").pack()
entry_time = tk.Entry(root)
entry_time.pack()

tk.Label(root, text="Compounding Period (times per year)").pack()
entry_period = tk.Entry(root)
entry_period.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()