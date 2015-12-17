import sqlite3
import webbrowser
import urllib
import ClientMaster
import FixedDeposit
from Tkinter import *
from tkMessageBox import *

con = sqlite3.Connection('Login.db')
cur=con.cursor()
try:
    cur.execute('create table datalogin(username varchar2(15), password varchar2(15),emailid varchar2(20))')
except:
    pass


def crm():
    crmgui=Toplevel()
    crmgui.title('CRM')
    Label(crmgui,text="CRM",fg="red",font=('bold',20)).grid(row=0,column=1,padx=40,columnspan=1,sticky=E+N+S)
    img1=PhotoImage(file="clients_123.gif")
    label=Label(crmgui, image=img1)
    label.image=img1
    label.grid(row=1,column=0)
    Label(crmgui,text="Client Master",fg="red",font=('bold',14)).grid(row=1,column=1,sticky=W)
    Button(crmgui,text="Add Clients",command=ClientMaster.addclient).grid(row=2,column=1,sticky=W)
    Button(crmgui,text="Update Clients",command=ClientMaster.updateclient).grid(row=3,column=1,sticky=W)
    
    Button(crmgui,text="Remove Clients",command=ClientMaster.removeclient).grid(row=4,column=1,sticky=W)
    Button(crmgui,text="Clients List",command=ClientMaster.listclients).grid(row=5,column=1,sticky=W)
    #crmgui.mainloop()

def currentmarket():
    address='https://www.my-eoffice.com/rateh_new_db.php'
    page=urllib.urlopen(address)

    l=list()
    temp=tuple()
    for line in page:
        if '	<div id="box1">' in line:
            break
        if '</div></div><div id="box2"' in line:
            i=line.find('</div></div><div id="box2"')
            incredecre=line[40:i]
            temp+=incredecre,
        if len(temp)==3:
            l.append(temp)
            temp=()
        if 'heading' in line:
            i=line.find('heading')
            start=line.find('>',i)+1
            end=line.find('<',start)
            head=line[start:end]
            temp+=head,
        if '"feeds"' in line:
            i=line.find('"feeds"')
            start=line.find('>',i)+1
            end=line.find('<',start)
            val=line[start:end]
            temp+=val,
    return l
    

def home(username):
    homegui=Tk()
    homegui.title('Home Page')
    bg_image1=PhotoImage(file="back.gif")
    bg_label1=Label(homegui,image=bg_image1)
    bg_label1.image = bg_image1
    bg_label1.place(x=0, y=0, relwidth=1, relheight=1)
    img1=PhotoImage(file="828.gif")
    Label(homegui,image=img1).grid(padx=40,row=0,column=0)
    img2=PhotoImage(file="logo.gif")
    Label(homegui,image=img2).grid(row=0,column=1)
    Label(homegui,text="Welcome "+username[0],fg="red",font=('bold',20)).grid(sticky=E+S+N,row=2,column=0,padx=40,pady=40)
    fm=Frame(homegui)
    fm.grid(row=1)
##    Button(fm,text="Home",command=homegui.bell).grid(row=1,column=0)
    Button(fm,text="CRM",command=crm).grid(row=1,column=1,sticky=W)
    Button(fm,text="Fixed Deposit",command=FixedDeposit.fixed).grid(row=1,column=2,sticky=W)
    def switch():
        homegui.destroy()
        loginwindow()
    Button(fm,text="Logoff",command=switch).grid(row=1,column=3,sticky=W)
    Label(homegui,text="Welcome "+username[0],fg="red",font=('bold',20)).grid(sticky=E+S+N,row=2,column=0,padx=40,pady=40)
    
    li=currentmarket()
    i=0
    fm1=Frame(homegui)
    fm1.grid(row=3,columnspan=4)
    for x in li:
        box=Frame(fm1,relief='raised',bd=3)
        Label(box,text=x[0],relief='raised',width=8).grid(ipadx=10)
        Label(box,text=x[1]).grid()
        Label(box,text=x[2]).grid()
        box.grid(row=3,column=i,pady=40)
        i+=1
    img3=PhotoImage(file="desk_10.gif")
    Label(homegui,image=img3).grid(row=4,column=0,columnspan=2)
    homegui.mainloop()
