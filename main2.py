import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())

        today = datetime.today()
        birth_date = datetime(year, month, day)

        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text="Your Age: " + str(age))
    except:
        result_label.config(text="Enter a valid date")

window = tk.Tk()
window.title("Age Calculator")
window.geometry("300x250")

tk.Label(window, text="Day").pack()
entry_day = tk.Entry(window)
entry_day.pack()

tk.Label(window, text="Month").pack()
entry_month = tk.Entry(window)
entry_month.pack()

tk.Label(window, text="Year").pack()
entry_year = tk.Entry(window)
entry_year.pack()

tk.Button(window, text="Calculate Age", command=calculate_age).pack(pady=10)


result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()