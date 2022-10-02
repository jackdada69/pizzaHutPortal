import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error

win = tk.Tk()
win.title("Insert Into Menu") 

win.iconbitmap(r'pz.ico')


lpid = ttk.Label(win, text="Pizza ID : ")
lpid.grid(column=0, row=0, sticky=tk.W)

pid = tk.StringVar()
tpid = ttk.Entry(win, width=20, textvariable=pid)
tpid.grid(column=1, row=0)

conn = mysql.connector.connect(host='localhost',database='pizza',user='root',password='root',charset='utf8')
cursor = conn.cursor()
row = cursor.execute("select max(pid) from menu")
ls=cursor.fetchall()
pid.set(str(ls[0][0]+1))

lpname = ttk.Label(win, text="Name : ")
lpname.grid(column=0, row=1)

pname = tk.StringVar()
tpname = ttk.Entry(win, width=20, textvariable=pname)
tpname.grid(column=1, row=1)

ldesc = ttk.Label(win, text="Description : ")
ldesc.grid(column=0, row=2)

desc = tk.StringVar()
tdesc = ttk.Entry(win, width=20, textvariable=desc)
tdesc.grid(column=1, row=2)

lvnv = ttk.Label(win, text="Category : ")
lvnv.grid(column=0, row=3)

vnv = tk.StringVar() 									
v = tk.Radiobutton(win, text='Veg', variable=vnv, value='V') 
v.grid(column=1, row=3, sticky=tk.W) 						
nv=tk.Radiobutton(win, text='Non Veg', variable=vnv, value='NV') 
nv.grid(column=2, row=3, sticky=tk.W)

ltyp = ttk.Label(win, text="Crust : ")
ltyp.grid(column=0, row=4)

typ = tk.StringVar()
tp = ttk.Combobox(win, width=12, textvariable=typ, state='readonly') 
tp['values'] = ('World Famous Pan Pizzas', 'Hand Tossed Big Pizza', 'Magic Pan')
tp.grid(column=1, row=4)

ls = ttk.Label(win, text="Size : ")
ls.grid(column=0, row=5)

sl = tk.StringVar()
s = ttk.Combobox(win, width=12, textvariable=sl, state='readonly') 
s['values'] = ('Personal','Medium')
s.grid(column=1, row=5)
s.current(0)

lcst = ttk.Label(win, text="Price : ")
lcst.grid(column=0, row=6)

cst = tk.StringVar()
tcst = ttk.Entry(win, width=20, textvariable=cst)
tcst.grid(column=1, row=6)

def _msgBox():
    try:
     
     conn = mysql.connector.connect(host='localhost',database='pizza',user='root',password='root',charset='utf8')
     cursor = conn.cursor()
     row = cursor.execute("insert into menu values("+pid.get()+", '"+pname.get()+"', '("+desc.get()+")', '"+vnv.get()+"', '"+typ.get()+"','"+sl.get()+"','"+cst.get()+"');")
     if(cursor.rowcount>0):
         mBox.showinfo('Added!')
         pid.set(str(int(pid.get())+1))
         sl.set('')
         cst.set('')
     else:
         print('Not Done!')
    except Error as e :
     print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")
        conn.commit()

submit = ttk.Button(win, text="Insert", command=_msgBox) 
submit.grid(column=1, row=7)
for child in win.winfo_children():
    child.grid_configure(padx=30, pady=30)

def back():
         win.quit()
         win.destroy()
         import modmenu
         
bk = ttk.Button(win, text="Back", command=back) 
bk.grid(column=2, row=7)

win.mainloop()
