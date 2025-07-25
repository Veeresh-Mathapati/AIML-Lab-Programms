import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import re

# ---------------- Database Setup ----------------
def connect_db():
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute(''' 
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            email TEXT NOT NULL,
            location TEXT NOT NULL DEFAULT 'Unknown'
        )
    ''')
    conn.commit()
    conn.close()

def insert_employee(name, department, email, location):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO employee (name, department, email, location) VALUES (?, ?, ?, ?)",
                (name, department, email, location))
    conn.commit()
    conn.close()
    refresh_employee_list()

def delete_employee(emp_id):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM employee WHERE id = ?", (emp_id,))
    conn.commit()
    conn.close()
    refresh_employee_list()

def update_employee(emp_id, name, department, email, location):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("UPDATE employee SET name=?, department=?, email=?, location=? WHERE id=?",
                (name, department, email, location, emp_id))
    conn.commit()
    conn.close()
    refresh_employee_list()

def get_all_employees():
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    conn.close()
    return rows

def search_employees(query):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM employee 
                   WHERE name LIKE ? OR department LIKE ? OR location LIKE ?""",
                (f'%{query}%', f'%{query}%', f'%{query}%'))
    rows = cur.fetchall()
    conn.close()
    return rows

# ---------------- Styling ----------------
style = ttk.Style()
style.theme_use('clam')

FONT_LABEL = ('Segoe UI', 12, 'bold')
FONT_ENTRY = ('Segoe UI', 11)
COLOR_FRAME = '#C5CAE9'
COLOR_ACCENT = '#3F51B5'
COLOR_TEXT = '#283593'
COLOR_ALT_ROW = '#BBDEFB'
COLOR_BUTTON_BG = '#FFEB3B'
COLOR_BUTTON_ACTIVE = '#FBC02D'
COLOR_HEADER = '#1E88E5'
COLOR_HIGHLIGHT = '#FF4081'

style.configure('TLabel', background=COLOR_FRAME, foreground=COLOR_TEXT, font=FONT_LABEL)
style.configure('TEntry', fieldbackground='#FFFFFF', foreground=COLOR_TEXT, font=FONT_ENTRY)
style.configure('TCombobox', fieldbackground='#FFFFFF', background='#FFFFFF', foreground=COLOR_TEXT, font=FONT_ENTRY)
style.configure('TButton', font=('Segoe UI', 12, 'bold'), foreground='black', background=COLOR_BUTTON_BG)
style.map('TButton', background=[('active', COLOR_BUTTON_ACTIVE)], foreground=[('active', 'black')])
style.configure('Treeview', background=COLOR_FRAME, fieldbackground=COLOR_FRAME, foreground=COLOR_TEXT, rowheight=30, font=FONT_ENTRY)
style.configure('Treeview.Heading', background=COLOR_HEADER, foreground='white', font=('Segoe UI', 12, 'bold'))
style.map('Treeview', background=[('selected', COLOR_HIGHLIGHT)], foreground=[('selected', 'white')])

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Employee Management System - Modern UI")
root.geometry("950x650")
root.resizable(True, True)

root.grid_rowconfigure(0, weight=1, minsize=100)
root.grid_rowconfigure(1, weight=1, minsize=200)
root.grid_rowconfigure(2, weight=3)
root.grid_columnconfigure(0, weight=1)

selected_emp_id = None  # For editing tracking

# ---------------- Employee Form ----------------
form_frame = ttk.LabelFrame(root, text="Employee Details", padding=15)
form_frame.grid(row=0, column=0, padx=25, pady=20, sticky='ew')

ttk.Label(form_frame, text="Name:", style="TLabel").grid(row=1, column=0, padx=10, pady=6, sticky='w')
name_entry = ttk.Entry(form_frame, width=40)
name_entry.grid(row=1, column=1, padx=10, pady=6, sticky='ew')

ttk.Label(form_frame, text="Department:", style="TLabel").grid(row=2, column=0, padx=10, pady=6, sticky='w')
dept_combo = ttk.Combobox(form_frame, values=["HR", "Finance", "Engineering", "Marketing", "Sales", "Support"], state='readonly', width=38)
dept_combo.grid(row=2, column=1, padx=10, pady=6, sticky='ew')
dept_combo.current(0)

ttk.Label(form_frame, text="Email:", style="TLabel").grid(row=3, column=0, padx=10, pady=6, sticky='w')
email_entry = ttk.Entry(form_frame, width=40)
email_entry.grid(row=3, column=1, padx=10, pady=6, sticky='ew')

ttk.Label(form_frame, text="Location:", style="TLabel").grid(row=4, column=0, padx=10, pady=6, sticky='w')
location_combo = ttk.Combobox(form_frame, values=["India", "America", "China", "Russia"], state='readonly', width=38)
location_combo.grid(row=4, column=1, padx=10, pady=6, sticky='ew')
location_combo.current(0)

def clear_form():
    global selected_emp_id
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    dept_combo.current(0)
    location_combo.current(0)
    selected_emp_id = None
    add_btn.config(text="Add Employee")

def validate_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

def add_or_update_employee():
    global selected_emp_id
    name = name_entry.get().strip()
    dept = dept_combo.get()
    email = email_entry.get().strip()
    location = location_combo.get()

    if not name or not email:
        messagebox.showwarning("Validation Error", "All fields are required.")
        return

    if not validate_email(email):
        messagebox.showwarning("Validation Error", "Invalid email address.")
        return

    if selected_emp_id:
        update_employee(selected_emp_id, name, dept, email, location)
        messagebox.showinfo("Success", "Employee updated.")
    else:
        insert_employee(name, dept, email, location)
        messagebox.showinfo("Success", "Employee added.")

    clear_form()

add_btn = ttk.Button(form_frame, text="Add Employee", command=add_or_update_employee)
add_btn.grid(row=5, column=1, sticky='e', pady=10)

# ---------------- Search Frame ----------------
search_frame = ttk.Frame(root)
search_frame.grid(row=1, column=0, padx=25, pady=10, sticky='ew')

ttk.Label(search_frame, text="Search:", style="TLabel").grid(row=0, column=0, padx=8)
search_entry = ttk.Entry(search_frame, width=40)
search_entry.grid(row=0, column=1, padx=8)

dept_filter = ttk.Combobox(search_frame, values=["All", "HR", "Finance", "Engineering", "Marketing", "Sales", "Support"], state='readonly', width=15)
dept_filter.set("All")
dept_filter.grid(row=0, column=3, padx=8)

location_filter = ttk.Combobox(search_frame, values=["All", "India", "America", "China", "Russia"], state='readonly', width=15)
location_filter.set("All")
location_filter.grid(row=0, column=5, padx=8)

def filter_employees():
    query = search_entry.get().strip()
    dept = dept_filter.get()
    location = location_filter.get()
    results = search_employees(query)
    filtered = [r for r in results if (dept == "All" or r[2] == dept) and (location == "All" or r[4] == location)]
    refresh_employee_list(filtered)

ttk.Button(search_frame, text="Search", command=filter_employees).grid(row=0, column=6, padx=8)

# ---------------- Employee Table ----------------
table_frame = ttk.Frame(root)
table_frame.grid(row=2, column=0, padx=25, pady=20, sticky='nsew')

columns = ("id", "name", "department", "email", "location")
employee_table = ttk.Treeview(table_frame, columns=columns, show='headings', height=10)
for col in columns:
    employee_table.heading(col, text=col.capitalize())

employee_table.column("id", width=50, anchor='center')
employee_table.column("name", width=180)
employee_table.column("department", width=140)
employee_table.column("email", width=220)
employee_table.column("location", width=120)
employee_table.pack(fill='both', expand=True)

def refresh_employee_list(data=None):
    for row in employee_table.get_children():
        employee_table.delete(row)
    data = data or get_all_employees()
    for i, emp in enumerate(data):
        tag = 'oddrow' if i % 2 else 'evenrow'
        employee_table.insert("", tk.END, values=emp, tags=(tag,))
    employee_table.tag_configure('oddrow', background=COLOR_ALT_ROW)
    employee_table.tag_configure('evenrow', background=COLOR_FRAME)

def on_row_select(event):
    global selected_emp_id
    selected = employee_table.focus()
    if not selected:
        return
    values = employee_table.item(selected, 'values')
    selected_emp_id = values[0]
    name_entry.delete(0, tk.END)
    name_entry.insert(0, values[1])
    dept_combo.set(values[2])
    email_entry.delete(0, tk.END)
    email_entry.insert(0, values[3])
    location_combo.set(values[4])
    add_btn.config(text="Update Employee")

employee_table.bind('<<TreeviewSelect>>', on_row_select)

# ---------------- Run ----------------
connect_db()
refresh_employee_list()
root.mainloop()
