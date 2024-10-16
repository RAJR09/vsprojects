import tkinter as tk
from datetime import date, timedelta

def create_calendar():
   
    root = tk.Tk()
    root.title("Calendar Application")

    
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    for col, day in enumerate(days_of_week):
        label_day = tk.Label(root, text=day, padx=10, pady=5)
        label_day.grid(row=0, column=col)

   
    current_date = date.today()

    
    first_day = date(current_date.year, current_date.month, 1)
    days_in_month = (date(current_date.year, current_date.month + 1, 1) - first_day).days

   
    day_labels = []
    for day in range(1, days_in_month + 1):
        label_day = tk.Label(root, text=str(day), padx=10, pady=5)
        day_labels.append(label_day)

    
    for day, label_day in enumerate(day_labels, start=1):
        row = (first_day.weekday() + day) // 7 + 1
        col = (first_day.weekday() + day) % 7
        label_day.grid(row=row, column=col)

    
    root.mainloop()


create_calendar()




