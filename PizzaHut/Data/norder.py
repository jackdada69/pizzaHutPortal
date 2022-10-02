import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error
import pandas as pd

win = tk.Tk()
win.title("New Order") 

win.iconbitmap(r'pz.ico')

lono = ttk.Label(win, text="Order No : ")
lono.grid(column=0, row=0)

ono = tk.StringVar()
tono = ttk.Entry(win, width=20, textvariable=ono)
tono.grid(column=1, row=0)

conn = mysql.connector.connect(host='localhost',database='pizza',user='root',password='root',charset='utf8')
cursor = conn.cursor()
row = cursor.execute("select max(ono) from norder")
l=cursor.fetchall()
p=None
if(l[0][0]!=p):
    ono.set(str(l[0][0]+1))
else:
    ono.set('1')

conn = mysql.connector.connect(host='localhost',database='pizza',user='root',password='root',charset='utf8')
cursor = conn.cursor()
row = cursor.execute("select distinct (pname) from menu")
lst=pd.DataFrame(cursor.fetchall())

el=[]
for i in range(0, len(lst.index)):
    el.insert(i, lst.loc[i,0])

lpname = ttk.Label(win, text="Pizza Name : ")
lpname.grid(column=0, row=1)

pname = tk.StringVar()
pnm = ttk.Combobox(win, width=12, textvariable=pname, state='readonly') 
pnm['values'] = el
pnm.grid(column=1, row=1)

lsize = ttk.Label(win, text="Size : ")
lsize.grid(column=0, row=2)

size = tk.StringVar() 									
p = tk.Radiobutton(win, text='Personal', variable=size, value='Personal') 
p.grid(column=1, row=2, sticky=tk.W) 						
m=tk.Radiobutton(win, text='Medium', variable=size, value='Medium') 
m.grid(column=2, row=2, sticky=tk.W)

lqty = ttk.Label(win, text="Quantity : ")
lqty.grid(column=0, row=3)

qty = tk.StringVar()
tqty = ttk.Entry(win, width=20, textvariable=qty)
tqty.grid(column=1, row=3)

def _msgBox():
    try:
     
     conn = mysql.connector.connect(host='localhost',database='pizza',user='root',password='root',charset='utf8')
     cursor = conn.cursor()
     row = cursor.execute("insert into norder (ono, pname, size, qty) values("+ono.get()+", '"+pname.get()+"', '"+size.get()+"',"+qty.get()+");")
     if(cursor.rowcount>0):
         pname.set('')
         qty.set('')
     else:
         print('Not Done!')
    except Error as e :
     print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")
        conn.commit()

add = ttk.Button(win, text="Add", command=_msgBox) 
add.grid(column=1, row=8)
for child in win.winfo_children():
    child.grid_configure(padx=30, pady=30)


def placewin():
    _msgBox()
    win.quit()
    win.destroy()
    import placewin


add = ttk.Button(win, text="Add", command=_msgBox) 
add.grid(column=1, row=8)
for child in win.winfo_children():
    child.grid_configure(padx=30, pady=30)
         

place = ttk.Button(win, text="Proceed To Pay", command=placewin, width=20) 
place.grid(column=2, row=8)
for child in win.winfo_children():
    child.grid_configure(padx=30, pady=30)

def back():
         win.quit()
         win.destroy()
         import MainWindow
         
submit1 = ttk.Button(win, text="Back", command=back) 
submit1.grid(column=0, row=8)

win.mainloop()
