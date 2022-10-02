import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error
import pandas as pd

win = tk.Tk()
win.title("Search And Update") 

win.iconbitmap(r'pz.ico')


lpid = ttk.Label(win, text="Pizza ID : ")
lpid.grid(column=0, row=0, sticky=tk.W)

pid = tk.StringVar()
tpid = ttk.Entry(win, width=20, textvariable=pid)
tpid.grid(column=1, row=0)

lpname = ttk.Label(win, text="Name : ")
lpname.grid(column=0, row=1)

pname = tk.StringVar()
tpname = ttk.Entry(win, width=20, textvariable=pname)
tpname.grid(column=1, row=1)
tpname.config(state='disable')

ldesc = ttk.Label(win, text="Description : ")
ldesc.grid(column=0, row=2)

desc = tk.StringVar()
tdesc = ttk.Entry(win, width=20, textvariable=desc)
tdesc.grid(column=1, row=2)
tdesc.config(state='disable')

lvnv = ttk.Label(win, text="Category : ")
lvnv.grid(column=0, row=3)

vnv = tk.StringVar() 									
v = tk.Radiobutton(win, text='Veg', variable=vnv, value='V') 
v.grid(column=1, row=3, sticky=tk.W) 						
nv=tk.Radiobutton(win, text='Non Veg', variable=vnv, value='NV') 
nv.grid(column=2, row=3, sticky=tk.W)
v.config(state='disable')
nv.config(state='disable')

ltyp = ttk.Label(win, text="Crust : ")
ltyp.grid(column=0, row=4)

typ = tk.StringVar()
tp = ttk.Combobox(win, width=12, textvariable=typ, state='readonly') 
tp['values'] = ('World Famous Pan Pizzas', 'Hand Tossed Big Pizza', 'Magic Pan')
tp.grid(column=1, row=4)
tp.current(0)
tp.config(state='disable')

ls = ttk.Label(win, text="Size : ")
ls.grid(column=0, row=5)

sl = tk.StringVar()
s = ttk.Combobox(win, width=12, textvariable=sl, state='readonly') 
s['values'] = ('Personal','Medium', 'King')
s.grid(column=1, row=5)
s.current(0)
s.config(state='disable')

lcst = ttk.Label(win, text="Price : ")
lcst.grid(column=0, row=6)

cst = tk.StringVar()
tcst = ttk.Entry(win, width=20, textvariable=cst)
tcst.grid(column=1, row=6)
tcst.config(state='disable')

def _msgBox():
    try:
     conn = mysql.connector.connect(host='localhost',database='pizza',user='root',password='root',charset='utf8')
     cursor = conn.cursor()
     row = cursor.execute("update menu set pname='"+pname.get()+"', description='"+desc.get()+"',vnv='"+vnv.get()+"', type='"+typ.get()+"', size='"+sl.get()+"', cost='"+cst.get()+"' where pid="+pid.get())
     if(cursor.rowcount>0):
         mBox.showinfo('Done!', 'Updated!')
         pid.set('')
         pname.set('')
         desc.set('')
         vnv.set('')
         typ.set('')
         sl.set('')
         cst.set('')         
         
     else:
         print('Not Done!')
    except Error as e :
     print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")
        conn.commit()

def _fill():
    try:
     
        conn = mysql.connector.connect(host='localhost',database='pizza',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select * from menu where pid="+pid.get())
        ls = pd.DataFrame(cursor.fetchall())
        if(len(ls.index)>0):
            pid.set(ls.iloc[0][0])
            pname.set(ls.iloc[0][1])
            desc.set(ls.iloc[0][2])
            vnv.set(ls.iloc[0][3])
            typ.set(ls.iloc[0][4])
            sl.set(ls.iloc[0][5])
            cst.set(ls.iloc[0][6])
            tpname.config(state='enable')
            tdesc.config(state='enable')
            tp.config(state='enable')
            s.config(state='enable')
            tcst.config(state='enable')
            v.config(state='normal')
            nv.config(state='normal')
            
        else:
            mBox.showinfo('Error', 'Pizza Doesnt Exist')
    except Error as e :
        print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")
        conn.commit()

search = ttk.Button(win, text="Search!", command=_fill) 
search.grid(column=0, row=7)

submit = ttk.Button(win, text="Update!", command=_msgBox) 
submit.grid(column=1, row=7)

def back():
    win.quit()
    win.destroy()
    import modmenu

submit = ttk.Button(win, text="Back", command=back) 
submit.grid(column=2, row=7)
    


    


for child in win.winfo_children():
    child.grid_configure(padx=30, pady=30)
 
win.mainloop()

