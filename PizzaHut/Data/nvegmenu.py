import pandas as pd
import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error


win = tk.Tk()
win.title("Veg Menu") 

try:
     
    conn = mysql.connector.connect(host='localhost',database='pizza',user='root',password='root',charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from menu where vnv='nv'")
    ls = pd.DataFrame(cursor.fetchall())

    ttk.Label(win, text="Pizza ID").grid(column=0, row=0, sticky=tk.W, columnspan=20)
    ttk.Label(win, text="Pizza Name").grid(column=1, row=0, sticky=tk.W, columnspan=20)
    ttk.Label(win, text="Description").grid(column=2, row=0, sticky=tk.W, columnspan=701)
    ttk.Label(win, text="Veg/Non Veg").grid(column=3, row=0, sticky=tk.W, columnspan=20)
    ttk.Label(win, text="Crust").grid(column=4, row=0, sticky=tk.W, columnspan=25)
    ttk.Label(win, text="Size").grid(column=5, row=0, sticky=tk.W, columnspan=20)
    ttk.Label(win, text="Price").grid(column=6, row=0, sticky=tk.W, columnspan=20)
    
    
    for i in range(0, len(ls.index)):
        for j in range(0, len(ls.columns)):
            b = tk.Entry(win)
            b.insert(0, ls.iloc[i][j])
            b.grid(row=i+1, column=j)
            if(j==0):
                b.config(state = "readonly", width = 10)
            elif(j==2):
                b.config(state = 'readonly', width=70)
            elif(j==4):
                b.config(state = "readonly", width = 25)
            else:
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
