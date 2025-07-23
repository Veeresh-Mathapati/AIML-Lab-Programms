import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

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
            location TEXT NOT NULL
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

# ---------------- UI Setup ----------------
root = tk.Tk()
root.title("Employee Management System - Infosys Style")
root.geometry("800x550")
root.resizable(False, False)

style = ttk.Style()
style.theme_use('clam')

# Define styles for labels and buttons
style.configure("BoldBlue.TLabel", foreground='darkblue', font=('Segoe UI', 10, 'bold'))
style.configure("TEntry", font=('Segoe UI', 10))
style.configure("TCombobox", font=('Segoe UI', 10))
style.configure("Treeview", font=('Segoe UI', 10), rowheight=25)
style.configure("BoldButton.TButton", font=('Segoe UI', 10, 'bold'), foreground='white', background='#0078D7')
style.map("BoldButton.TButton",
          foreground=[('active', 'white')],
          background=[('active', '#005A9E')])

selected_emp_id = None
departments = ["HR", "Finance", "Engineering", "Marketing", "Sales", "Support"]
locations = ["India", "America", "China", "Russia"]

# Top Frame (Form)
form_frame = ttk.LabelFrame(root, text="Employee Details", padding=20)
form_frame.pack(fill='x', padx=20, pady=10)

ttk.Label(form_frame, text="Name:", style="BoldBlue.TLabel").grid(row=0, column=0, padx=5, pady=5, sticky='w')
name_entry = ttk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(form_frame, text="Department:", style="BoldBlue.TLabel").grid(row=1, column=0, padx=5, pady=5, sticky='w')
dept_combo = ttk.Combobox(form_frame, values=departments, state='readonly', width=28)
dept_combo.grid(row=1, column=1, padx=5, pady=5)
dept_combo.current(0)

ttk.Label(form_frame, text="Email:", style="BoldBlue.TLabel").grid(row=2, column=0, padx=5, pady=5, sticky='w')
email_entry = ttk.Entry(form_frame, width=30)
email_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(form_frame, text="Location:", style="BoldBlue.TLabel").grid(row=3, column=0, padx=5, pady=5, sticky='w')
location_combo = ttk.Combobox(form_frame, values=locations, state='readonly', width=28)
location_combo.grid(row=3, column=1, padx=5, pady=5)
location_combo.current(0)

def clear_form():
    global selected_emp_id
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    dept_combo.current(0)
    location_combo.current(0)
    selected_emp_id = None
    add_btn.config(text="Add Employee")

def add_or_update_employee():
    global selected_emp_id
    name = name_entry.get().strip()
    dept = dept_combo.get()
    email = email_entry.get().strip()
    location = location_combo.get()

    if not name or not email or not location:
        messagebox.showwarning("Validation Error", "All fields are required.")
        return

    if selected_emp_id:
        update_employee(selected_emp_id, name, dept, email, location)
        messagebox.showinfo("Updated", "Employee updated successfully!")
    else:
        insert_employee(name, dept, email, location)
        messagebox.showinfo("Added", "Employee added successfully!")

    clear_form()

add_btn = ttk.Button(form_frame, text="Add Employee", style="BoldButton.TButton", command=add_or_update_employee)
add_btn.grid(row=4, column=1, sticky='e', pady=10)

# Search Frame
search_frame = ttk.Frame(root)
search_frame.pack(fill='x', padx=20, pady=5)

ttk.Label(search_frame, text="Search:", style="BoldBlue.TLabel").pack(side='left', padx=5)
search_entry = ttk.Entry(search_frame, width=30)
search_entry.pack(side='left', padx=5)

def perform_search():
    query = search_entry.get().strip()
    results = search_employees(query)
    refresh_employee_list(results)

ttk.Button(search_frame, text="Search", style="BoldButton.TButton", command=perform_search).pack(side='left', padx=5)
ttk.Button(search_frame, text="Reset", style="BoldButton.TButton", command=lambda: refresh_employee_list()).pack(side='left', padx=5)

# Table Frame
table_frame = ttk.Frame(root)
table_frame.pack(fill='both', expand=True, padx=20, pady=10)

columns = ("id", "name", "department", "email", "location")
employee_table = ttk.Treeview(table_frame, columns=columns, show='headings', height=10)
employee_table.heading("id", text="ID")
employee_table.heading("name", text="Name")
employee_table.heading("department", text="Department")
employee_table.heading("email", text="Email")
employee_table.heading("location", text="Location")

employee_table.column("id", width=50, anchor='center')
employee_table.column("name", width=150)
employee_table.column("department", width=150)
employee_table.column("email", width=200)
employee_table.column("location", width=120)

employee_table.pack(fill='both', expand=True)

def on_table_select(event):
    global selected_emp_id
    selected = employee_table.selection()
    if not selected:
        return
    values = employee_table.item(selected[0])['values']
    selected_emp_id = values[0]
    name_entry.delete(0, tk.END)
    name_entry.insert(0, values[1])
    dept_combo.set(values[2])
    email_entry.delete(0, tk.END)
    email_entry.insert(0, values[3])
    location_combo.set(values[4])
    add_btn.config(text="Update Employee")

employee_table.bind("<<TreeviewSelect>>", on_table_select)

# Bottom Frame
bottom_frame = ttk.Frame(root)
bottom_frame.pack(fill='x', padx=20, pady=10)

def delete_selected():
    selected = employee_table.selection()
    if not selected:
        messagebox.showwarning("Delete Error", "Select an employee to delete.")
        return

    emp_id = employee_table.item(selected[0])['values'][0]
    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this employee?")
    if confirm:
        delete_employee(emp_id)
        clear_form()
        messagebox.showinfo("Deleted", "Employee deleted successfully!")

ttk.Button(bottom_frame, text="Delete Selected Employee", style="BoldButton.TButton", command=delete_selected).pack(anchor='e')

# Refresh table
def refresh_employee_list(data=None):
    for row in employee_table.get_children():
        employee_table.delete(row)

    if data is None:
        data = get_all_employees()

    for emp in data:
        employee_table.insert("", tk.END, values=emp)

# Init
connect_db()
refresh_employee_list()
root.mainloop()
