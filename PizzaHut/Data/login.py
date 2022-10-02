
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error

win = tk.Tk() 	
win.title("Pizza")
win.minsize(300, 200)
win.iconbitmap(r'pz.ico')

ulab = ttk.Label(win, text="User ID")
ulab.grid(column=0, row=0)

usr = tk.StringVar()
usrw = ttk.Entry(win, width=20, textvariable=usr)
usrw.grid(column=1, row=0)

upas = ttk.Label(win, text="Password")
upas.grid(column=0, row=1)

pas = tk.StringVar()
pasw = ttk.Entry(win, width=20, textvariable=pas, show='*')
pasw.grid(column=1, row=1)

def _msgBox():
    try:
     
     conn = mysql.connector.connect(host='localhost',
                             database='pizza',
                             user='root',
                             password='root',
                             charset='utf8')
     cursor = conn.cursor()
     cursor.execute("SELECT * FROM login where username='"+usr.get()+"' and password='"+pas.get()+"'")
     ls = cursor.fetchall()
     ls=list(ls[0])
     if(ls):
         mBox.showinfo('Login Successful', 'Welcome '+str(ls[0])+ ' !')
         usr.set('')
         pas.set('')
         win.quit()
         win.destroy()
         import MainWindow
         
    except Error as e :
     print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")
#closing database connection.
'''
if(connection.is_connected()):
            cursor.close()
            connection.close()
    '''
        
'''
    mBox.showinfo('Welcome', usr.get())
    usr.set('gg')
    pas.set('gg')
    '''
				
action = ttk.Button(win, text="Secure Login", command=_msgBox) 
action.grid(column=1, row=3) 

for child in win.winfo_children():
    child.grid_configure(padx=30, pady=30)
    
win.mainloop()
    




