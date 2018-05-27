###################documetation#####################
###############prerequisites#####################
'''1)create a mysql database named main
 2)a table named record i.e >>create table record(ano int,password varchar(20),email varchar(60),balance numeric(50,10))'''

from tkinter import *
from tkinter import messagebox
from mysql.connector import *
import smtplib
################################SMTP#################################
server=smtplib.SMTP('smtp.gmail.com', 587) #smtp server you are using
server.starttls()
server.login('bankeyindiana@gmail.com', '#############') #email through which you want to send the mail regarding withdrawl or depositions
sender='bankeyindiana@gmail.com'
####################################################################################
con=connect(user="root",password="root",database="main")
cur=con.cursor()
############## GUI #########################
root=Tk()
root.title="the banking application"
root.configure(bg = "white")
################variables###########################
anum=IntVar()
bal=IntVar()
email=StringVar()



####################################functions###################################
def login():
    f3=Frame(root,height=100,width=2000000,bg="white")
    f3.place(x=0,y=199)
   
#################################################function layer2################################
    def login2():
        f4=Frame(root,height=400,width=1900,bg="snow")
        f4.place(x=0,y=199)
##################################function layer3################################################
        def bcheck():
            query="select * from record where ano=%d"%(anum.get())
            cur.execute(query)
            record=cur.fetchone()
            messagebox.showinfo("balance","you have %d balance"%(bal.get()))
        def transact():
            f5=Frame(root,height=400,width=1900,bg="snow")
            f5.place(x=0,y=199)
##################################function layer 4#############################################
            def withdraw():
                f7=Frame(root,height=100,width=2000000,bg="white")
                f7.place(x=0,y=199)
##################################fuction layer 5 ###############################################################
                def withdraw2():
                    
                    if int(e17.get())>=0:
                        money=bal.get()-int(e17.get())
                        if money<0:
                            messagebox.showinfo("transaction unsuccessfull ","insufficient balance")
                            f2call()
                            return
                        query=" update record set balance= %d where ano=%d "%(money,anum.get())
                        cur.execute(query)
                        con.commit()
                        messagebox.showinfo("money withdrawn","collect your cash")
                        msg = "Hello, %d amount has been withdrawn from your account, your remaining balance is %f"%(int(e17.get()),money)
                        receiver=email.get()
                        server.sendmail(sender, receiver, msg)
                        server.close()
                        print("sent...")
                        f2call()
                    else:
                        messagebox.showinfo("invalid ","invalid amount")
                l17=Label(f7,text="ENTER AMOUNT TO BE WITHDRAWN",bg="dark blue",fg="snow",font=("calibre",50))
                l17.grid(row=0,column=0,padx=100,pady=30,rowspan=6,columnspan=10)
                e17=Entry(f7,font=("calibre",50),bg="grey",justify="right")
                e17.grid(row=7,column=1,padx=100,pady=30,rowspan=3,columnspan=10)
                b17=Button(f7,text="WITHDRAW",bg="dark blue",fg="snow",font=("calibre",30),command=withdraw2)
                b17.grid(row=11,column=1,padx=30,pady=30,columnspan=10)
            def deposit():
                f7=Frame(root,height=100,width=2000000,bg="white")
                f7.place(x=0,y=199)
                def deposit2():
                    if int(e17.get())>=0:
                        money=bal.get()+int(e17.get())
                        query=" update record set balance= %d where ano=%d "%(money,anum.get())
                        cur.execute(query)
                        con.commit()
                        messagebox.showinfo("money deposited","your money has been successfully deposited")
                        msg = "Hello, %d amount has been deposited from your account, now your balance is %f"%(int(e17.get()),money)
                        receiver=email.get()
                        server.sendmail(sender, receiver, msg)
                        server.close()
                        print("sent...")
                        f2call()
                    else:
                        messagebox.showinfo("invalid ","invalid amount")
                    
                l17=Label(f7,text="            ENTER AMOUNT DEPOSITED         ",bg="dark blue",fg="snow",font=("calibre",50))
                l17.grid(row=0,column=0,padx=100,pady=30,rowspan=6,columnspan=10)
                e17=Entry(f7,font=("calibre",50),bg="grey",justify="right")
                e17.grid(row=7,column=1,padx=100,pady=30,rowspan=3,columnspan=10)
                b17=Button(f7,text="DEPOSIT",bg="dark blue",fg="snow",font=("calibre",30),command=deposit2)
                b17.grid(row=11,column=1,padx=30,pady=30,columnspan=10)
                            
            b11=Button(f5,text="withdraw",font=("calibre",50),bg="dark blue",fg="snow",activebackground="blue",command=withdraw)
            b11.place(x=350,y=150)
            b21=Button(f5,text="deposit",font=("calibre",50),bg="dark blue",fg="snow",activebackground="blue",command=deposit)
            b21.place(x=800,y=150)
                    
                
        b1=Button(f4,text="transaction",font=("calibre",50),bg="dark blue",fg="snow",activebackground="blue",command=transact)
        b1.place(x=350,y=150)
        b2=Button(f4,text="balance check",font=("calibre",50),bg="dark blue",fg="snow",activebackground="blue",command=bcheck)
        b2.place(x=800,y=150)

    def checker():
        query="select * from record where ano=%d"%(int(e1.get()))
        cur.execute(query)
        record=cur.fetchone()
        if record!=None and int(e1.get())==record[0] and e2.get()==record[1] :
            anum.set(int(e1.get()))
            bal.set(int(record[3]))
            email.set(record[2])
            login2()
            messagebox.showinfo("congrats","you are logged in")
            
        else:
            messagebox.showinfo("wrong","invalid details")
    ####################################### l2 ##########################################################
    l1=Label(f3,text="account number",bg="dark blue",fg="snow",font=("calibre",50))
    l1.grid(row=0,column=0,padx=100,pady=30,rowspan=3)
    l2=Label(f3,text="password",bg="dark blue",fg="snow",font=("calibre",50))
    l2.grid(row=4,column=0,padx=100,pady=30,rowspan=3)
    e1=Entry(f3,font=("calibre",50))
    e1.grid(row=0,column=1,padx=100,pady=30,rowspan=3,columnspan=6)
    e2=Entry(f3,font=("calibre",50))
    e2.grid(row=4,column=1,padx=100,pady=30)
    b1=Button(f3,text="login",bg="dark blue",fg="snow",font=("calibre",30),command=checker)
    b1.grid(row=7,column=1,padx=30,pady=30)
