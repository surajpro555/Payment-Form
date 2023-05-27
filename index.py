from tkinter import *
from tkinter.messagebox import *
import sqlite3,time
import pyttsx3

#------------------------------------------Audio------------------------------------------

engine=pyttsx3.init()
def speaknow():
    engine.say(f'..{UNAME.get()}.....Payment Successful')
    engine.runAndWait()
    engine.stop()

#--------------------------------------WINDOW----------------------------------------------

root = Tk()
root.title("Payment Form")
width = 640
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

#--------------------------------------VARIABLES-------------------------------------------

USERNAME = StringVar()
PASSWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
UNAME=StringVar()
CARD=StringVar()
MONTH=StringVar()
YEAR=StringVar()
CVV=StringVar()
MONEY=StringVar()
ACC1=StringVar()
ACC2=StringVar()
AMT=StringVar()
REC=StringVar()
IFSC=StringVar()

#------------------------------------------Database------------------------------------------
def Database():
    global conn, cursor
    conn = sqlite3.connect("db_member.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT)")
    
 #------------------------------------------LOGIN------------------------------------------

def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP, pady=40)
    Label(LoginFrame,text='').grid(row=1)
    lbl_username = Label(LoginFrame, text="Username:", font=('arial', 20), bd=18)
    lbl_username.grid(row=2)
    lbl_password = Label(LoginFrame, text="Password:", font=('arial', 20), bd=18)
    lbl_password.grid(row=3)
    lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
    lbl_result1.grid(row=4, columnspan=2)
    username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=2, column=1)
    password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=3, column=1)
    btn_login = Button(LoginFrame, text="Login", font=('arial', 18),bg='lightblue',activeforeground='red',activebackground='orange', width=20, command=Login)
    btn_login.grid(row=5, columnspan=2, pady=20)
    lbl_register = Label(LoginFrame, text="Register", fg="Blue", font=('arial', 12))
    lbl_register.grid(row=0, sticky=W)
    lbl_register.bind('<Button-1>', shift_Register)

#------------------------------------------Register------------------------------------------

def RegisterForm():
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP, pady=40)
    lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = Label(RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=5, columnspan=2)
    username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=3, column=1)
    lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
    lastname.grid(row=4, column=1)
    btn_login = Button(RegisterFrame, text="Register", font=('arial', 18),bg='lightblue',activeforeground='red',activebackground='orange', width=20, command=Register)
    btn_login.grid(row=6, columnspan=2, pady=20)
    lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', shift_Login)

#------------------------------------------Shifting Frame----------------------------------

def shift_Login(event=None):
    RegisterFrame.destroy()
    LoginForm()

def shift_Register(event=None):
    LoginFrame.destroy()
    RegisterForm()

def shift_payment(event=None):
    LoginFrame.destroy()
    Payment1()

def shift_payment2(event=None):
    window.destroy()
    Payment2()    

