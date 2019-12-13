import tkinter as tk
from tkinter import messagebox
from db import Database

# Instanciate database object
db = Database('data.db')

# Widgets
# array_order -> [name, age, p1class, p1teacher, p2class, p2teacher, p3class, p3teacher, p4class, p4teacher, p5class, p5teacher]
texts = []
labels = []
entries = []

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

        # Name
        self.name_text = tk.StringVar()
        self.name_label = tk.Label(self.master, text='Name', font=('bold', 14))
        self.name_label.grid(row=0, column=2, sticky=tk.W)
        self.name_entry = tk.Entry(self.master, textvariable=self.name_text)
        self.name_entry.grid(row=0, column=3)
        # Age
        self.age_text = tk.StringVar()
        self.age_label = tk.Label(self.master, text='Age', font=('bold', 14))
        self.age_label.grid(row=1, column=2, sticky=tk.W)
        self.age_entry = tk.Entry(self.master, textvariable=self.age_text)
        self.age_entry.grid(row=1, column=3)
        # P1class
        self.p1class_text = tk.StringVar()
        self.p1class_label = tk.Label(self.master, text='Period 1 Class', font=('bold', 14))
        self.p1class_label.grid(row=2, column=2, sticky=tk.W)
        self.p1class_entry = tk.Entry(self.master, textvariable=self.p1class_text)
        self.p1class_entry.grid(row=2, column=3)
        # p1teacher
        self.p1teacher_text = tk.StringVar()
        self.p1teacher_label = tk.Label(self.master, text='Period 1 Teacher', font=('bold', 14))
        self.p1teacher_label.grid(row=3, column=2, sticky=tk.W)
        self.p1teacher_entry = tk.Entry(self.master, textvariable=self.p1teacher_text)
        self.p1teacher_entry.grid(row=3, column=3)
        # P2class
        self.p2class_text = tk.StringVar()
        self.p2class_label = tk.Label(self.master, text='Period 2 Class', font=('bold', 14))
        self.p2class_label.grid(row=4, column=2, sticky=tk.W)
        self.p2class_entry = tk.Entry(self.master, textvariable=self.p2class_text)
        self.p2class_entry.grid(row=4, column=3)
        # p2teacher
        self.p2teacher_text = tk.StringVar()
        self.p2teacher_label = tk.Label(self.master, text='Period 2 Teacher', font=('bold', 14))
        self.p2teacher_label.grid(row=5, column=2, sticky=tk.W)
        self.p2teacher_entry = tk.Entry(self.master, textvariable=self.p2teacher_text)
        self.p2teacher_entry.grid(row=5, column=3)
        # p3class
        self.p3class_text = tk.StringVar()
        self.p3class_label = tk.Label(self.master, text='Period 3 Class', font=('bold', 14))
        self.p3class_label.grid(row=6, column=2, sticky=tk.W)
        self.p3class_entry = tk.Entry(self.master, textvariable=self.p3class_text)
        self.p3class_entry.grid(row=6, column=3)
        # p3teacher
        self.p3teacher_text = tk.StringVar()
        self.p3teacher_label = tk.Label(self.master, text='Period 3 Teacher', font=('bold', 14))
        self.p3teacher_label.grid(row=7, column=2, sticky=tk.W)
        self.p3teacher_entry = tk.Entry(self.master, textvariable=self.p3teacher_text)
        self.p3teacher_entry.grid(row=7, column=3)
        # p4class
        self.p4class_text = tk.StringVar()
        self.p4class_label = tk.Label(self.master, text='Period 4 Class', font=('bold', 14))
        self.p4class_label.grid(row=8, column=2, sticky=tk.W)
        self.p4class_entry = tk.Entry(self.master, textvariable=self.p4class_text)
        self.p4class_entry.grid(row=8, column=3)
        # p4teacher
        self.p4teacher_text = tk.StringVar()
        self.p4teacher_label = tk.Label(self.master, text='Period 4 Teacher', font=('bold', 14))
        self.p4teacher_label.grid(row=9, column=2, sticky=tk.W)
        self.p4teacher_entry = tk.Entry(self.master, textvariable=self.p4teacher_text)
        self.p4teacher_entry.grid(row=9, column=3)
        # p5class
        self.p5class_text = tk.StringVar()
        self.p5class_label = tk.Label(self.master, text='Period 5 Class', font=('bold', 14))
        self.p5class_label.grid(row=10, column=2, sticky=tk.W)
        self.p5class_entry = tk.Entry(self.master, textvariable=self.p5class_text)
        self.p5class_entry.grid(row=10, column=3)
        # p5teacher
        self.p5teacher_text = tk.StringVar()
        self.p5teacher_label = tk.Label(self.master, text='Period 5 Teacher', font=('bold', 14))
        self.p5teacher_label.grid(row=11, column=2, sticky=tk.W)
        self.p5teacher_entry = tk.Entry(self.master, textvariable=self.p5teacher_text)
        self.p5teacher_entry.grid(row=11, column=3)

        # Buttons
        self.add_btn = tk.Button(self.master, text="Add Student", width=12, command=self.add_item)
        self.add_btn.grid(row=12, column=3, columnspan=1, pady=5)

        self.remove_btn = tk.Button(self.master, text="Remove Student", width=12, command=self.remove_item)
        self.remove_btn.grid(row=13, column=3, columnspan=1, pady=5)

        self.update_btn = tk.Button(self.master, text="Update Student", width=12, command=self.update_item)
        self.update_btn.grid(row=14, column=3, columnspan=1, pady=5)

        self.exit_btn = tk.Button(self.master, text="Clear Input", width=12, command=self.clear_text)
        self.exit_btn.grid(row=15, column=3, columnspan=1, pady=5)

        # student list (listbox)
        self.student_list = tk.Listbox(self.master, height=29, width=65, border=0)
        self.student_list.grid(row=0, column=0, columnspan=1, rowspan=16, pady=5, padx=10)
        
        # Scrolling is also built in to the Listbox. (tested on macOS)
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
        if self.name_text.get() == '' or self.age_text.get() == '' or self.p1class_text.get() == '' or self.p1teacher_text.get() == '' or self.p2class_text.get() == '' or self.p2teacher_text.get() == '' or self.p3class_text.get() == '' or self.p3teacher_text.get() == '' or self.p4class_text.get() == '' or self.p4teacher_text.get() == '' or self.p5class_text.get() == '' or self.p5teacher_text.get() == '':
            messagebox.showerror("Required Fields", "Please include all fields")
            return
        print(self.name_text.get())
        # Insert into DB
        db.insert(self.name_text.get(), self.age_text.get(), self.p1class_text.get(), self.p1teacher_text.get(), self.p2class_text.get(), self.p2teacher_text.get(), self.p3class_text.get(), self.p3teacher_text.get(), self.p4class_text.get(), self.p4teacher_text.get(), self.p5class_text.get(), self.p5teacher_text.get())
        # Clear list
        self.student_list.delete(0, tk.END)
        # Insert into list
        self.student_list.insert(tk.END, (self.name_text.get(), self.age_text.get(), self.p1class_text.get(), self.p1teacher_text.get(), self.p2class_text.get(), self.p2teacher_text.get(), self.p3class_text.get(), self.p3teacher_text.get(), self.p4class_text.get(), self.p4teacher_text.get(), self.p5class_text.get(), self.p5teacher_text.get()))
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
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, self.selected_item[1])
            self.age_entry.delete(0, tk.END)
            self.age_entry.insert(tk.END, self.selected_item[2])
            self.p1class_entry.delete(0, tk.END)
            self.p1class_entry.insert(tk.END, self.selected_item[3])
            self.p1teacher_entry.delete(0, tk.END)
            self.p1teacher_entry.insert(tk.END, self.selected_item[4])
            self.p2class_entry.delete(0, tk.END)
            self.p2class_entry.insert(tk.END, self.selected_item[3])
            self.p2teacher_entry.delete(0, tk.END)
            self.p2teacher_entry.insert(tk.END, self.selected_item[4])
            self.p3class_entry.delete(0, tk.END)
            self.p3class_entry.insert(tk.END, self.selected_item[3])
            self.p3teacher_entry.delete(0, tk.END)
            self.p3teacher_entry.insert(tk.END, self.selected_item[4])
            self.p4class_entry.delete(0, tk.END)
            self.p4class_entry.insert(tk.END, self.selected_item[3])
            self.p4teacher_entry.delete(0, tk.END)
            self.p4teacher_entry.insert(tk.END, self.selected_item[4])
            self.p5class_entry.delete(0, tk.END)
            self.p5class_entry.insert(tk.END, self.selected_item[3])
            self.p5teacher_entry.delete(0, tk.END)
            self.p5teacher_entry.insert(tk.END, self.selected_item[4])
        except IndexError:
            pass

    # Remove item
    def remove_item(self):
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()

    # Update item
    def update_item(self):
        db.update(self.selected_item[0], self.name_text.get(), self.age_text.get(), self.p1class_text.get(), self.p1teacher_text.get(), self.p2class_text.get(), self.p2teacher_text.get(), self.p3class_text.get(), self.p3teacher_text.get(), self.p4class_text.get(), self.p4teacher_text.get(), self.p5class_text.get(), self.p5teacher_text.get())
        self.populate_list()

    # Clear all text fields

    def clear_text(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.p1class_entry.delete(0, tk.END)
        self.p1teacher_entry.delete(0, tk.END)
        self.p2class_entry.delete(0, tk.END)
        self.p2teacher_entry.delete(0, tk.END)
        self.p3class_entry.delete(0, tk.END)
        self.p3teacher_entry.delete(0, tk.END)
        self.p4class_entry.delete(0, tk.END)
        self.p4teacher_entry.delete(0, tk.END)
        self.p5class_entry.delete(0, tk.END)
        self.p5teacher_entry.delete(0, tk.END)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
