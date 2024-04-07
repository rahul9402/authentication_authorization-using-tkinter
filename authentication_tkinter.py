import tkinter.messagebox
from tkinter import *
import mysql.connector

db = mysql.connector.connect(host='localhost', user='root',password='rahul',db='sample')
cursor = db.cursor()

def admin():
    global admin_frame, admin_username, admin_password
    admin_frame = Frame(homepage, width=350, height=200)
    admin_frame.place(x=70,y=130)
    Label(admin_frame, text='Username', font=('calibri',13)).place(x=30,y=30)
    Label(admin_frame, text='Password', font=('calibri',13)).place(x=30,y=80)
    admin_username = StringVar()
    admin_password = StringVar()
    Entry(admin_frame, textvariable=admin_username, font=('calibri',12),
          bg='lightblue').place(x=150,y=30)
    Entry(admin_frame, textvariable=admin_password, font=('calibri',12),
          bg='lightblue').place(x=150,y=80)
    Button(admin_frame, text='Login', font=('calibri',13), bg='blue', fg='white',
           width='10', height='1', command=admin_login).place(x=210,y=130)

def admin_login():
    username = admin_username.get()
    password = admin_password.get()
    if username == 'admin' and password == 'admin@123':
        tkinter.messagebox.showinfo('Authenticate','Welcome Admin')
        admin_home()
    else:
        tkinter.messagebox.showinfo('Authenticate','Invalid')

def admin_home():
    global admin_page
    admin_page = Toplevel(homepage)
    admin_page.geometry('1300x500')
    admin_page.title('Admin Home')
    admin_page.configure(bg='lightblue')
    Button(admin_page, text='Pending List', font=('calibri',13), bg='blue',
           fg='white', width='10', height=1, command=pending).grid(row=0,column=0)
    Button(admin_page, text='Approved List', font=('calibri',13), bg='blue',
           fg='white', width='10', height=1, command=approved).grid(row=0,column=1)

def pending():
    cursor.execute('select * from login_info where Status=False')
    data = cursor.fetchall()
    rows = len(data)
    cols = len(data[0])
    Label(admin_page, text='Id', font=('calibri',13,'bold'),bg='lightblue').grid(row=1,column=0)
    Label(admin_page, text='Name', font=('calibri',13,'bold'),bg='lightblue').grid(row=1,column=1)
    Label(admin_page, text='Mail', font=('calibri',13,'bold'), bg='lightblue').grid(row=1,column=2)
    Label(admin_page, text='Gender', font=('calibri',13,'bold'),bg='lightblue').grid(row=1,column=3)
    Label(admin_page, text='Address', font=('calibri',13,'bold'),bg='lightblue').grid(row=1,column=4)
    Label(admin_page, text='Username', font=('calibri',13,'bold'),bg='lightblue').grid(row=1,column=5)
    Label(admin_page, text='Password', font=('calibri',13,'bold'),bg='lightblue').grid(row=1,column=6)
    Label(admin_page, text='Status', font=('calibri',13,'bold'),bg='lightblue').grid(row=1,column=7)
    Label(admin_page, text='Action', font=('calibri',13,'bold'),bg='lightblue').grid(row=1,column=8)

    for i in range(rows):
        for j in range(cols):
            s = Entry(admin_page, font=('calibri',11))
            s.grid(row=i+2,column=j)
            s.insert(END, data[i][j])
        b1 = Button(admin_page, text='Approve', font=('calibri',10),
                    command=lambda :approve(data[i][0]))
        b1.grid(row=i+2,column=cols+1)
        b2 = Button(admin_page, text='Delete', font=('calibri',10),
                    command=lambda :delete(data[i][0]))
        b2.grid(row=i+2,column=cols+2)

def approve(id):
    cursor.execute('update login_info set Status=True where Id=%s',[id])
    db.commit()
    tkinter.messagebox.showinfo('Authorize','Status Updated')

def delete(id):
    cursor.execute('delete from login_info where Id=%s',[id])
    db.commit()
    tkinter.messagebox.showinfo('Authorize','Deleted')

def approved():
    cursor.execute('select * from login_info where Status=True')
    data = cursor.fetchall()
    rows = len(data)
    cols = len(data[0])
    Label(admin_page, text='Id', font=('calibri',13,'bold'),bg='lightblue').grid(row=1,column=0)
    Label(admin_page, text='Name', font=('calibri',13,'bold'), bg='lightblue').grid(row=1,column=1)
    Label(admin_page, text='Mail', font=('calibri',13,'bold'),bg='lightblue').grid(row=1,column=2)
    Label(admin_page, text='Gender', font=('calibri',13,'bold'),bg='lightblue').grid(row=1,column=3)
    Label(admin_page, text='Address', font=('calibri',13,'bold'),bg='lightblue').grid(row=1,column=4)
    Label(admin_page, text='Username', font=('calibri',13,'bold'),bg='lightblue').grid(row=1,column=5)
    Label(admin_page, text='Password', font=('calibri',13,'bold'),bg='lightblue').grid(row=1,column=6)
    Label(admin_page, text='Status', font=('calibri',13,'bold'),bg='lightblue').grid(row=1,column=7)

    for i in range(rows):
        for j in range(cols):
            s = Entry(admin_page, font=('calibri',11))
            s.grid(row=i+2,column=j)
            s.insert(END, data[i][j])