def loginwindow():
    def callmozilla(event):
        webbrowser.open_new(r"https://www.mozilla.org/en-US/firefox/new/")

    logingui=Tk()
    logingui.title("Wealth e-Office-Login Page")
    
    fm1=Frame()
    fm2=Frame()
    fm3=Frame(fm2)
    
    bg_image1=PhotoImage(file="back.gif")
    bg_label1=Label(fm1,image=bg_image1)
    bg_label1.image = bg_image1
    bg_label1.place(x=0, y=0, relwidth=1, relheight=1)
    img1=PhotoImage(file=r"logo.gif")
    Label(fm1, image=img1).grid(padx=40,pady=20)
    fm1.grid(row=0,column=0)
    img2=PhotoImage(file=r"globe.gif")
    Label(fm2, image=img2).grid(row=0,column=1,sticky=N)
    img3=PhotoImage(file=r"responsive.gif")
    Label(fm1,image=img3).grid(row=1,column=0,padx=40,pady=40)
    Label(fm1,text='''Note:  1. Password is case sensitive. e.g "Admin" and "admin" are different passwords.
            2. After five unsuccessful attempts, your account will be locked.
            3. You should change your password in every 30 days.
            4. All locked accounts will be unlocked automatically after 30 minutes.''',justify=LEFT).grid(row=2,column=0,padx=80,sticky=S+E)
    link=Label(fm1,text="Use Mozilla for better results",fg="blue",cursor="hand2")
    link.grid(row=3,column=0)
    link.bind('<Button-1>',callmozilla)
    Label(fm3, text="Advisor Login",bg="blue",fg="white",font=('bold',16)).grid(row=1,column=0,columnspan=2)
    Label(fm3,text="Username: ").grid(row=2, sticky=N+W+S+E)
    Label(fm3,text="Password: ").grid(row=3, sticky=N+W+S+E)
    
    e1=Entry(fm3)
    e1.grid(row=2, column=1,padx=5,pady=15)
    e2=Entry(fm3,show='*')
    e2.grid(row=3, column=1)
    def clear():
        e1.delete(0,END)
        e2.delete(0,END)
    def signin():
        flagp=flagu=0
        cur.execute("select password from datalogin where password='%s'" %e2.get())
        checkpwd=cur.fetchall()
        if len(checkpwd):
            flagp=1

        cur.execute("select username from datalogin where username='%s'" %e1.get())
        checkuser=cur.fetchall()
        if len(checkuser):
            flagu=1

        if len(e1.get()) == 0 or len(e2.get()) == 0:
            showwarning("Warning", "Fields cannot be left empty!!!")
        else:
            if flagu == 1 and flagp == 1:
                cur.execute("select username from datalogin where password='%s'" %e2.get())
                usecondcheck=cur.fetchone()
                cur.execute("select password from datalogin where username='%s'" %e1.get())
                psecondcheck=cur.fetchone()
                if usecondcheck[0] == e1.get() and psecondcheck[0] == e2.get():
                    logingui.destroy()
                    
                    home(usecondcheck)
                else:
                    showerror("Error", "Check Username or Password")
            else:
                showerror("Error", "Check Username or Password")
    def switchsignup():
        logingui.destroy()
        signupwindow()
    def switchforgot():
        logingui.destroy()
        forgotwindow()
    Checkbutton(fm3, text="Keep me logged in").grid(row=4,columnspan=2,padx=5,pady=15, sticky=W)
    Button(fm3,text="Login",command=signin).grid(row=5,column=0,sticky=W)
    Button(fm3,text="Sign Up",command=switchsignup).grid(row=5,column=1, sticky=E)
    Button(fm3,text="Forgot Password?",command=switchforgot).grid(row=6,column=1,sticky=E)
    Button(fm3,text="Reset",command=clear).grid(row=6,column=0,sticky=W)
    fm3.grid(column=1,sticky=S,pady=60)
    fm2.grid(row=0,column=3,sticky=N+S+E,rowspan=2)
    logingui.mainloop()