#------------------------------------------INSERTING-----------------------------------------
def Register():
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get() == "":
        lbl_result2.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Username is already taken", fg="red")
        else:
            cursor.execute("INSERT INTO `member` (username, password, firstname, lastname) VALUES(?, ?, ?, ?)", (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
            conn.commit()
            USERNAME.set("")
            PASSWORD.set("")
            FIRSTNAME.set("")
            LASTNAME.set("")
            lbl_result2.config(text="Successfully Created!", fg="black")
        cursor.close()
        conn.close()

#------------------------------------------VALIDATE------------------------------------------

def Login():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?",(USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            c=sqlite3.connect('db_member.db').cursor()
            c.execute('''SELECT * FROM member''')
            data = c.fetchall() 
            print(data)
            shift_payment()
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")

#------------------------------------------Payment1------------------------------------------          

def Payment1():
    global window
    window=Frame(root)
    window.pack(side=TOP,pady=5)
    Label(window, text="Welcome to KPAY",fg='blue',font=15).pack()
    Label(window,text="").pack()
    Label(window, text="Card Holder's Name").pack()
    name= Entry(window,textvariable=UNAME,width=30).pack()
    Label(window,text="").pack()
    Label(window, text="Enter the Card Number").pack()
    card_Number= Entry(window, textvariable=CARD,width=30).pack()
    Label(window,text="").pack()
    Label(window, text="Expiry Month").pack()
    exp_month= Entry(window, textvariable=MONTH).pack()
    Label(window,text="").pack()
    Label(window, text="Expiry Year").pack()
    exp_year= Entry(window, textvariable=YEAR).pack()
    Label(window,text="").pack()
    Label(window, text="CVV").pack()
    Entry(window, textvariable=CVV,width=10).pack()
    Label(window,text="").pack()
    Button(window, text="Procced", width=30, height=1,bg='lightblue',command=validation1).pack()

#------------------------------------------Payment2------------------------------------------

def Payment2():
    global w
    w=Frame(root)
    w.pack(side=TOP,pady=20)
    Label(w, text="Recipient details",fg='blue',font=15).pack()
    Label(w, text="Name").pack()
    e0=Entry(w,textvariable=REC,width=30).pack()
    Label(w,text="").pack()
    Label(w, text="Account Number").pack()
    e1=Entry(w,textvariable=ACC1,width=30).pack()
    Label(w,text="").pack()
    Label(w,text="Re-enter the account number").pack()
    e1=Entry(w,textvariable=ACC2,width=30).pack()
    Label(w,text="").pack()
    Label(w,text='IFSC CODE').pack()
    e2=Entry(w,textvariable=IFSC,width=30).pack()
    Label(w,text="").pack()
    Label(w,text="Amount").pack()
    e3=Entry(w, textvariable=MONEY,width=20).pack()
    Label(w,text="").pack()
    Button(w, text="Pay", width=30, height=1,bg='lightblue',command=validation2).pack()

#------------------------------------------Validation------------------------------------------

def validation1():
    cg=CARD.get()
    mg=MONTH.get()
    if(not cg.isnumeric() or len(cg) != 16):
        showwarning('','Wrong Card Number',icon="error")
    elif len(mg)>2 or not mg.isnumeric() or 12<int(mg) or int(mg)<0:
        showwarning('Warning','Wrong Month',icon="error")
    elif len(YEAR.get())>4 or not YEAR.get().isnumeric():
        showwarning('warning','Wrong Year',icon="error")        
    elif len(CVV.get())!=3 or not CVV.get().isnumeric():
        showwarning('','Wrong CVV',icon="error")
    else:
        shift_payment2()    

def validation2():
    if ACC1.get()!=ACC2.get() or not ACC2.get().isdigit():
        showwarning('Warning','Wrong Account Details',icon='warning')
    elif askyesno('','Are you sure to pay'):
        conn1=sqlite3.connect("db_history.db")
        cursor1=conn1.cursor()
        cursor1.execute("CREATE TABLE IF NOT EXISTS `history` (H_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, recipient TEXT, Amount TEXT, IFSC TEXT)")
        cursor1.execute("INSERT INTO `history` (username, recipient,Amount,IFSC) VALUES(?, ?, ?, ?)",(str(UNAME.get()), str(REC.get()),AMT.get(), str(IFSC.get())))
        conn1.commit()
        cursor1.execute('''SELECT * FROM history''')
        print(cursor1.fetchall())
        conn1.close()
        speaknow()
        payment_successful()

# ---------------------- PAYMENT SUCCESSFUL------------------------#

def payment_successful(event=None):
    root.destroy()
    f=Tk()
    f.title('Payment Succesful')
    f.geometry('600x400')
    p=PhotoImage(file='image.png')
    Label(f,image=p,height=400,width=350).pack()
    f.mainloop()

# --------------------------- MAIN --------------------------------#
LoginForm()
root.mainloop()