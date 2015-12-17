import sqlite3
from Tkinter import *
from tkMessageBox import *
con1=sqlite3.Connection('ClientMaster.db')
cur1=con1.cursor()
try:
    cur1.execute('create table client(clientname varchar2(25),address1 varchar2(20),address2 varchar2(15),address3 varchar2(15),city varchar2(15),state varchar2(15),pincode number(7),mobile number(10),pan varchar2(10),email varchar2(20),dob date)')
except:
    pass

def updateclient():
    upcl=Toplevel()
    upcl.title('Update Client Details')
    Label(upcl,text="Update Client",fg="red",font=('bold',16)).grid(columnspan=2)
    Label(upcl,text="Client Name ").grid(row=1,sticky=W)
    var=StringVar()
    var.set('--Select--')
    cur1.execute("select clientname from client")
    li=cur1.fetchall()
    listli=[]
    ##print li
    for x in li:
        listli.append(x[0])
    if listli==[]:
##      listli=['No client']
        listli=['--Select--']
    option=OptionMenu(upcl,var,*listli)
    option.grid(row=1,column=1)
    
    
    Label(upcl,text="Home Address:").grid(row=3,sticky=W)
    e2=Entry(upcl)
    e2.grid(row=2,column=1)
    
    e3=Entry(upcl)
    e3.grid(row=3,column=1)
    
    e4=Entry(upcl)
    e4.grid(row=4,column=1)
    
    Label(upcl,text="City ").grid(row=5,sticky=W)
    e5=Entry(upcl)
    e5.grid(row=5,column=1)
    
    Label(upcl,text="State ").grid(row=6,sticky=W)
    e6=Entry(upcl)
    e6.grid(row=6,column=1)
    
    Label(upcl,text="Pincode ").grid(row=7,sticky=W)
    e7=Entry(upcl)
    e7.grid(row=7,column=1)
    
    Label(upcl,text="Mobile ").grid(row=8,sticky=W)
    e8=Entry(upcl)
    e8.grid(row=8,column=1)
    
    Label(upcl,text="PAN ").grid(row=9,sticky=W)
    e9=Entry(upcl)
    e9.grid(row=9,column=1)
    
    Label(upcl,text="Email ").grid(row=10,sticky=W)
    e10=Entry(upcl)
    e10.grid(row=10,column=1)
    
    Label(upcl,text="Date of Birth ").grid(row=11,sticky=W)
    e11=Entry(upcl)
    e11.grid(row=11,column=1)
    global valid
    valid=0
    def change(*args):
        global valid
        valid=1
