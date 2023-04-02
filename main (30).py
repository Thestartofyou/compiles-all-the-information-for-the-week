import sqlite3
from datetime import datetime
from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfFileMerger, PdfFileReader

# Create or connect to the SQLite database
conn = sqlite3.connect('work_db.db')
c = conn.cursor()

# Create tables for notes, purchases, and mileage
c.execute('''CREATE TABLE IF NOT EXISTS notes
             (id INTEGER PRIMARY KEY, note TEXT, created_at TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS purchases
             (id INTEGER PRIMARY KEY, vendor TEXT, amount REAL, receipt_path TEXT, created_at TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS mileage
             (id INTEGER PRIMARY KEY, distance REAL, start_location TEXT, end_location TEXT, created_at TEXT)''')

# Create a table for pay stubs
c.execute('''CREATE TABLE IF NOT EXISTS paystubs
             (id INTEGER PRIMARY KEY, employee_name TEXT, hours_worked REAL, hourly_rate REAL, gross_pay REAL, taxes REAL, net_pay REAL, created_at TEXT)''')

# GUI for note-taking
def take_note():
    note_window = Toplevel()
    note_window.title('Take a note')

    note_label = Label(note_window, text='Note:')
    note_label.pack()

    note_text = Text(note_window)
    note_text.pack()

    def save_note():
        note = note_text.get('1.0', 'end')
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("INSERT INTO notes (note, created_at) VALUES (?, ?)", (note, created_at))
        conn.commit()
        note_window.destroy()

    save_button = Button(note_window, text='Save', command=save_note)
    save_button.pack()

# GUI for adding a purchase
def add_purchase():
    purchase_window = Toplevel()
    purchase_window.title('Add a purchase')

    vendor_label = Label(purchase_window, text='Vendor:')
    vendor_label.pack()

    vendor_entry = Entry(purchase_window)
    vendor_entry.pack()

    amount_label = Label(purchase_window, text='Amount:')
    amount_label.pack()

    amount_entry = Entry(purchase_window)
    amount_entry.pack()

    def browse_receipt():
        receipt_path = filedialog.askopenfilename()
        receipt_path_label.config(text=receipt_path)

    receipt_label = Label(purchase_window, text='Receipt:')
    receipt_label.pack()

    receipt_path_label = Label(purchase_window, text='')
    receipt_path_label.pack()

    browse_button = Button(purchase_window, text='Browse', command=browse_receipt)
    browse_button.pack()

    def save_purchase():
        vendor = vendor_entry.get()
        amount = amount_entry.get()
        receipt_path = receipt_path_label.cget('text')
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("INSERT INTO purchases (vendor, amount, receipt_path, created_at) VALUES (?, ?, ?, ?)", (vendor, amount, receipt_path, created_at))
        conn.commit()
        purchase_window.destroy()

    save_button = Button(purchase_window, text='Save', command=save_purchase)
    save_button.pack()

# GUI for tracking mileage
def track_mileage

