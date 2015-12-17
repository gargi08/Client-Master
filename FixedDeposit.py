import sqlite3
from Tkinter import *
from tkMessageBox import *
con1=sqlite3.Connection('ClientMaster.db')
cur1=con1.cursor()
con2=sqlite3.Connection('Issuer.db')
cur2=con2.cursor()
try:
    cur2.execute('create table fdIssuer(companyname varchar2(25))')
except:
    pass

try:
    cur2.execute("create table FDetails(clientname varchar2(20),company varchar2(25),tenure number(10),compounded varchar2(10),rate number(10),investamt number(15),matureamt number(15))")
except:
    pass

'''cur2.execute('select * from fdIssuer')
li=cur2.fetchall()
print li
cur2.execute('select * from FDetails')
li=cur2.fetchall()
print li'''

def addissuer():
##    addis=Tk()
    addis=Toplevel()
    addis.title('Fixed Deposits')
    Label(addis, text="Add FD Issuer",fg="red",font=('bold',16)).grid(columnspan=2)
    Label(addis,text="Issuer Name ").grid(row=1,sticky=W)
    e1=Entry(addis)
    e1.grid(row=1,column=1)
    def callissuer():
        if len(e1.get())==0:
            showwarning("Warning","Fields cannot be left empty!!")
        else:
            cur2.execute("insert into fdIssuer values('%s')" %(e1.get()))
            con2.commit()
            showinfo("Successful","Issuer Name Added Successfully!!!")
    Button(addis,text="Add Issuer!",command=callissuer).grid(row=2,column=1,sticky=W)
##    addis.mainloop()

    
def fixed():
##    fd=Tk()
    fd=Toplevel()
    fd.title("Fixed Deposits")
    Label(fd, text="Fixed Income:Corporate FD",fg="red",font=('bold',16)).grid(columnspan=2)

    Label(fd,text="Name Of Investor ").grid(row=1,sticky=W)
    var1=StringVar()
    var1.set('-----Select-----')
    cur1.execute("select clientname from client")
    li1=cur1.fetchall()
    listli1=[]
    for x1 in li1:
        listli1.append(x1[0])
    if listli1==[]:
        listli1=['-----Select-----']
    option1=OptionMenu(fd,var1,*listli1)
    option1.grid(row=1,column=1)

    Label(fd,text="Issuer Name ").grid(row=2,sticky=W)
    var2=StringVar()
    var2.set('-----Select-----')
    cur2.execute("select companyname from fdIssuer")
    li2=cur2.fetchall()
    listli2=[]
    for x2 in li2:
        listli2.append(x2[0])
    if listli2==[]:
        listli1=['-----Select-----']
    option2=OptionMenu(fd,var2,*listli2)
    option2.grid(row=2,column=1)

    Label(fd,text="Tenure in years ").grid(row=3,sticky=W)
    time=DoubleVar()
    e1=Entry(fd)
    e1.grid(row=3,column=1)
    
    Label(fd,text="Amount ").grid(row=4,sticky=W)
    e2=Entry(fd)
    e2.grid(row=4,column=1)
    
    def clear(x=0):
        e1.configure(state='normal')
        e2.configure(state='normal')
        e3.configure(state='normal')
        e4.configure(state='normal')
        e4.delete(0,END)
        e4.configure(state='readonly')
        
    Label(fd,text="Interest Compounding ").grid(row=5,sticky=W)
    var3=StringVar()
    var3.set("Yearly")
    option3=OptionMenu(fd,var3,"Yearly","Half-Yearly","Quaterly","Monthly",command=clear)
    option3.grid(row=5,column=1)
    
    Label(fd,text="Interest Rate ").grid(row=6,sticky=W)
    e3=Entry(fd)
    e3.grid(row=6,column=1)


    Label(fd,text="Maturity Value ").grid(row=7,sticky=W)
    e4=Entry(fd)
    e4.configure(state='readonly')
    e4.grid(row=7,column=1)
    
