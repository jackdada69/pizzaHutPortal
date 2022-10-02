import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error

win = tk.Tk() 	
win.title("Payment Portal")

win.iconbitmap(r'pz.ico')



ltotal = ttk.Label(win, text="Amount Due : ")
ltotal.grid(column=0, row=1)

total = tk.StringVar()
ttotal = ttk.Entry(win, width=20, textvariable=total)
ttotal.grid(column=1, row=1)
ttotal.config(state='disable')
conn = mysql.connector.connect(host='localhost',database='pizza',user='root',password='root',charset='utf8')
cursor = conn.cursor()
row1 = cursor.execute("select sum(n.qty*m.cost) from norder n, menu m where n.pname=m.pname and n.size=m.size")
tot=cursor.fetchall()
total.set(str(tot[0][0]))



ldisc = ttk.Label(win, text="Discount % : ")
ldisc.grid(column=0, row=2)

disc = tk.StringVar()
tdisc = ttk.Entry(win, width=20, textvariable=disc)
tdisc.grid(column=1, row=2)

lmode = ttk.Label(win, text="Payment Mode : ")
lmode.grid(column=0, row=3)

mode = tk.StringVar()
tmode = ttk.Combobox(win, width=12, textvariable=mode, state='readonly') 
tmode['values'] = ('Cash', 'Credit Card', 'Paytm', 'Google Pay', 'Bhim UPI')
tmode.grid(column=1, row=3)
tmode.current(0)

ono = tk.StringVar()
conn = mysql.connector.connect(host='localhost',database='pizza',user='root',password='root',charset='utf8')
cursor = conn.cursor()
row = cursor.execute("select max(ono) from norder")
ls=cursor.fetchall()
ono.set(str(ls[0][0]))

def get_disc():
    total.set(str(int(total.get()) - int(disc.get())))

def _msgBox():
    try:
     
     conn = mysql.connector.connect(host='localhost',database='pizza',user='root',password='root',charset='utf8')
     cursor = conn.cursor()
     row = cursor.execute("update norder set mode = '"+mode.get()+"' where ono="+ono.get()+";")
     row1=cursor.execute("insert into ordhst values ( curdate(),"+ono.get()+","+disc.get()+","+total.get()+");")
     if(cursor.rowcount>0):
         mBox.showinfo('Payment Succesful!', 'Yor pizza is on its way!!')
         mode.set('')
         ono.set('')
         total.set('')
         win.quit()
         win.destroy()
         import MainWindow
     else:
         print('Payment Failed!')
    except Error as e :
     print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")
        conn.commit()

action = ttk.Button(win, text="Pay", command=_msgBox) 
action.grid(column=1, row=4)

discount = ttk.Button(win, text="Discount", command=get_disc) 
discount.grid(column=0, row=4)

for child in win.winfo_children():
    child.grid_configure(padx=30, pady=30)
    
win.mainloop()