def signupwindow():
    signup=Tk()
    signup.title("Sign Up")
    bg_image1=PhotoImage(file="back.gif")
    bg_label1=Label(signup,image=bg_image1)
    bg_label1.image = bg_image1
    bg_label1.place(x=0, y=0, relwidth=1, relheight=1) 
    Label(signup, text="Sign Up",fg="blue",font=('bold',16)).grid(row=0,column=0,columnspan=2)
    Label(signup,text="Username:").grid(row=1,sticky=E)
    e1=Entry(signup)
    e1.grid(row=1,column=1)
    Label(signup,text="Password:").grid(row=2,sticky=E)
    e2=Entry(signup,show='*')
    e2.grid(row=2,column=1)
    Label(signup,text="Confirm Password:").grid(row=3,sticky=E)
    e3=Entry(signup,show='*')
    e3.grid(row=3,column=1)
    Label(signup,text="Email-Id:").grid(row=4,sticky=E)
    e4=Entry(signup)
    e4.grid(row=4,column=1)
    def createid():
        userexist=emailexist=0
        valide=1
        cur.execute("select username from datalogin where username='%s'" %(e1.get()))
        user=cur.fetchall()
        if len(user):
            userexist=1
        cur.execute("select emailid from datalogin where emailid='%s'" %(e4.get()))
        email=cur.fetchall()
        if len(email):
            emailexist=1
        allowed=['yahoo.com', 'gmail.com', 'hotmail.com', 'rediffmail.com']
        emailid=e4.get()
        loc=emailid.find('@')
        emailid=emailid[loc+1:]
        if emailid not in allowed:
            showerror("Invalid","Enter a valid email id")
            valide=0
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0:
            showwarning("Warning","Fields cannot be left empty!!!")
        else:
            if userexist or emailexist:
                showwarning("Warning", "Email or Username exists")
            elif valide==1 and e2.get()==e3.get():
                showinfo("Success", "Id Created Successfully!!!")
                cur.execute("insert into datalogin values('%s','%s','%s')" %(e1.get(),e2.get(),e4.get()))
                con.commit()
    def switchlogin():
        signup.destroy()
        loginwindow()
    Button(signup,text="Sign Up",command=createid).grid(row=5)
    Button(signup, text="Click Here to login again",command=switchlogin).grid(row=5,column=1)
    signup.mainloop()

def forgotwindow():
    forgot=Tk()
    forgot.title("Change Password")
    Label(forgot,text="Enter your username: ").grid(row=0,column=0)
    e1=Entry(forgot)
    e1.grid(row=0,column=1)
    Label(forgot,text="Enter new password: ").grid(row=1,column=0)
    e2=Entry(forgot,show='*')
    e2.grid(row=1,column=1)
    Label(forgot,text="Confirm new password: ").grid(row=2,column=0)
    e3=Entry(forgot,show='*')
    e3.grid(row=2,column=1)
    def forgotpass():
        cur.execute("select username from datalogin where username='%s'" %e1.get())
        user=cur.fetchall()
        if len(user)==0:
            showerror("Error","Username not found")
        else:
            cur.execute("select password from datalogin where username='%s'" %user[0])
            password=cur.fetchall()
            if len(e1.get()) == 0 or len(e2.get()) == 0 or len(e3.get())==0:
                showwarning("Warning", "Fields cannot be left blank")
            elif password[0]!=e2.get():
                if e2.get()==e3.get() and len(e2.get())!=0:
                    cur.execute("update datalogin set password='%s' where username='%s'" %(e2.get(),e1.get()))
                    con.commit()
                    showinfo("Success","Password Changed Successfully")
                else:
                    showerror("Error", "Password doesn't match")
    def switchlogin2():
        forgot.destroy()
        loginwindow()
    Button(forgot,text="Change Password",command=forgotpass).grid(row=3,column=0)
    Button(forgot,text="Click Here to login again",command=switchlogin2).grid(row=3,column=1)
    forgot.mainloop()
loginwindow()