##    def clear():
##        e1.configure(state='normal')
##        e2.configure(state='normal')
##        e3.configure(state='normal')
##        e4.configure(state='normal')
##        e4.delete(0,END)
##        e4.configure(state='readonly')
    
    Label(fd,text="Nominee Name ").grid(row=8,sticky=W)
    e5=Entry(fd)
    e5.grid(row=8,column=1)

    def calculate():
        try:
            e4.configure(state='normal')
            if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 :
                showwarning("Warning","Fields cannot be left empty!!")
                return
            ci=var3.get()
            rate=(float)(e3.get())
            time=(float)(e1.get())
            p=(float)(e2.get())
        
        
            if ci=="Half-Yearly":
                rate=rate/6.0
                time=time*6
            elif ci=="Quaterly":
                rate=rate/4.0
                time=time*4
            elif ci=="Monthly":
                rate=rate/12.0
                time=time*12
            m=(p*((1+rate/100)**(time)))
            mature=round(m,2)
            e4.delete(0,END)
            e4.insert(0,mature)
            e1.configure(state='readonly')
            e2.configure(state='readonly')
            e3.configure(state='readonly')
            e4.configure(state='readonly')
            
        except:
            showwarning("Warning","Enter Correct Values")
            clear()
    def add():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or var1.get()=='-----Select-----' or var2.get()=='-----Select-----':
            showwarning("Warning","Fields cannot be left empty!!")
            return
        else:
            cur2.execute("insert into FDetails values('%s','%s','%s','%s','%s','%s','%s')" %(var1.get(),var2.get(),e1.get(),var3.get(),e3.get(),e2.get(),e4.get()))
            showinfo("Success", "Data Stored Successfully!!!")
            con2.commit()
            clear()
            
    def display():
        fddisp=Toplevel()
        fddisp.title('Fixed Deposits')
        Label(fddisp, text="Fixed Deposits/Bonds",fg="red",font=('bold',16)).grid(columnspan=2)
        Label(fddisp,text="Name Of Investor ").grid(row=1,sticky=W)
        var4=StringVar()
        var4.set('-----Select-----')
        cur2.execute("select distinct clientname from FDetails")
        li2=cur2.fetchall()
        listli2=[]
        for x1 in li2:
            listli2.append(x1[0])
        if listli2==[]:
            listli2=['-----Select-----']
        option4=OptionMenu(fddisp,var4,*listli2)
        option4.grid(row=1,column=1)
        def result():
            res=Toplevel()
            li1=["FD/Bond Issuer","Int. Rate","Tenure","Compounded","Invest. Amt","Matu. Amt"]
            cur2.execute("select company from FDetails where clientname='%s'"%(var4.get()))
            li2=cur2.fetchall()
            cur2.execute("select rate from FDetails where clientname='%s'"%(var4.get()))
            li3=cur2.fetchall()
            cur2.execute("select tenure from FDetails where clientname='%s'"%(var4.get()))
            li4=cur2.fetchall()
            cur2.execute("select compounded from FDetails where clientname='%s'"%(var4.get()))
            li5=cur2.fetchall()
            cur2.execute("select investamt from FDetails where clientname='%s'"%(var4.get()))
            li6=cur2.fetchall()
            cur2.execute("select matureamt from FDetails where clientname='%s'"%(var4.get()))
            li7=cur2.fetchall()
            Label(res, text="Fixed Deposits/Bonds",fg="red",font=('times',24,'bold')).grid(columnspan=2,sticky=E)
            Label(res,text=str(var4.get()),font=('times',16)).grid(column=3,row=0)
            y=0
            for x in li1:
                if x=="FD/Bond Issuer":
                    w=30
                else:
                    w=20
                Label(res,text=x,bd=1,relief='solid',font='times 9 bold',bg='cyan',width=w).grid(row=1,column=y)
                y+=1
            r=0
            ro=2
            for x in li2:
                Label(res,text=x[0],bd=1,relief='solid',width=30).grid(row=ro,column=0)
                Label(res,text=li3[r],bd=1,relief='solid',width=20).grid(row=ro,column=1)
                Label(res,text=li4[r],bd=1,relief='solid',width=20).grid(row=ro,column=2)
                Label(res,text=li5[r],bd=1,relief='solid',width=20).grid(row=ro,column=3)
                Label(res,text=li6[r],bd=1,relief='solid',width=20).grid(row=ro,column=4)
                Label(res,text=li7[r],bd=1,relief='solid',width=20).grid(row=ro,column=5)
                ro+=1
                r+=1
            #res.mainloop()
        Button(fddisp,text="Display Details",command=result).grid(row=2,column=1)
        #fddisp.mainloop()
        
    Button(fd,text="Add FD/Bond",command=add).grid(row=9,column=0)
    Button(fd,text="Calculate Maturity Value",command=calculate).grid(row=9,column=1)
    Button(fd,text="Display FD",command=display).grid(row=9,column=2)
##    fd.mainloop()