def sup():
    ########################databse code#########################
    query="select count(*) from record"
    cur.execute(query)
    count=cur.fetchone()
    #####################python code#####################################


    ##############################sup layer 2 ################################
    def store():
        query="insert into record values (%d,%s,'%s',%d)"%(count[0]+1,e2.get(),e3.get(),int(e4.get()))
        cur.execute(query)
        con.commit()
        messagebox.showinfo("succesful","your account has been succesfully created")
        f2call()
        
    f3=Frame(root,height=90,width=2000000,bg="white")
    f3.place(x=0,y=199)
    l1=Label(f3,text="alloted account number is %d"%(int(count[0])+1),bg="dark blue",fg="snow",font=("calibre",20))
    l1.grid(row=0,column=0,padx=100,pady=30,rowspan=1,columnspan=20)
    l2=Label(f3,text="set password",bg="dark blue",fg="snow",font=("calibre",20))
    l2.grid(row=2,column=0,padx=100,pady=30,rowspan=1)
    e2=Entry(f3,font=("calibre",20))
    e2.grid(row=2,column=1,padx=100,pady=30)
    l3=Label(f3,text="email address",bg="dark blue",fg="snow",font=("calibre",20))
    l3.grid(row=3,column=0,padx=100,pady=30,rowspan=1)
    e3=Entry(f3,font=("calibre",20))
    e3.grid(row=3,column=1,padx=100,pady=30)
    l4=Label(f3,text="initial balance",bg="dark blue",fg="snow",font=("calibre",20))
    l4.grid(row=4,column=0,padx=100,pady=30,rowspan=1)
    e4=Entry(f3,font=("calibre",20))
    e4.grid(row=4,column=1,padx=100,pady=30)
    b1=Button(f3,text="sign up",bg="dark blue",fg="snow",font=("calibre",30),command=store)
    b1.grid(row=0,column=8,padx=70,pady=30,rowspan=5)
    

############################mid frame########################################################################
def f2call():
    f2=Frame(root,height=400,width=1900,bg="snow")
    f2.place(x=0,y=199)
    b1=Button(f2,text="Log in",font=("calibre",50),bg="dark blue",fg="snow",activebackground="blue",command=login)
    b1.place(x=350,y=150)
    b2=Button(f2,text="Sign up!",font=("calibre",50),bg="dark blue",fg="snow",activebackground="blue",command=sup)
    b2.place(x=800,y=150)
f2call()


##########___heading_____#####################################################################################
class element:
    def __init__(self,text,xp,yp):
        f_top=Canvas(root,height=200,width=1900,bg="dark blue")
        f_top.place(x=xp,y=yp)
        f_top.create_text(775,105,text=text,font=('Helvetica',80),fill="white")
top=element("Bank ",0,0)
#####################__bottom ad ____#########################################################################
bottom=element("desh ka apna bank !   ",0,620)
root.mainloop() 
