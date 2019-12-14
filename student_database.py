# Ahmed Raja
# Student Database

import tkinter as tk
from tkinter import messagebox
from db import Database

# Instanciate database object
db = Database('data.db')

# Main Application/GUI class
class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Student Database')
        # Width height
        master.geometry("950x500")
        # Create widgets/grid
        self.create_widgets()
        # Init selected item var
        self.selected_item = 0
        # Populate initial list
        self.populate_list()

    def create_widgets(self):
        # Widgets
        subtitles = ['Name', 'Age', 'Period 1 Class', 'Period 1 Teacher', 'Period 2 Class', 'Period 2 Teacher', 'Period 3 Class', 'Period 3 Teacher', 'Period 4 Class', 'Period 4 Teacher', 'Period 5 Class', 'Period 5 Teacher']
        self.texts = [None]*12
        self.labels = [None]*12
        self.entries = [None]*12

        # Text Fields
        for i in range(12):
            self.texts[i] = tk.StringVar()
            self.labels[i] = tk.Label(self.master, text=(subtitles[i]), font=('bold', 14))
            self.labels[i].grid(row=i, column=2, sticky=tk.W)
            self.entries[i] = tk.Entry(self.master, textvariable=self.texts[i])
            self.entries[i].grid(row=i, column=3)

        # Buttons
        self.add_btn = tk.Button(
            self.master, text="Add Student", width=12, command=self.add_item)
        self.add_btn.grid(row=12, column=3, columnspan=1, pady=5)

        self.remove_btn = tk.Button(
            self.master, text="Remove Student", width=12, command=self.remove_item)
        self.remove_btn.grid(row=13, column=3, columnspan=1, pady=5)

        self.update_btn = tk.Button(
            self.master, text="Update Student", width=12, command=self.update_item)
        self.update_btn.grid(row=14, column=3, columnspan=1, pady=5)

        self.exit_btn = tk.Button(
            self.master, text="Clear Input", width=12, command=self.clear_text)
        self.exit_btn.grid(row=15, column=3, columnspan=1, pady=5)

        # Student List (listbox)
        self.student_list = tk.Listbox(
            self.master, height=29, width=65, border=0)
        self.student_list.grid(
            row=0, column=0, columnspan=1, rowspan=16, pady=5, padx=10)

        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=0, column=1, rowspan=29, sticky='ns')
        # Set scrollbar to student
        self.student_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.student_list.yview)

        # Bind select
        self.student_list.bind('<<ListboxSelect>>', self.select_item)

    def populate_list(self):
        # Delete items before update. So when you keep pressing it doesnt keep getting (show example by calling this twice)
        self.student_list.delete(0, tk.END)
        # Loop through records
        for row in db.fetch():
            # Insert into list
            self.student_list.insert(tk.END, row)

    # Add new item
    def add_item(self):
        if self.texts[0].get() == '' or self.texts[1].get() == '' or self.texts[2].get() == '' or self.texts[3].get() == '' or self.texts[4].get() == '' or self.texts[5].get() == '' or self.texts[6].get() == '' or self.texts[7].get() == '' or self.texts[8].get() == '' or self.texts[9].get() == '' or self.texts[10].get() == '' or self.texts[11].get() == '':
            messagebox.showerror("Required Fields", "Please fill in all fields.")
            return
        print(self.texts[0].get())
        # Insert into DB
        db.insert(self.texts[0].get(), self.texts[1].get(), self.texts[2].get(), self.texts[3].get(), self.texts[4].get(), self.texts[5].get(), self.texts[6].get(), self.texts[7].get(), self.texts[8].get(), self.texts[9].get(), self.texts[10].get(), self.texts[11].get())
        # Clear list
        self.student_list.delete(0, tk.END)
        # Insert into list
        self.student_list.insert(tk.END, (self.texts[0].get(), self.texts[1].get(), self.texts[2].get(), self.texts[3].get(), self.texts[4].get(), self.texts[5].get(), self.texts[6].get(), self.texts[7].get(), self.texts[8].get(), self.texts[9].get(), self.texts[10].get(), self.texts[11].get()))
        self.clear_text()
        self.populate_list()

    # Runs when item is selected
    def select_item(self, event):
        # # Create global selected item to use in other functions
        # global self.selected_item
        try:
            # Get index
            index = self.student_list.curselection()[0]
            # Get selected item
            self.selected_item = self.student_list.get(index)
            # print(selected_item) # Print tuple

            # Add text to entries
            for i in range(12):
                self.entries[i].delete(0, tk.END)
                self.entries[i].insert(tk.END, self.selected_item[i+1])
        except IndexError:
            pass

    # Remove item
    def remove_item(self):
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()

    # Update item
    def update_item(self):
        db.update(self.selected_item[0], self.texts[0].get(), self.texts[1].get(), self.texts[2].get(), self.texts[3].get(), self.texts[4].get(), self.texts[5].get(), self.texts[6].get(), self.texts[7].get(), self.texts[8].get(), self.texts[9].get(), self.texts[10].get(), self.texts[11].get())
        self.populate_list()

    # Clear all text fields

    def clear_text(self):
        for i in range(12):
            self.entries[i].delete(0, tk.END)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