##        name=upcl.getvar(args[0])
        name=var.get()
        cur1.execute("select address1 from client where clientname='%s'"%(name))
        result=cur1.fetchone()
        e2.delete(0,END)
        e2.insert(0,result[0])

        cur1.execute("select address2 from client where clientname='%s'"%(name))
        result=cur1.fetchone()
        e3.delete(0,END)
        e3.insert(0,result[0])

        cur1.execute("select address3 from client where clientname='%s'"%(name))
        result=cur1.fetchone()
        e4.delete(0,END)
        e4.insert(0,result[0])

        cur1.execute("select city from client where clientname='%s'"%(name))
        result=cur1.fetchone()
        e5.delete(0,END)
        e5.insert(0,result[0])

        cur1.execute("select state from client where clientname='%s'"%(name))
        result=cur1.fetchone()
        e6.delete(0,END)
        e6.insert(0,result[0])

        cur1.execute("select pincode from client where clientname='%s'"%(name))
        result=cur1.fetchone()
        e7.delete(0,END)
        e7.insert(0,result[0])

        cur1.execute("select mobile from client where clientname='%s'"%(name))
        result=cur1.fetchone()
        e8.delete(0,END)
        e8.insert(0,result[0])

        cur1.execute("select pan from client where clientname='%s'"%(name))
        result=cur1.fetchone()
        e9.delete(0,END)
        e9.insert(0,result[0])

        cur1.execute("select email from client where clientname='%s'"%(name))
        result=cur1.fetchone()
        e10.delete(0,END)
        e10.insert(0,result[0])

        cur1.execute("select dob from client where clientname='%s'"%(name))
        result=cur1.fetchone()
        e11.delete(0,END)
        e11.insert(0,result[0])
        
    if listli[0]!='--Select--':
        var.trace('w',change)
    
    def callupdate():
        global valid
        if valid==0:
            showwarning('Warning','You must select a client to update!!')
            return
        name=var.get()
        panexist=emailexist=0
        validemail=validstate=1
        cur1.execute("select clientname from client where pan='%s'"%(e9.get()))
        pan=cur1.fetchall()
        try:
            if pan[0][0]!=name:
                panexist=1
        except:
            panexist=0
        cur1.execute("select clientname from client where email='%s'"%(e10.get()))
        eid=cur1.fetchall()
        try:
            if eid[0][0]!=name:
                emailexist=1
        except:
            emailexist=0
        allowede=['yahoo.com', 'gmail.com', 'hotmail.com', 'rediffmail.com','juet.ac.in']
        alloweds=['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand',
                  'Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Orissa','Punjab','Rajasthan','Sikkim','Tamil Nadu',
                  'Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
        state=e6.get()
        state=state.title()
        emailid=e10.get()
        emailid=emailid.lower()
        loc=emailid.find('@')
        emailid=emailid[loc+1:]
        if emailid not in allowede:
            showerror("Invalid","Enter a valid email id")
            validemail=0
        if  state not in alloweds:
            showerror("Invalid","Enter a valid state")
            validstate=0
        if (len(e2.get())==0 or len(e5.get())==0 or len(e6.get())==0 or len(e7.get())==0 or len(e8.get())==0 or len(e9.get())==0 or len(e10.get())==0 or len(e11.get())==0):
               showwarning("Warning","Fields cannot be left empty!!!")
        else:
            if panexist or emailexist:
                showwarning("Warning", "Email or Pan Name exists")
            elif validemail==1 and validstate==1:
                cur1.execute("delete from client where clientname='%s'"%(name))
                cur1.execute("insert into client values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(name,e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get()))
                con1.commit()
                s=showinfo(title="Succesful",message='Client Updated Successfully')
                upcl.destroy()
    Button(upcl,text="Update Info!",command=callupdate).grid(row=12,column=1,sticky=W)
    
def addclient():
    addcl=Toplevel()
    addcl.title('New Client')
    Label(addcl, text="Add New Client",fg="red",font=('bold',16)).grid(columnspan=2)

    Label(addcl,text="Client Name ").grid(row=1,sticky=W)
    e1=Entry(addcl)
    e1.grid(row=1,column=1)
    
    Label(addcl,text="Home Address:").grid(row=3,sticky=W)
    e2=Entry(addcl)
    e2.grid(row=2,column=1)
    e3=Entry(addcl)
    e3.grid(row=3,column=1)
    e4=Entry(addcl)
    e4.grid(row=4,column=1)

    Label(addcl,text="City ").grid(row=5,sticky=W)
    e5=Entry(addcl)
    e5.grid(row=5,column=1)
    
    Label(addcl,text="State ").grid(row=6,sticky=W)
    e6=Entry(addcl)
    e6.grid(row=6,column=1)
    
    Label(addcl,text="Pincode ").grid(row=7,sticky=W)
    e7=Entry(addcl)
    e7.grid(row=7,column=1)
    
    Label(addcl,text="Mobile ").grid(row=8,sticky=W)
    e8=Entry(addcl)
    e8.grid(row=8,column=1)
    
    Label(addcl,text="PAN ").grid(row=9,sticky=W)
    e9=Entry(addcl)
    e9.grid(row=9,column=1)
    
    Label(addcl,text="Email ").grid(row=10,sticky=W)
    e10=Entry(addcl)
    e10.grid(row=10,column=1)

    Label(addcl,text="Date of Birth ").grid(row=11,sticky=W)
    e11=Entry(addcl)
    e11.grid(row=11,column=1)

    def calladd():
        panexist=emailexist=0
        validemail=validstate=1
        cur1.execute("select pan from client where pan='%s'"%(e9.get()))
        pan=cur1.fetchall()
        if len(pan):
            panexist=1
        cur1.execute("select email from client where email='%s'"%(e10.get()))
        eid=cur1.fetchall()
        if len(eid):
            emailexist=1
        allowede=['yahoo.com', 'gmail.com', 'hotmail.com', 'rediffmail.com','juet.ac.in']
        alloweds=['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand',
                  'Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Orissa','Punjab','Rajasthan','Sikkim','Tamil Nadu',
                  'Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
        state=e6.get()
        state=state.title()
        emailid=e10.get()
        emailid=emailid.lower()
        loc=emailid.find('@')
        emailid=emailid[loc+1:]
        if len(e1.get())==0 or len(e2.get())==0 or len(e5.get())==0 or len(e6.get())==0 or len(e7.get())==0 or len(e8.get())==0 or len(e9.get())==0 or len(e10.get())==0 or len(e11.get())==0:
            showwarning("Warning","Fields cannot be left empty!!!")
            return
        if emailid not in allowede:
            showerror("Invalid","Enter a valid email id")
            validemail=0
        if  state not in alloweds:
            showerror("Invalid","Enter a valid state")
            validstate=0
        
        else:
            if panexist or emailexist:
                showwarning("Warning", "Email or Username exists")
            elif validemail==1 and validstate==1:
                cur1.execute("insert into client values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get()))
                con1.commit()
                s=showinfo(title="Succesful",message='Client Added Successfully')
                addcl.destroy()

    Button(addcl,text="Add Client!",command=calladd).grid(row=12,column=1,sticky=W)
    
def removeclient():
    remcl=Toplevel()
    remcl.title('Remove Client')
    Label(remcl,text="Remove Client",fg="red",font=('bold',16)).grid(columnspan=2)
    var=StringVar()

    def func(*args):
        global selected
        selected=1

    tr=var.trace_variable('w',func)
    
    global warn
    warn='You must select a client to remove!!'
    
    def optionlist():
        var.set('--Select--')
        cur1.execute("select clientname from client")
        li=cur1.fetchall()
        listli=[]
        for x in li:
            listli.append(x[0])
        if listli==[]:
##            listli=['No client']
            listli=['--Select--']
            var.trace_vdelete('w',tr)
            global warn
            warn='No client is registered'
        option=OptionMenu(remcl,var,*listli)
        option.grid(row=1,column=1)
    optionlist()
    

    global selected
    selected=0
    
    def callremove():
        global selected
        if selected==0:
            showwarning('Warning',warn)
            return
        name=var.get()
        cur1.execute("delete from client where clientname='%s'"%(name))
        cur1.execute('select clientname from client')
        con1.commit()
        s=showinfo(title="Succesful",message='Client Removed Successfully')
        optionlist()
        selected=0
        remcl.destroy()
    Button(remcl,text="Remove Client!",command=callremove).grid(row=12,column=1,sticky=W)
    
def listclients():
    #licl=Tk()
    licl=Toplevel()
    cur1.execute("select * from client")
    detail=cur1.fetchall()
    Label(licl,text="Clients List",fg="red",font=('times',24,'bold')).grid(columnspan=2)
    head=["Client Name","Home Address","City","State","Pincode","Mobile","PAN","Email","Date of Birth"]

    t=Frame(licl)
    Label(t,text=head[0],bd=1,relief='solid',width=15,font='times 9 bold',bg='cyan').grid(row=0,column=0)
    Label(t,text=head[1],bd=1,relief='solid',width=25,font='times 9 bold',bg='cyan').grid(row=0,column=1)
    Label(t,text=head[2],bd=1,relief='solid',width=10,font='times 9 bold',bg='cyan').grid(row=0,column=2)
    Label(t,text=head[3],bd=1,relief='solid',width=10,font='times 9 bold',bg='cyan').grid(row=0,column=3)
    Label(t,text=head[4],bd=1,relief='solid',width=10,font='times 9 bold',bg='cyan').grid(row=0,column=4)
    Label(t,text=head[5],bd=1,relief='solid',width=10,font='times 9 bold',bg='cyan').grid(row=0,column=5)
    Label(t,text=head[6],bd=1,relief='solid',width=10,font='times 9 bold',bg='cyan').grid(row=0,column=6)
    Label(t,text=head[7],bd=1,relief='solid',width=20,font='times 9 bold',bg='cyan').grid(row=0,column=7)
    Label(t,text=head[8],bd=1,relief='solid',width=10,font='times 9 bold',bg='cyan').grid(row=0,column=8)
    t.grid()
    
    for row in detail:
        t=Frame(licl)
        Label(t,text=row[0],bd=1,relief='solid',width=15).grid(row=0,column=0)
        Label(t,text=str(",".join(row[1:4])),bd=1,relief='solid',width=25).grid(row=0,column=1)
        Label(t,text=row[4],bd=1,relief='solid',width=10).grid(row=0,column=2)
        Label(t,text=row[5],bd=1,relief='solid',width=10).grid(row=0,column=3)
        Label(t,text=row[6],bd=1,relief='solid',width=10).grid(row=0,column=4)
        Label(t,text=row[7],bd=1,relief='solid',width=10).grid(row=0,column=5)
        Label(t,text=row[8],bd=1,relief='solid',width=10).grid(row=0,column=6)
        Label(t,text=row[9],bd=1,relief='solid',width=20).grid(row=0,column=7)
        Label(t,text=row[10],bd=1,relief='solid',width=10).grid(row=0,column=8)


##        x=0
##        st=""
##        for cell in row:
##            
##            if x==1 or x==2 or x==3:
##                e=Entry(t)
##                e.grid(row=0,column=1)
##                st=st+row[x]+" "
##                if x==3:
##                    e.insert(0,st)
##                    e.configure(state='readonly')
##            else:
##                e=Entry(t)
##                e.grid(row=0,column=x)
##                e.insert(0,cell)
##                e.configure(state='readonly')
##            x+=1
        t.grid()
    #mainloop()
#listclients()
