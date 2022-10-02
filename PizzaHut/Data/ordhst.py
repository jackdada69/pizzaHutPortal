import pandas as pd
import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error


win = tk.Tk()
win.title("Order History") 


win.iconbitmap('pz.ico')


def back():
    win.quit()
    win.destroy()
    import MainWindow

action = ttk.Button(win, text="Back", command=back) 
action.grid(column=0, row=0)

try:    
    conn = mysql.connector.connect(host='localhost',database='pizza',user='root',password='root',charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from ordhst group by date")
    ls = pd.DataFrame(cursor.fetchall())

        

    ttk.Label(win, text="Order Date").grid(column=0, row=1, sticky=tk.W, columnspan=20)
    ttk.Label(win, text="Order No").grid(column=1, row=1, sticky=tk.W, columnspan=20)
    ttk.Label(win, text="Discount").grid(column=2, row=1, sticky=tk.W, columnspan=20)
    ttk.Label(win, text="Order Total").grid(column=3, row=1, sticky=tk.W, columnspan=20)
        
        
    for i in range(0, len(ls.index)):
        for j in range(0, len(ls.columns)):
            b = tk.Entry(win)
            b.insert(0, ls.iloc[i][j])
            b.grid(row=i+2, column=j)
            b.config(state = "readonly", width = 20)
    conn.commit()
    conn.close()
except Error as e :
    print("Error while connecting to MySQL", e)
finally:
    print("MySQL connection is closed")

for child in win.winfo_children():
    child.grid_configure(padx=5, pady=5)

win.mainloop()