def user():
    global user_frame, user_username, user_password
    user_frame = Frame(homepage, width=350, height=200)
    user_frame.place(x=470,y=130)
    Label(user_frame, text='Username', font=('calibri',13)).place(x=30,y=30)
    Label(user_frame, text='Password', font=('calibri',13)).place(x=30,y=80)
    user_username = StringVar()
    user_password = StringVar()
    Entry(user_frame, textvariable=user_username, font=('calibri',12),
          bg='lightblue').place(x=150,y=30)
    Entry(user_frame, textvariable=user_password, font=('calibri',12),
          bg='lightblue').place(x=150,y=80)
    Button(user_frame, text='SignUp', font=('calibri',13), bg='blue', fg='white',
           width='10', height='1', command=register).place(x=30,y=130)
    Button(user_frame, text='Login', font=('calibri',13), bg='blue', fg='white',
           width='10', height='1', command=user_login).place(x=210,y=130)

def user_login():
    username = user_username.get()
    password = user_password.get()
    cursor.execute('select * from login_info where Username=%s and Password=%s',
                   [username,password])
    data = cursor.fetchone()
    if data != None:
        tkinter.messagebox.showinfo('Authenticate','Welcome User')
    else:
        tkinter.messagebox.showwarning('Authenticate','Invalid User')


def register():
    global register_frame, register_name, register_mail, register_address
    global register_gender, register_username, register_password
    register_frame = Frame(homepage, width=350, height=400)
    register_frame.place(x=870,y=130)
    Label(register_frame, text='Name', font=('calibri',13)).place(x=30,y=30)
    Label(register_frame, text='Mail', font=('calibri',13)).place(x=30,y=80)
    Label(register_frame, text='Gender', font=('calibri',13)).place(x=30,y=130)
    Label(register_frame, text='Address', font=('calibri',13)).place(x=30,y=180)
    Label(register_frame, text='Username', font=('calibri',13)).place(x=30,y=230)
    Label(register_frame, text='Password', font=('calibri',13)).place(x=30,y=280)
    register_name = StringVar()
    register_mail = StringVar()
    register_address = StringVar()
    register_gender = StringVar()
    register_username = StringVar()
    register_password = StringVar()
    Entry(register_frame, textvariable=register_name, font=('calibri',12),
          bg='lightblue').place(x=150,y=30)
    Entry(register_frame, textvariable=register_mail, font=('calibri',12),
          bg='lightblue').place(x=150,y=80)
    Radiobutton(register_frame, text='Male', variable=register_gender,
                value='Male', font=('calibri',12)).place(x=150,y=130)
    Radiobutton(register_frame, text='Female', variable=register_gender,
                value='Female', font=('calibri',12)).place(x=250,y=130)
    Entry(register_frame, textvariable=register_address, font=('calibri',12),
          bg='lightblue').place(x=150,y=180)
    Entry(register_frame, textvariable=register_username, font=('calibri',12),
          bg='lightblue').place(x=150,y=230)
    Entry(register_frame, textvariable=register_password, font=('calibri',12),
          bg='lightblue').place(x=150,y=280)
    Button(register_frame, text='Submit', font=('calibri',13), bg='blue', fg='white',
           width='10', height='1', command=store_data).place(x=210,y=330)

def store_data():
    name = register_name.get()
    mail = register_mail.get()
    gender = register_gender.get()
    address = register_address.get()
    username = register_username.get()
    password = register_password.get()
    cursor.execute('insert into register(Name,Email,Gender,Address,Username,'
                   'Password) values(%s,%s,%s,%s,%s,%s)',
                   [name,mail,gender,address,username,password])
    db.commit()
    tkinter.messagebox.showinfo('Authenticate','Registered Successfully')

def startpage():
    global homepage
    homepage = Tk()
    homepage.geometry('1300x600')
    homepage.title('Authentication')
    homepage.configure(bg='lightblue')
    Label(homepage, text='Welcome to Login Page', font=('calibri',25)).place(x=450,y=10)
    Button(homepage, text='Admin', font=('calibri',25), bg='blue', fg='white',
           width='10', height='1', command=admin).place(x=100,y=50)
    Button(homepage, text='User', font=('calibri',25), bg='blue', fg='white',
           width='10', height='1', command=user).place(x=1000,y=50)
    homepage.mainloop()

startpage()
