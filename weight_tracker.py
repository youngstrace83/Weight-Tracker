import tkinter as tk
from tkinter import ttk
import sqlite3

class WeightTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weight and Calorie Tracker")
        self.master.geometry("800x600")

        # Create database connection
        self.conn = sqlite3.connect('weight_tracker.db')
        self.create_tables()

        # Create and show the main menu
        self.show_main_menu()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            height REAL,
            weight REAL,
            activity_level TEXT,
            goal TEXT
        )
        ''')
        self.conn.commit()

    def show_main_menu(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Button(main_frame, text="Create Profile", command=self.show_create_profile).grid(row=0, column=0, pady=10)
        ttk.Button(main_frame, text="View Profile", command=self.show_profile).grid(row=1, column=0, pady=10)
        ttk.Button(main_frame, text="Track Weight", command=self.show_weight_tracker).grid(row=2, column=0, pady=10)
        ttk.Button(main_frame, text="Calorie Calculator", command=self.show_calorie_calculator).grid(row=3, column=0, pady=10)

    def show_create_profile(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        profile_frame = ttk.Frame(self.master, padding="10")
        profile_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(profile_frame, text="Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.name_entry = ttk.Entry(profile_frame)
        self.name_entry.grid(row=0, column=1, pady=5)

        ttk.Label(profile_frame, text="Age:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.age_entry = ttk.Entry(profile_frame)
        self.age_entry.grid(row=1, column=1, pady=5)

        ttk.Label(profile_frame, text="Gender:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.gender_var = tk.StringVar()
        ttk.Radiobutton(profile_frame, text="Male", variable=self.gender_var, value="Male").grid(row=2, column=1, sticky=tk.W, pady=5)
        ttk.Radiobutton(profile_frame, text="Female", variable=self.gender_var, value="Female").grid(row=2, column=2, sticky=tk.W, pady=5)

        ttk.Label(profile_frame, text="Height (cm):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.height_entry = ttk.Entry(profile_frame)
        self.height_entry.grid(row=3, column=1, pady=5)

        ttk.Label(profile_frame, text="Weight (kg):").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.weight_entry = ttk.Entry(profile_frame)
        self.weight_entry.grid(row=4, column=1, pady=5)

        ttk.Label(profile_frame, text="Activity Level:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.activity_var = tk.StringVar()
        activity_levels = ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"]
        ttk.Combobox(profile_frame, textvariable=self.activity_var, values=activity_levels).grid(row=5, column=1, pady=5)

        ttk.Label(profile_frame, text="Goal:").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.goal_var = tk.StringVar()
        ttk.Radiobutton(profile_frame, text="Lose Weight", variable=self.goal_var, value="Lose").grid(row=6, column=1, sticky=tk.W, pady=5)
        ttk.Radiobutton(profile_frame, text="Gain Weight", variable=self.goal_var, value="Gain").grid(row=6, column=2, sticky=tk.W, pady=5)

        ttk.Button(profile_frame, text="Save Profile", command=self.save_profile).grid(row=7, column=0, columnspan=3, pady=20)
        ttk.Button(profile_frame, text="Back to Main Menu", command=self.show_main_menu).grid(row=8, column=0, columnspan=3)

    def save_profile(self):
        # TODO: Implement profile saving logic
        print("Profile saved!")
        self.show_main_menu()

    def show_profile(self):
        # TODO: Implement profile viewing logic
        print("Showing profile...")
        self.show_main_menu()

    def show_weight_tracker(self):
        # TODO: Implement weight tracking logic
        print("Showing weight tracker...")
        self.show_main_menu()

    def show_calorie_calculator(self):
        # TODO: Implement calorie calculator logic
        print("Showing calorie calculator...")
        self.show_main_menu()

if __name__ == "__main__":
    root = tk.Tk()
    app = WeightTrackerApp(root)
    root.mainloop()
