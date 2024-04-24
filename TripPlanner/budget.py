from tkinter import *
import tkinter as tk


def create_budget(parent):
    # Setting up the window
    budget_window = Toplevel(parent)
    budget_window.title("Budget")
    budget_window.configure(background="#111F4D")
    budget_window.resizable(False, False)

    # Positioning the application
    window_width = 900
    window_height = 700

    screen_width = budget_window.winfo_screenwidth()
    screen_height = budget_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    budget_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    font_budget = ('Arial', 20, 'italic')
    font_bud = ('Arial', 15, 'italic')

    font_button = ('Arial', 15, 'italic')

    budget_label = Label(budget_window,
                         text="Budget Calculator",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_budget)
    budget_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')
    budget_label = Label(budget_window,
                         text="Enter your destination",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_bud)
    budget_label.grid(row=1, column=0, columnspan=3, padx=20, pady=10, sticky='w')

    entry_field = Entry(budget_window, width=50, justify="left")
    entry_field.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    budget_label = Label(budget_window,
                         text="Enter duration of trip",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_bud)
    budget_label.grid(row=2, column=0, columnspan=3, padx=20, pady=10, sticky='w')

    duration_entry = Entry(budget_window, width=50, justify="left")
    duration_entry.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    budget_label = Label(budget_window,
                         text="Enter your Budget",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_bud)
    budget_label.grid(row=3, column=0, columnspan=3, padx=20, pady=10, sticky='w')

    budget_entry = Entry(budget_window, width=50, justify="left")
    budget_entry.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    budget_label = Label(budget_window,
                         text="Enter the number of people",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_bud)
    budget_label.grid(row=4, column=0, columnspan=3, padx=20, pady=10, sticky='w')

    people_entry = Entry(budget_window, width=50, justify="left")
    people_entry.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    budget_label = Label(budget_window,
                         text="Enter percentage of budget for hotel (in %)",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_bud)
    budget_label.grid(row=5, column=0, columnspan=3, padx=20, pady=10, sticky='w')

    hotel_entry = Entry(budget_window, width=50, justify="left")
    hotel_entry.grid(row=5, column=1, columnspan=3, padx=10, pady=10, sticky='n')

    budget_label = Label(budget_window,
                         text="Enter percentage of budget for travel (in %)",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_bud)
    budget_label.grid(row=6, column=0, columnspan=3, padx=20, pady=10, sticky='w')

    travel_entry = Entry(budget_window, width=50, justify="left")
    travel_entry.grid(row=6, column=1, columnspan=3, padx=10, pady=10, sticky='n')

    budget_label = Label(budget_window,
                         text="Enter percentage of budget for food (in %)",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_bud)
    budget_label.grid(row=7, column=0, columnspan=3, padx=20, pady=10, sticky='w')

    food_entry = Entry(budget_window, width=50, justify="left")
    food_entry.grid(row=7, column=1, columnspan=3, padx=10, pady=10, sticky='n')

    budget_label = Label(budget_window,
                         text="Enter percentage of budget for activities (in %)",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_bud)
    budget_label.grid(row=8, column=0, columnspan=3, padx=20, pady=10, sticky='w')

    activities_entry = Entry(budget_window, width=50, justify="left")
    activities_entry.grid(row=8, column=2, columnspan=3, padx=10, pady=10, sticky='n')

    budget_label = Label(budget_window,
                         text="Enter percentage of budget for miscellaneous (in %)",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_bud)
    budget_label.grid(row=9, column=0, columnspan=3, padx=20, pady=10, sticky='w')

    misc_entry = Entry(budget_window, width=50, justify="left")
    misc_entry.grid(row=9, column=2, columnspan=3, padx=10, pady=10, sticky='n')

    def show_budget():
        destination = entry_field.get()
        total_budget = float(budget_entry.get())
        num_people = int(people_entry.get())
        trip_duration = int(duration_entry.get())
        hotel_percentage = float(hotel_entry.get()) / 100
        travel_percentage = float(travel_entry.get()) / 100
        food_percentage = float(food_entry.get()) / 100
        activities_percentage = float(activities_entry.get()) / 100
        misc_percentage = float(misc_entry.get()) / 100

        hotel_budget = total_budget * hotel_percentage
        travel_budget = total_budget * travel_percentage
        food_budget = total_budget * food_percentage
        activities_budget = total_budget * activities_percentage
        misc_budget = total_budget * misc_percentage

        per_person_budget = total_budget / num_people
        per_day_budget = total_budget / trip_duration

        result_window = Toplevel(budget_window)
        result_window.title("Budget Results")
        result_window.geometry("400x300")
        result_window.configure(background="#111F4D")

        Label(result_window, text=f"Destination: {destination}", fg='#f7f7f7', bg='#111F4D').pack(pady=5)
        Label(result_window, text=f"Per Person Budget: ${per_person_budget:.2f}", fg='#f7f7f7', bg='#111F4D').pack(
            pady=5)
        Label(result_window, text=f"Per Day Budget: ${per_day_budget:.2f}", fg='#f7f7f7', bg='#111F4D').pack(
            pady=5)
        Label(result_window, text=f"Hotel Budget: ${hotel_budget:.2f}", fg='#f7f7f7', bg='#111F4D').pack(pady=5)
        Label(result_window, text=f"Travel Budget: ${travel_budget:.2f}", fg='#f7f7f7', bg='#111F4D').pack(pady=5)
        Label(result_window, text=f"Food Budget: ${food_budget:.2f}", fg='#f7f7f7', bg='#111F4D').pack(pady=5)
        Label(result_window, text=f"Activities Budget: ${activities_budget:.2f}", fg='#f7f7f7', bg='#111F4D').pack(
            pady=5)
        Label(result_window, text=f"Miscellaneous Budget: ${misc_budget:.2f}", fg='#f7f7f7', bg='#111F4D').pack(
            pady=5)

    show_button = Button(budget_window, text="Show Budget", command=show_budget, font=font_button)
    show_button.grid(row=10, column=0, columnspan=3, padx=10, pady=10)

    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(budget_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(budget_window, parent),
                  font=font_button
                  )
    Back.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='w')

    budget_window.grid_columnconfigure(0, weight=1, uniform="group1")
    budget_window.grid_columnconfigure(1, weight=1, uniform="group1")
    budget_window.grid_columnconfigure(2, weight=1, uniform="group1")

    budget_window.grid_rowconfigure(2, weight=0)
    budget_window.grid_rowconfigure(3, weight=0)
    budget_window.grid_rowconfigure(4, weight=0)
    budget_window.grid_rowconfigure(5, weight=0)
    budget_window.grid_rowconfigure(6, weight=0)
    budget_window.grid_rowconfigure(7, weight=0)
    budget_window.grid_rowconfigure(8, weight=0)
    budget_window.grid_rowconfigure(9, weight=0)
    budget_window.grid_rowconfigure(10, weight=0)

    budget_window.mainloop()


if __name__ == "__main__":
    window = tk.Tk()
    create_budget(window)
    window.mainloop()
