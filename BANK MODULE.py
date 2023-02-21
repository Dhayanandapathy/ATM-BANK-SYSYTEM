
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from time import strftime
#from time import gmtime, strftime

e3=''
e2=''
e1=''
h2=''
h4=''
rootwn=''
ed=''
check=0
global acctype
acctype="savings"
def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

def check_acc_nmb(num):
        global e3
        try:
            fpin=open(num+".txt",'r')
            pin=fpin.readline()
            pin=pin.strip('\n')
            fpin.readline()
            fpin.readline()
            name=fpin.readline()
            name=name.strip('\n')
            fpin.readline()
            fpin.readline()
            fpin.readline()
            fpin.readline()
            a=fpin.readline()
            a=a.strip("\n")
        
            p=e3.get()
            n=e1.get()
            n=n.strip('\n')
            if(p!=pin or name!=n):
                messagebox.showinfo("Error","Invalid credentials Check Name/Pin/Accountnumber")
                #Main_Menu()
                return 0
            elif a=="blocked":
                messagebox.showinfo("ERROR","SORRY YOUR ACCOUNT IS BLOCKED FOR MORE DETAILS CONTACT BANK")
                return 0
            

            
        except FileNotFoundError:
               messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
               return 0
        fpin.close()
        return 

def home_return(master):
	master.destroy()
	Main_Menu()
	
def write(master,name,oc,pin,aadarno,phno,panno):
    if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0) or (is_number(phno)==0)  or name==""):
        messagebox.showinfo("ERROR","PLEASE FILL ALL THE DETAILS")
        return
    if len(pin)!=4:
        messagebox.showinfo("ERROR","YOUR PIN SHOULD BE 4 DIGITS")
        return
    if len(aadarno)!=14:
        messagebox.showinfo("Error,Invalid Aadhar Card Format")
    s1=aadarno[0:4]
    s2=aadarno[5:9]
    s3=aadarno[10:14]

    if len(aadarno)!=14 or not s1.isdigit() or not s2.isdigit() or not s3.isdigit() or aadarno[4]!=" " or aadarno[9]!=" ":
        messagebox.showinfo("ERROR","INVALID AADHAR NUMBER FORMAT")
        return

    if len(phno)!=10:
        messagebox.showinfo("ERROR","YOUR PHONE NUMBER SHOULD BE 10 DIGITS")
        return
    if len(panno)!=10:
        messagebox.showinfo("Error","Invalid Pan Number Format")
        return
    
    p1=panno[0:5]
    p2=panno[5:9]
    p3=panno[9]
    if len(panno)!=10 or not p1.isalpha() or not p2.isdigit() or not p3.isalpha():
        messagebox.showinfo("ERROR","YOUR PAN NUMBER FORMAT IS WRONG")

    global acctype
    global check
    if check==0:
        messagebox.showinfo("ERROR","Accept terms and conditions")
        return

    f1=open("Accnt_Record.txt",'r')
    accnt_no=int(f1.readline())
    accnt_no+=1
    f1.close()

    f1=open("Accnt_Record.txt",'w')
    f1.write(str(accnt_no))
    f1.close()

    fdet=open(str(accnt_no)+".txt","w")
    fdet.write(pin+"\n")
    fdet.write(oc+"\n")
    fdet.write(str(accnt_no)+"\n")
    fdet.write(name+"\n")
    fdet.write(aadarno+"\n")
    fdet.write(phno+"\n")
    fdet.write(panno+"\n")
    fdet.write(acctype+"\n")
    fdet.write("active"+"\n")
    fdet.close()

    frec=open(str(accnt_no)+"-rec.txt",'w')
    frec.write("Date                        Credit        Debit    Balance    TYPE OF TRANSACTION\n")
    frec.write(str(datetime.now())+"    "+oc+"                      "+oc+"             Account Opened\n")
    frec.close()

    messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
    check=0
    master.destroy()
    
    global rootwn
    rootwn.deiconify()
    return

    

    
    
def crdt_write(master,amt,accnt,name):
    if(is_number(amt)==0):
        messagebox.showinfo("Error","Invalid Amount\nPlease try again.")
        master.destroy()
        return
    amt=int(amt)
    if amt<100 or amt%100!=0 or amt>15000:
        messagebox.showinfo("Error","THE AMOUNT SHOULD BE MINIMUM 100 AND MAXIMUM 150000 AND IT SHOULD BE MULTIPLE OF 100")
        return
    fdet=open(accnt+".txt",'r')
    pin=fdet.readline()
    camt=int(fdet.readline())
    fdet.close()
    amti=int(amt)
    cb=amti+camt
    fdet=open(accnt+".txt",'w')
    fdet.write(pin)
    fdet.write(str(cb)+"\n")
    fdet.write(accnt+"\n")
    fdet.write(name+"\n")
    fdet.close()
    frec=open(str(accnt)+"-rec.txt",'a+')
    frec.write(str(datetime.now())+"    "+str(amti)+"                    "+str(cb)+"             "+"self deposit"+"\n")
    frec.close()
    messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
    master.destroy()
    rootwn.deiconify()
    return
def debit_write(master,amt,accnt,name):
	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return

	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	if int(amt)<100 or int(amt)%100!=0 or int(amt)>15000:
		messagebox.showinfo("Error","THE AMOUNT SHOULD BE GREATER THAN 100 AND LESS THAN 15000 AND IT SHOULD BE MULTIPLE OF 100")
		return
	if(int(amt)>camt):
		messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
	else:
		amti=int(amt)
		cb=camt-amti
		fdet=open(accnt+".txt",'w')
		fdet.write(pin)
		fdet.write(str(cb)+"\n")
		fdet.close()
		frec=open(str(accnt)+"-rec.txt",'a+')
		frec.write(str(datetime.now())+"                      "+str(amti)+"    "+str(cb)+"             "+"self withdraw"+"\n")
		messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
		master.destroy()
		return
        
def Cr_Amt(accnt,name):
        global rootwn
        rootwn.iconify()
        creditwn=tk.Tk()
        creditwn.geometry("800x400")
        creditwn.title("Credit Amount")
        creditwn.configure(bg="pink")
        fr1=tk.Frame(creditwn,bg="blue")
        l_title=tk.Message(creditwn,text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        l_title.config(font=("Courier","50","bold"))
        l_title.pack(side="top")
        l1=tk.Label(creditwn,relief="raised",text="ENTER AMOUNT TO BE CREDITED:",font="Castellar 20 bold",bg="yellow")
        e1=tk.Entry(creditwn,relief="raised",font="comicsansms 15 bold")
        l1.pack(side="top")
        e1.pack(side="top")
        b=tk.Button(creditwn,text="CREDIT",relief="raised",font="comicsansms 15 bold",fg="red",bg="black",command=lambda:crdt_write(creditwn,e1.get(),accnt,name))
        b.pack(side="top")
        creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),accnt,name))


def De_Amt(accnt,name):
        
	debitwn=tk.Tk()
	debitwn.geometry("800x400")
	debitwn.title("Debit Amount")	
	debitwn.configure(bg="lightblue")
	fr1=tk.Frame(debitwn,bg="orange")
	l_title=tk.Message(debitwn,text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(debitwn,relief="raised",text="ENTER AMOUNT TO BE DEBITED: ",font="comicsansms 19 bold",bg="green")
	e1=tk.Entry(debitwn,relief="raised",font="comicsansms 19 bold")
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(debitwn,text="DEBIT",relief="raised",font="comicsansms 19 bold",fg="red",bg="black",command=lambda:debit_write(debitwn,e1.get(),accnt,name))
	b.pack(side="top")
	debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),accnt,name))




def disp_bal(accnt):
	fdet=open(accnt+".txt",'r')
	fdet.readline()
	bal=fdet.readline()
	fdet.close()
	messagebox.showinfo("YOUR ACCOUNT BALANCE IS",bal)




def disp_tr_hist(accnt):
	disp_wn=tk.Tk()
	disp_wn.geometry("900x600")
	disp_wn.title("Transaction History")
	disp_wn.configure(bg="light blue")
	fr1=tk.Frame(disp_wn,bg="blue")
	l_title=tk.Message(disp_wn,text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	fr1=tk.Frame(disp_wn)
	fr1.pack(side="top")
	l1=tk.Message(disp_wn,text="Your Transaction History:",padx=100,pady=20,width=1000,bg="blue",fg="orange",relief="raised")
	l1.pack(side="top")
	fr2=tk.Frame(disp_wn)
	fr2.pack(side="top")
	frec=open(accnt+"-rec.txt",'r')
	S = tk.Scrollbar(disp_wn)
	t=tk.Text(disp_wn,width=200, height=50)
	S.pack(side=tk.RIGHT, fill=tk.Y)
	t.pack(side=tk.LEFT, fill=tk.Y)
	S.config(command=t.yview)
	t.config(yscrollcommand=S.set)
	

	for line in frec:
            
		#l=tk.Message(disp_wn,anchor="w",text=line,relief="raised",width=2000)
		#l.pack(side="top")
		t.insert(tk.END,line+"\n")
	t.configure(state="disabled")
	b=tk.Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy)
	b.pack(side="top")
	frec.close()
def changepass(accnt,pas):
    global h2
    global h4
    pas1=h2.get()
    pas2=h4.get()
    if pas1==pas2:
        fpin=open(accnt+".txt",'r')
        fpin.readline()
        amb=fpin.readline()
        accno=fpin.readline()
        name=fpin.readline()
        aad=fpin.readline()
        pho=fpin.readline()
        panno=fpin.readline()
        acctype=fpin.readline()
        stas=fpin.readline()
        fpin.close()
        fpin=open(accnt+".txt","w")
        fpin.write(pas1+"\n")
        fpin.write(amb)
        fpin.write(accno)
        fpin.write(name)
        fpin.write(aad)
        fpin.write(pho)
        fpin.write(panno)
        fpin.write(acctype)
        fpin.write(stas)
        fpin.close()
        messagebox.showinfo("Operation Successfull!!","PIN CHANGED SUCESSFULLY")
        pas.destroy()
    
    else:
        messagebox.showinfo("OPERATION FALIED","PIN DOES NOT MATCH")
        return 
        #passwords do not match
def change_password(accnt):
        global h2
        global h4
        pas=tk.Tk()
        pas.geometry("800x400")
        pas.title("CHANGE PIN")
        pas.configure(bg="lightgreen")
        fra1=tk.Frame(pas,bg="light blue")
        l_title=tk.Message(pas,text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        l_title.config(font=("Courier","50","bold"))
        l_title.pack(side="top")
        h1=tk.Label(pas,relief="raised",text="NEW PIN: ",font="Cambria 20 bold",bg="pink")
        h2=tk.Entry(pas,show="*",relief="raised",font="Cambria 20 bold",bg="white")
        h1.pack(side="top")
        h2.pack(side="top")
        h3=tk.Label(pas,relief="raised",text="RE-TYPE PIN:",font="Cambria 20 bold",bg="pink")
        h4=tk.Entry(pas,show="*",relief="raised",font="Cambria 20 bold",bg="white")
        h3.pack(side="top")
        h4.pack(side="top")
        bt=tk.Button(pas,text="CHANGE",font="Cambria 20 bold",bg="pink",command=lambda:changepass(accnt,pas))
        bt.pack(side="top")
        
def changedetails(accnt,name,aadhar,phone,pan):
    global ed
    global rootwn
    global acctype
    if name=='':
        messagebox.showinfo("OPERATION FAILED","Enter name")
        return
    if aadhar=='':
        messagebox.showinfo("OPERATION FAILED","Enter aadhar number")
        return
    if phone=='':
        messagebox.showinfo("OPERATION FAILED","ENTER PHONE NUMBER")
        return
    if pan=='':
        messagebox.showinfo("OPERATION FAILED","ENTER PAN NUMBER")
        return
    fpin=open(accnt+".txt","r")
    pin=fpin.readline()
    oc=fpin.readline()
    fpin.close()
    fpout=open(accnt+".txt","w")
    fpout.write(pin)
    fpout.write(oc)
    fpout.write(accnt+"\n")
    fpout.write(name+"\n")
    fpout.write(aadhar+"\n")
    fpout.write(phone+"\n")
    fpout.write(pan+"\n")
    fpout.write(acctype+"\n")
    fpout.write("active"+"\n")
    fpout.close()
    messagebox.showinfo("CHANGE DETAILS","Details Updated Successfully")
    rootwn.deiconify()
    ed.withdraw()
def edit_accnt(accnt):
        rootwn.iconify()
        global ed
        global acctype
        ed=tk.Tk()
        fpin=open(accnt+".txt","r")
        fpin.readline()
        fpin.readline()
        fpin.readline()
        name=fpin.readline()
        aadhar=fpin.readline()
        phone=fpin.readline()
        pan=fpin.readline()
        accnttype=fpin.readline()
        name.strip("\n")
        aadhar.strip("\n")
        phone.strip("\n")
        pan.strip("\n")
        accnttype.strip("\n")
        ed.geometry("700x550")
        ed.title("CHANGE PIN")
        ed.configure(bg="light blue")
        l_title=tk.Message(ed,text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        l_title.config(font=("Courier","50","bold"))
        l_title.pack(side="top")
        g01=tk.Label(ed,relief="raised",text="NEW NAME: ",font="Cambria 20 bold",bg="pink")
        g01.pack(side="top")
        g02=tk.Entry(ed,relief="raised",font="Cambria 20 bold",bg="white")
        g02.insert(tk.END,name)
        g02.pack(side="top")
        g1=tk.Label(ed,relief="raised",text="NEW AADHAR NUMBER: ",font="Cambria 20 bold",bg="pink")
        g2=tk.Entry(ed,relief="raised",font="Cambria 20 bold",bg="white")
        g2.insert(tk.END,aadhar)
        g1.pack(side="top")
        g2.pack(side="top")
        g3=tk.Label(ed,relief="raised",text="NEW PHONE NUMBER",font="Cambria 20 bold",bg="pink")
        g4=tk.Entry(ed,relief="raised",font="Cambria 20 bold",bg="white")
        g4.insert(tk.END,phone)
        g3.pack(side="top")
        g4.pack(side="top")
        g5=tk.Label(ed,relief="raised",text="NEW PAN NUMBER",font="Cambria 20 bold",bg="pink")
        g5.pack(side="top")
        g6=tk.Entry(ed,relief="raised",font="Cambria 20 bold",bg="white")
        g6.insert(tk.END,pan)
        g6.pack(side="top")
        avar=tk.IntVar()
        bl=tk.IntVar()
        if accnttype=="savings":
            acctype="savings"
            tk.Radiobutton(ed,text="CURRENT ACCOUNT",font="comicsansms 10 bold",bd=3,relief="raised",bg="white",command=aaa, value=1, variable=avar).pack(side="top")
            r2=tk.Radiobutton(ed,text="SAVINGS",font="comicsansms 10 bold",bd=3,relief="raised",bg="white",command=bbb, varibale=avr, value=2).pack(side="top")
            
        else:
            acctype="current"
            tk.Radiobutton(ed,text="SAVINGS",font="comicsansms 10 bold",bd=3,relief="raised",bg="white",command=bbb, variable=avar, value=1).pack(side="top")
            r1=tk.Radiobutton(ed,text="CURRENT ACCOUNT",font="comicsansms 10 bold",bd=3,relief="raised",bg="white",command=aaa, variable=avar, value=2).pack(side="top")
        bt=tk.Button(ed,text="CHANGE",font="Cambria 20 bold",bg="pink",command=lambda: changedetails(accnt,g02.get().strip(),g2.get().strip(),g4.get().strip(),g6.get().strip()))
        bt.pack(side="top")

def aaa():
    global acctype
    acctype="current"
def bbb():
    global acctype
    acctype="savings"
def transfer(accnt,toacc,amt):
    global rootwn
    if toacc=="":
        messagebox.showinfo("Error","Fill Account Number")
        return
    if amt=="":
        messagebox.showinfo("Error","Fill Amount")
        return
    fpin=open(accnt+".txt","r")
    pin1=fpin.readline()
    bal1=fpin.readline()
    bal1=bal1.strip('\n')
    bal1=int(bal1)
    amt=int(amt)
    if accnt==toacc:
        messagebox.showinfo("OPERATION FAILED","INVALID ACCOUNT NUMBER")
        return
    if amt<=0:
        messagebox.showinfo("OPERATION FAILED","INVALID AMOUNT")
        return
    if(bal1<amt):
        messagebox.showinfo("Error","Insufficient balance")
        return
    bal1=bal1-amt
    fpin.readline()
    name1=fpin.readline()
    aadhar1=fpin.readline()
    phone1=fpin.readline()
    pan1=fpin.readline()
    fpin.close()
    try:
        fpin=open(toacc.strip('\n')+".txt","r")
        pin2=fpin.readline()
        bal2=fpin.readline()
        fpin.readline()
        
        name2=fpin.readline()
        aadhar2=fpin.readline()
        phone2=fpin.readline()
        pan2=fpin.readline()
        fpin.close()
        bal2=bal2.strip("\n")
        bal2=int(bal2)
        bal2=bal2+amt
        fpout=open(toacc.strip('\n')+".txt","w")
        fpout.write(pin2)
        fpout.write(str(bal2)+"\n")
        fpout.write(str(toacc)+"\n")
        fpout.write(name2)
        fpout.write(aadhar2)
        fpout.write(phone2)
        fpout.write(pan2)
        fpout.close()
        fpout=open(accnt+".txt","w")
        fpout.write(pin1)
        fpout.write(str(bal1)+"\n")
        fpout.write(accnt+"\n")
        fpout.write(name1)
        fpout.write(aadhar1)
        fpout.write(phone1)
        fpout.write(pan1)
        fpout.close()
        fpout=open(toacc.strip('\n')+"-rec.txt","a+")
        fpout.write(str(datetime.now())+"     "+str(amt)+"              "+str(bal2)+"     "+"TRANSFER FROM ACCOUNT "+str(accnt)+"\n")
        fpout.close()
        fpout=open(accnt.strip("\n")+"-rec.txt","a+")
        fpout.write(str(datetime.now())+"     "+"              "+str(amt)+"     "+str(bal1)+"     "+"TRANSFER TO ACCOUNT "+str(accnt)+"\n")
        
        messagebox.showinfo("OPERATION SUCESSFULL!!","Fund transfered")
    except:
        messagebox.showinfo("ERORR!!","Invalid account number"+toacc)
        return
    rootwn.deiconify()
def fund_transfer(accnt):
        global rootwn
        rootwn.iconify()
        ft=tk.Tk()
        ft.geometry("800x400")
        ft.title("FUND TRANSFER")
        ft.configure(background="green")
        fr1=tk.Frame(ft)
        fr1.pack(side="top")
        l_title=tk.Message(ft,text="BANK OF BUSSINESS",width=2000,padx=600,pady=0,fg="black",bg="red",justify="center",anchor="center")
        l_title.config(font=("Courier","50","bold"))
        l_title.pack(side="top")
        #label=tk.Label(text="Logged in as: "+name,relief="raised",font="Cambria 15 bold",bg="black",fg="white",anchor="center",justify="center")
        #l_title.pack(side="top")
        l1=tk.Label(ft,relief="raised",text="ENTER ACCOUNT NUMBER:" ,font="comicsansms 19 bold",bg="pink")
        l1.pack(side="top")
        e1=tk.Entry(ft,relief="raised",font="comicsansms 19 bold")
        e1.pack(side='top')
        l2=tk.Label(ft,relief="raised",text="ENTER AMOUNT:",font="comicsansms 19 bold",bg="pink")
        l2.pack(side="top")
        e2=tk.Entry(ft,relief="raised",font="comicsansms 19 bold")
        e2.pack(side="top")
        bt1=tk.Button(ft,text="TRANSFER",font="Cambria 20 bold",bg="white", command=lambda: transfer(accnt,e1.get().strip(),e2.get().strip()))
        bt1.pack(side="top")
def ques():
    qes=tk.Tk()
    qes.geometry("1000x900")
    qes.title("****HELP////WINDOW***")
    qes.configure(background="white")
    fr1=tk.Frame(qes)
    fr1.pack(side="top")
    l_title=tk.Message(qes,text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="black",bg="red",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    b1=tk.Button(qes,relief="raised",text="HOW I CAN CREDIT MY MONEY?" ,font="comicsansms 19 bold",bg="white",command=lambda: credit_help())
    b1.pack(side="top")
    b2=tk.Button(qes,relief="raised",text="HOW I CAN DEBIT MY MONEY?" ,font="comicsansms 19 bold",bg="white",command=lambda: debit_help())
    b2.pack(side="top")
    b3=tk.Button(qes,relief="raised",text="HOW I CAN I TRANSFER FUND TO ANOTHER ACCOUNT?" ,font="comicsansms 19 bold",bg="white",command=lambda: fund_trans_help())
    b3.pack(side="top")
    b4=tk.Button(qes,relief="raised",text="HOW I CAN CHECK MY BALANCE?" ,font="comicsansms 19 bold",bg="white",command=lambda: bal_help() )
    b4.pack(side="top")
    b5=tk.Button(qes,relief="raised",text="HOW I CAN CHANGE MY PIN?" ,font="comicsansms 19 bold",bg="white",command=lambda: pin_help())
    b5.pack(side="top")
    b6=tk.Button(qes,relief="raised",text="HOW I CAN VIEW MY TRANSACTION HISTORY?" ,font="comicsansms 19 bold",bg="white",command=lambda: trans_history())
    b6.pack(side="top")
    b7=tk.Button(qes,relief="raised",text="HOW I CAN CHANGE ACCOUNT DETALIAS?" ,font="comicsansms 19 bold",bg="white",command=lambda: acc_detail_help() )
    b7.pack(side="top")
    b8=tk.Button(qes,relief="raised",text="HOW I DO FAST WITHDRAW?" ,font="comicsansms 19 bold",bg="white",command=lambda: fcash_help())
    b8.pack(side="top")
def credit_help():
    cr=tk.Tk()
    cr.geometry("900x800")
    cr.title("****HELP////WINDOW~~~~CREDIT\\\\***")
    cr.configure(background="black")
    fr1=tk.Frame(cr)
    fr1.pack(side="top")
    l_title=tk.Message(cr,text=" BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="black",bg="red",justify="center",anchor="center")
    l_title.config(font=("Courier","40","bold"))
    l_title.pack(side="top")
    t=tk.Text(cr,height=50,width=550,font="Courier 12 bold",bg="pink")
    t.pack()
    text="""
After you Login, 
There Will Be 9 Buttons Namely,CREDIT IN YOUR ACCOUNT,DEBEIT IN YOUR ACCOUNT,
CHECK BALANCE,VIEW TRANSACTION.,DEBEIT IN YOUR ACCOUNT,VIEW TRANSACTION,BALANCE,
CHANGE ACCOUNT DETAILS,FUND TRANSFER,HELP,FAST CASH,CHANGE PIN....
By Clicking CREDIT IN YOUR ACCOUNT button You Can Deposit To the bank.
It will Ask How Much Amount You Need To deposit after entering it click CREDIT button          
"""
    t.insert(tk.END,text)
    t.configure(state="disabled")
    #filename=tk.PhotoImage(file="money.gif")
    #bglab=tk.Label(cr,image=filename)
    #bglab.place(x=0,y=0,relwidth=1,relheight=1)
    bg_image = tk.PhotoImage(file ="money.gif")
    x = tk.Label (cr,image = bg_image)
    x.place(y=0)
    
def debit_help():
    dh=tk.Tk()
    dh.geometry('900x800')
    dh.title("****HELP////WINDOW~~~~DEBIT\\\\***")
    dh.configure(background="white")
    fr1=tk.Frame(dh)
    fr1.pack(side="top")
    l_title=tk.Message(dh,text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="black",bg="red",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    t=tk.Text(dh,height=50,width=550,font="Courier 12 bold",bg="light blue")
    t.pack()
    text="""
After You Login,
THERE WILL BE 9 BUTTONS NAMELY,CREDIT IN YOUR ACCOUNT,DEBEIT IN YOUR ACCOUNT,CHECK BALANCE,
VIEW TRANSACTION,DEBEIT IN YOUR ACCOUNT,CHECK BALANCE,VIEW TRANSACTION,FUND TRANSFER,
EDIT ACCOUNT DETALIS,CHANGE PIN,FUND TRANSFER..........
THAT NEW PAGE THE BUTTON NAMED DEBIT ON MY ACCOUNT CLICK THAT.
NOW YOU CAN ENTER YOUR DEBIT MONEY AND CLICK DEBIT BUTTON.....
"""
    t.insert(tk.END,text)
    t.configure(state="disabled")

def fund_trans_help():
    fth=tk.Tk()
    fth.geometry("900x800")
    fth.title("***HELP////WINDOW~~~~~FUND TRANSFER**")
    fth.configure(background="white")
    fr1=tk.Frame(fth)
    fr1.pack(side="top")
    l_title=tk.Message(fth,text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="black",bg="red",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    t=tk.Text(fth,height=50,width=550,font="Courier 12 bold",bg="light green")
    t.pack()
    text="""
After You Login,
THERE WILL BE 9 BUTTONS NAMELY,CREDIT IN YOUR ACCOUNT,DEBEIT IN YOUR ACCOUNT,CHECK BALANCE,
VIEW TRANSACTION,DEBEIT IN YOUR ACCOUNT,CHECK BALANCE,VIEW TRANSACTION,FUND TRANSFER,
EDIT ACCOUNT DETALIS,CHANGE PIN,FUND TRANSFER..........
THERE THE BUTTON NAMED [FUNDTRANSFER] YOU CAN CLICK THAT...THE NEW WINDOW WILL BE OPENED
THERE WILL BE 2 BUTTONS [ACCOUNT NUMBER] [AMOUNT] YOU NEED TO ENTER THE TO ACCOUNT IN THE FIRST BUTTON AND
YOU NEED TO ENTER THE AMOUNT TO TRANSFER IN SECOND BUTTON
AFTER YOU ENTERED ALL THE DETAILS GIVE TRANSFER BUTTON.......
"""
    t.insert(tk.END,text)
    t.configure(state="disabled")
    
def bal_help():
    bh=tk.Tk()
    bh.geometry("500x500")
    bh.title("***HELP////WINDOW~~~~~FUND TRANSFER**")
    bh.configure(background="white")
    fr1=tk.Frame(bh)
    fr1.pack(side="top")
    l_title=tk.Message(bh,text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="black",bg="red",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    t=tk.Text(bh,height=50,width=550,font="Courier 12 bold",bg="light green")
    t.pack()
    text="""
After You Login,
THERE WILL BE 9 BUTTONS NAMELY,CREDIT IN YOUR ACCOUNT,DEBEIT IN YOUR ACCOUNT,CHECK BALANCE,
VIEW TRANSACTION,DEBEIT IN YOUR ACCOUNT,CHECK BALANCE,VIEW TRANSACTION,FUND TRANSFER,
EDIT ACCOUNT DETALIS,CHANGE PIN,FUND TRANSFER..........
YOU CHECK YOUR BALANCE BY CLICKING CHECK BALANCE BUTTON.THE BALANCE WILL BE SHOWN.
"""
    t.insert(tk.END,text)
    t.configure(state="disabled")
    
def pin_help():
    ph=tk.Tk()
    ph.geometry("800x800")
    ph.title("***HELP////WINDOW~~~~~FUND TRANSFER**")
    ph.configure(background="white")
    fr1=tk.Frame(ph)
    fr1.pack(side="top")
    t=tk.Text(ph,height=50,width=550,font="Courier 12 bold",bg="light blue")
    t.pack()
    text="""
AFTER LOGIN,
THERE WILL BE 9 BUTTONS NAMELY,CREDIT IN YOUR ACCOUNT,DEBEIT IN YOUR ACCOUNT,CHECK BALANCE,
VIEW TRANSACTION,DEBEIT IN YOUR ACCOUNT,CHECK BALANCE,VIEW TRANSACTION,FUND TRANSFER,
EDIT ACCOUNT DETALIS,CHANGE PIN,FUND TRANSFER..........
THERE YOU CLICK ON [CHANGE PIN]...A NEW WINDOW WILL BE OPENED....THERE IT WILL BE 2 BUTTONS...
2 BUTTONS NAMELY[NEW PIN],[RE-TYPE PIN]. YOU NEED TO TYPE YOUR NEW PIN IN FIRST BUTTON AND
FOR CONFORM YOU NEED TO TYPE AGAIN IN THE PIN IN SECOND BUTTON AND GIVE SUBMIT........
"""
    t.insert(tk.END,text)
    t.configure(state="disabled")
    
def trans_history():
    trans=tk.Tk()
    trans.geometry("800x800")
    trans.title("***HELP////WINDOW~~~~~TRANSACTION HISTORY**")
    trans.configure(bg="pink")
    fr1=tk.Frame(trans)
    fr1.pack(side="top")
    t=tk.Text(trans,height=50,width=550,font="Courier 12 bold",bg="light blue")
    t.pack()
    text="""
AFTER LOGIN,
THERE WILL BE 9 BUTTONS NAMELY,CREDIT IN YOUR ACCOUNT,DEBEIT IN YOUR ACCOUNT,CHECK BALANCE,
VIEW TRANSACTION,DEBEIT IN YOUR ACCOUNT,CHECK BALANCE,VIEW TRANSACTION,FUND TRANSFER,
EDIT ACCOUNT DETALIS,CHANGE PIN,FUND TRANSFER..........
YOU CAN CHECK YOUR TRANSACTION HISTORY BY CLICKING VIEW TRANSACTION HISTORY BUTTON.
AFTER CLICKING A NEW WINDOW WILL BE OPENED.THERE IT WILL BE DISPLAYED ON WHICH TIME,DATE
YOU HAVE DONE TRANSACTION
"""
    t.insert(tk.END,text)
    t.configure(state="disabled")
def acc_detail_help():
    adh=tk.Tk()
    adh.geometry("800x500")
    adh.title("***HELP////WINDOW~~~~~ACCOUNT DETAILS**")
    adh.configure(bg="pink")
    fr1=tk.Frame(adh)
    fr1.pack(side="top")
    t=tk.Text(adh,height=50,width=550,font="Courier 12 bold",bg="light blue")
    t.pack()
    text="""
AFTER LOGIN IN,
THERE WILL BE 9 BUTTONS NAMELY,CREDIT IN YOUR ACCOUNT,DEBEIT IN YOUR ACCOUNT,CHECK BALANCE,
VIEW TRANSACTION,DEBEIT IN YOUR ACCOUNT,CHECK BALANCE,VIEW TRANSACTION,FUND TRANSFER,
EDIT ACCOUNT DETALIS,CHANGE PIN,FUND TRANSFER..........
YOU CAN CLICK ON [EDIT ACCOUNT DETAILS].THERE IT WILL BE MORE OPTIONS.ONCE YOU HAVE ENTERED ALL
DETAILS YOU GIVE UPDATE......IT WILL BE UPDATED....
"""
    t.insert(tk.END,text)
    t.configure(state="disabled")
    
    
def fcash_help():
    fastcash=tk.Tk()
    fastcash.geometry("500x900")
    fastcash.title("transaction help")
    fastcash.configure(bg="pink")
    fr1=tk.Frame(fastcash)
    fr1.pack(side="top")
    T=tk.Text(fastcash,height=50,width=550,font="Courier 12 bold",bg="light blue")
    T.pack(side="top")
    text="""
AFTER  LOGIN 
IN,THE NEW WINDOW WILL OPENED.
THERE WILL BE 9 BUTTONS NAMELY,CREDIT IN YOUR ACCOUNT,DEBEIT IN YOUR ACCOUNT,CHECK BALANCE,
VIEW TRANSACTION,DEBEIT IN YOUR ACCOUNT,CHECK BALANCE,VIEW TRANSACTION,FUND TRANSFER,
EDIT ACCOUNT DETALIS,CHANGE PIN,FUND TRANSFER..........
THERE THE FAST CASH BUTTON WILL BE THERE BY CLICKING THAT WE CAN BE WITHDRAW BY CLICKING ONE BUTTON.
THERE ONLY 4 BUTTON,500,1000,5000,10000 BY CLICKING THAT BUTTON YOU CAN BE WITHRAW
"""

    
def fast_cash(accnt,name):
    fc=tk.Tk()
    fc.geometry("900x800")
    fc.title("***FAST CASH***")
    fc.configure(background="white")
    fr1=tk.Frame(fc)
    fr1.pack(side="top")
    l_title=tk.Message(fc,text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="black",bg="red",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    e1=500
    e2=1000
    e3=5000
    e4=10000
    b=tk.Button(fc,text="500",relief="raised",font="comicsansms 25 bold",bg="pink",fg="black",width=20,bd=12,command=lambda:debit_write(fc,500,accnt,name))
    b.pack(side="top")
    fc.bind("<Return>",lambda x:debit_write(fc,500,accnt,name))
    b2=tk.Button(fc,text="1000",relief="raised",font="comicsansms 25 bold",bg="pink",fg="black",width=20,bd=12,command=lambda:debit_write(fc,1000,accnt,name))
    b2.pack(side="top")
    fc.bind("<Return>",lambda x:debit_write(fc,1000,accnt,name))
    b3=tk.Button(fc,text="5000",relief="raised",font="comicsansms 25 bold",bg="pink",fg="black",width=20,bd=12,command=lambda:debit_write(fc,5000,accnt,name))
    b3.pack(side="top")
    fc.bind("<Return>",lambda x:debit_write(fc,5000,accnt,name))
    b4=tk.Button(fc,text="10000",relief="raised",font="comicsansms 25 bold",bg="pink",fg="black",width=20,bd=12,command=lambda:debit_write(fc,10000,accnt,name))
    b4.pack(side="top")
    fc.bind("<Return>",lambda x:debit_write(fc,5000,accnt,name))
def cnfm_block(delacc,accnt):
    global rootwn
    fpin=open(accnt+".txt","r")
    pin=fpin.readline()
    oc=fpin.readline()
    pas=fpin.readline()
    nam=fpin.readline()
    g=fpin.readline()
    h=fpin.readline()
    i=fpin.readline()
    j=fpin.readline()
    k="blocked"
    fpin.close()
    fpin=open(accnt+".txt","w")
    fpin.write(pin)
    fpin.write(oc)
    fpin.write(accnt+"\n")
    fpin.write(nam)
    fpin.write(g)
    fpin.write(h)
    fpin.write(i)
    fpin.write(j)
    fpin.write(k+"\n")
    fpin.close()
    messagebox.showinfo("PROCESS SUCESSFUL!!","ACCOUNT BLOCKED SUCESSFULLY ******TO UNBLOCK CONTACT BANK*****")
    delacc.destroy()
    rootwn.destroy()
    return

    
def block_accnt(accnt,name):
    delacc=tk.Tk()
    delacc.geometry("800x500")
    delacc.title("BLOCK ACCOUNT")
    delacc.configure(bg="pink")
    fr1=tk.Frame(delacc)
    fr1.pack(side="top")
    l_title=tk.Message(delacc,text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="black",bg="red",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    b1=tk.Button(delacc,text="BLOCK MY ACCOUNT",font="Courier 20 bold",bg="pink",bd=10,command=lambda: cnfm_block(delacc,accnt)).place(x=270,y=200)
    #b1.pack(side="top")

def terms_and_conditions():
    tac=tk.Tk()
    tac.geometry("900x900")
    tac.title("TERMS AND CONDITIONS")
    tac.configure(bg="light blue")
    fr1=tk.Frame(tac)
    fr1.pack(side="top")
    l_title=tk.Message(tac,text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="black",bg="red",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    S = tk.Scrollbar(tac)
    t=tk.Text(tac,width=200, height=50,bg="light blue")
    S.pack(side=tk.RIGHT, fill=tk.Y)
    t.pack(side=tk.LEFT, fill=tk.Y)
    t.config(yscrollcommand=S.set)
    text="""
Terms & Conditions
NOTICE
Your use of this website constitutes your agreement to be bound by these TERMS of use. By using this website you signify your assent to these terms of use. If you do not agree to these terms of use, please do not use the site.
Definitions
In this document the following words and phrases have the meaning set opposite them unless the context indicates otherwise:
BANK refers to Bank Of Bussiness , a body corporate constituted in India under the Banking Companies (Acquisition and Transfer of Undertakings) Act No. 5 of 1970 and having its Head Office at Karur and includes its successors and assigns.
WEBSITE means website of the http://www.bob.in.
Corporate means all accounts of sole proprietorship concern, partnership firm, Hindu Undivided Family, Public Limited Company, Private Limited Company, Trusts, Society, Government Departments and any other institution falling under this category.
Corporate User(s) refer(s) to an authorized person(s) on behalf of Corporate to avail Internet Banking Services of the Bank and such other similar services (hereinafter referred to as ONLINE SERVICES) that may be offered in future.
" INTERNET BANKING ACCOUNT " refers to any type of account so designated by the Bank for allowing Internet Banking facility.
PERSONAL INFORMATION refers to the information about the CORPORATE obtainedfor providing Internet Banking Service.
TERMS refer to Terms and Conditions for use of Internet Banking Services as specified herein and available at the Bank's website with URLs: http://www.pnbindia.in and/or http://www.netpnb.com and as modified from time to time.
Applicability of TERMS
These TERMS form the contract between the CORPORATE using the Internet Banking services and the BANK. By applying for Internet Banking Services and accessing the service the Corporate acknowledges and accepts these TERMS.
The user agrees that in the event the corporate or its user avails of any services offered by BANK through the website, the corporate or its user shall be bound by all the terms and conditions stipulated by BANK pertaining to such services offered by BANK from time to time and availed by the user through the aforesaid website(s).
The agreement shall remain valid until it is replaced by another agreement or terminated by either party or the account/s is/are closed, whichever is earlier.
Application for Internet Banking Services
The Bank may offer Internet Banking Services to select Corporate customer at its discretion. The Corporate customer would need to be a current Internet User or have legal access to the Internet and knowledge of its working. Submission of Form A or B and the acknowledgment thereof do not automatically imply the acceptance of application for providing Internet Banking Services by the Bank.
The Bank may, from time to time, advise the Internet softwares which are required for using Internet Banking Services by the Corporate customer. There will be no obligation on the part of the Bank to support all the versions of these Internet softwares. and their updates.
Internet Banking Services
The Bank shall endeavor to provide various banking services to the Corporate through Internet Banking Services, such as, inquiry about the balance in its account(s), details about transactions, statement of account(s), etc. These facilities may be offered in a phased manner at the discretion of the Bank. The Bank, at its sole discretion, may also make additions / deletions to the Internet Banking Services being offered to the Corporate. The availability / non-availability of a particular service shall be advised through e-mail or web page of the Bank or written communication.
The information provided to the Corporate through the Internet Banking Service is not updated continuously but at regular intervals. Consequently, any information supplied to the Corporate through Internet Banking Services will pertain to the date and time when it was last updated and not as the date and time when it is supplied to the Corporate. Bank shall not be liable for any loss that the Corporate may suffer by relying on or acting on such information.
The Bank may keep or maintain its records of the transactions as prescribed under the law for the time being in force. In any dispute, Bank's records shall be binding as the conclusive and best evidence of the transactions carried out through Internet Banking Service in the absence of clear proof that Bank's records are erroneous or incomplete.
The Bank shall take reasonable care to prevent unauthorized access and ensure reasonable security of the Internet Banking Services by using technology reasonably available to the Bank. in India.
The Corporate shall not use or permit to use Internet Banking Services or any other related service for any illegal, fraudulent, dishonest or improper purposes.
Internet Banking Service Access
After submission of the form(s), the Bank would be allot a Corporate ID along with the User ID and a secret password (to be used at the time of login) for Account Administrator in the first instance. The Account Administrator will define Corporate Users, as per the hierarchy, roles and limits. For authentication of the transactions, a separate transaction password will be allotted. As a safety measure, all the Corporate Users including the Account Administrator shall have to change the passwords after first login and accept terms and conditions coming on the computer screen before the system permit them to start using Internet Banking Services.
In addition to or in substitution of User ID and Password, the Bank may, at its discretion, advise the User to adopt such other means of authentication including but not limited to digital certification and / or smart cards. issued by licensed Certifying Authorities or vendors. The Corporate shall not attempt or permit others to attempt accessing the account information stored in the computers and computer networks of the Bank through any means other than the Internet Banking Services.
Functionalities available in Corporate Internet Banking Services
A) For viewing and generating reports-
•	Details for various types of deposits and loan accounts.
•	Account wise Last Ten Transactions , Account Details, Query Selection, Cheque Status Inquiry and Outward Clearing Instruments.
•	Details of Closed Accounts.
•	Bill alerts, Bill Presentment and Details of payment history.
•	Details of pending transfers and unapproved transfers.
•	Trade Finance Services -
•	Details of Import Documentary Credits, Import Bills, Amendment of letters of credit
•	Details of Export Documentary Credit, Export Bills, Export Loans
•	Details of Inland Bills and letters of credit.
•	Details of Bank Guarantees o Details of Forward Contracts
•	Mail option for sending mails to relationship manager.
•	Customise option to change password(s) and details of my profile, my billers, my beneficiaries
•	Inquiry regarding activity, limits and approvals.
•	Availability of functionalities with the Corporate Account Administrator:
•	Division Maintenance
•	Corp Level Account Maintenance
•	Corp Level User Maintenance
•	Enabling and disabling menu options for Corporate Users
•	View of records
•	Option to allot login time restrictions for Corporate Users
•	Fund Management Services with following functionalities -
•	MIS record maintenance
•	Collection Reports
•	Payment Reports
•	Deposit and Loan Modeling
B) Transaction functionalities
•	Online Transfer / Schedule Transfer of funds to own account(s)
•	Online Transfer / Schedule Transfer of funds to third party account(s)
•	Online Transfer / Schedule Transfer of funds to linked account(s)
•	Utility Bill Payments
•	Request for account opening / renewal of any type of account
•	Request for cheque book
•	Request for reporting loss of demand draft / cash order
•	Request for bill lodging (both inland and foreign)
•	Request for issuance of Demand Draft / Cash Order
•	Request for LC / LG opening / amendment
•	Request for funds transfer to non-CBS branches of PNB
•	Online opening of LC, LG and lodging of bills
•	Upload of files like salary upload, dealer debit upload, etc
•	Creation of / modifications in pool of accounts
•	Setting up of sweeping rules
Account Administrator
Every Corporate has to appoint an account administrator and convey the same to Bank along with a copy of the mandate containing such authorisation. Account Administrator will be the single point of contact for the Bank in all issues related to Internet Banking of the Corporate Accounts. He will be able to create new Corporate Users, allocate divisions to Corporate Users, maintain Corporate level accounts and allocate access of different customer ID to different Users and enable/disable menu option. However, for creation / modification of division, roles, hierarchy and transaction limits, fresh mandate needs to be submitted at the branch under signature of the persons duly authorised by the Corporate. All operations and/or transactions performed by the Account Administrator will be binding on the Corporate as he / she is the authorized person from the Corporate for doing all the aforesaid activities. However, the Account Administrator representing a Corporate may or may not be able to initiate any transaction depending upon the constitution of said Corporate.
Password
The Corporate User(s) must:

(a) keep the User ID and passwords totally confidential and not reveal the passwords to any person(s);
(b) change the password at the time of first log in;
(c) create a password of at least 6 characters long consisting of a mix of alphabets, numbers and special characters not relating to any readily accessible personal data, such as, his / her name, address, telephone number, vehicle number, driving licence no. etc. or easily guessable combination of letters and / or numbers;
(d) commit the User ID and passwords to memory and not record them in a written or electronic form; and
(e) not let any unauthorised person have access to his / her computer or leave the computer unattended while using Internet Banking Services.
In the event of forgetting of User ID and / or passwords or expiry / disability of password(s), the Corporate User can request for change of the passwords by sending a request to the Bank in writing through the Account Administrator. The selection of new passwords and / or replacement of User ID shall not be construed as the commencement of a new contract. The User agrees and acknowledges that Bank shall in no way be held responsible or liable if the User incurs any loss as a result of compromise of User-id and password by the User himself or User has failed to follow the Internet Banking Service instructions as published by the Bank on the website from time to time. User agrees to fully indemnify and hold harmless Bank in respect of the same.
Initially, the Account Administrator will be issued User ID and passwords by the Bank along with the Corporate ID. Account Administrator will create Corporate User(s) and allot User ID to him / her / them. Passwords will be printed by the Bank on the basis of request received from the Corporate User(s).
Partnership accounts
Internet Banking facility will be provided to the Account Administrator of partnership account. Partners will authorize one person among themselves or any other person for using Internet Banking Services. However, if the partners want to use Internet Banking Services themselves also, the same can be given to partners but it will be managed by the Account Administrator only. Partners will be the authorised persons to execute forms and mandates.
Private / Public Limited Company Accounts
Internet Banking facility will be provided to private / public limited company accounts. The company concerned has to authorize one person through a resolution passed by the Board of the company concerned to act as the Account Administrator. The Account Administrator will be single point of contact between the Bank and the company concerned for all Internet Banking requirements. The Account Administrator will be acting on behalf of the company concerned for creating Users with various rights, allocation of divisions and attaching accounts with Users. The persons authorized to execute forms and mandates will be informed to the Bank through a resolution passed by the Board of the company concerned.
Hindu Undivided Family Accounts
Internet Banking facility will be provided to the HUF accounts. Karta will be acting as the Account Administrator for Internet Banking Services and may appoint himself as a Corporate User.
Trust / Society Accounts
Internet Banking facility will be provided to the trust / society account. Trust / Society will authorize one person for using Internet Banking Services and he / she will act as the Account Administrator.
Requirement of Minimum Balance
The Corporate shall maintain, at all times, such minimum balance in Corporate Internet Banking account(s), as the Bank may stipulate from time to time. The Bank may, at its discretion, levy penal charges for non-maintenance of the minimum balance. The Bank may withdraw the Internet Banking Services facility, if at any time the amount of deposit falls short of the required minimum as aforesaid and / or if the other charges remain unpaid, without giving any further notice to the Corporate and / or without incurring any liability or responsibility whatsoever by reason of such withdrawal.
Charges
The Bank may, at its discretion, from time to time specify charges for usage of Internet Banking Services and / or additional charges for select services which will be advised to the Corporate at the time of opening the account and also be displayed on the website of the Bank. All out of pocket expenses, wherever applicable, will be borne by the Corporate.
Any further change in the charges / fees shall be displayed on the Bank's website. The Corporate authorizes Bank to recover all charges related to Internet Banking Services as determined by Bank from time to time by debiting Corporate Account held with the Bank.
The Bank may withdraw the Internet Banking Services, if at any time the amount of deposit falls short of the required minimum as aforesaid and/or if the service charges remain unpaid, without giving any further notice to the Corporate and/or without incurring any liability or responsibility whatsoever by reason of such withdrawal.
Funds Transfer
The Corporate shall advise its Users including the Account Administrator that they shall not use or attempt to use Internet Banking Services for funds transfer without sufficient funds in the relative Internet Banking Services account or without prior arrangement with the Bank for grant of an overdraft facility. The corporate shall also advise the users including Account Administrator that they should use or attempt to use funds transfer facility within the workflow limits.
The Bank will endeavor to effect such funds transfer transactions received through Internet Banking Services provided there are sufficient funds available in the Corporate account. The Bank shall not be liable for any omission to make all or any of the payments or for late payments due to circumstances beyond the reasonable control of the Bank.
If due to technical errors or non-giving effects to certain instructions, the account results in overdraft, the Corporate will be liable to refund the overdrawn amount along with interest as applicable to such type of accounts.
If fund transfer is made available to the Corporate, it may be used for transfer of funds from Account of the Corporate to other accounts belonging to third parties maintained at Bank (Intra- Bank transfers) and/or at any other Bank (Inter- Bank transfers), which falls under the network of Reserve Bank of India's Electronic Fund Transfer system. Only such User who has been specifically authorized by the Corporate in this behalf shall operate the fund transfer facility. Such User will be allowed to transfer funds using Corporate Internet Banking in accordance with the mandate / resolution submitted by the Corporate If the mandate given by the Corporate does not mention any upper limit for the funds transfer, Bank shall, at its discretion, be entitled to impose such limits for any funds transfer as it may decide and all transactions for amounts beyond such limits would be rejected.
However, in the event of users does funds transfer beyond his defined workflow limits, Corporate would be liable for such acts of its users including account administrator.
Authority to the Bank in case of Corporate Accounts
Banking transactions in the account(s) are permitted through Internet after authentication of the Corporate ID, User ID and passwords of the Corporate User(s) only. The Corporate gives an express authority to the Bank to carry out the Banking transactions performed by its Users through Internet Banking Services. The Bank shall have no obligation to verify the authenticity of any transaction purported to have been sent by the Corporate User via Internet Banking Services except verification of the Corporate ID, User ID and the passwords.
All transactions arising from the use of Internet Banking Services shall be binding on all the parties of the Corporate body, jointly and severally.
The display or printed output that is generated by the Corporate at the time of operation of Internet Banking Services is a record of the operation of the Internet access and shall not be construed as the Bank's record of the relative transactions. The Bank's own records generated by the transactions arising out of the use of the Internet Banking, including the time the transaction recorded shall be conclusive proof of the genuineness and accuracy of the transaction and shall be accepted as conclusive and binding for all purposes. While Bank shall endeavour to carry out the instructions promptly, it shall not be responsible for any delay in carrying on the instructions due to any reason whatsoever, including due to failure of operational systems or any requirement of law.
Instructions
All instructions for Internet Banking shall be given, through computer system or otherwise as advised by Bank for the purpose, by the User in the manner indicated by Bank. The User is also responsible for the accuracy and authenticity of the instructions provided to Bank and the same shall be considered to be sufficient to operate the Corporate Internet Banking Services. The Bank shall not be required to independently verify the instructions, and the instruction shall remain effective till such time the same is countermanded by further instructions by the User. Bank shall have no liability if it does not or is unable to stop or prevent the implementation of an instruction, which is subsequently countermanded. Where Bank considers the instructions to be inconsistent or contradictory it may seek clarification from the user before acting on any instruction of the user or act upon any such instruction as it deems fit. Bank states that it has no liability or obligation to keep a record of the instructions to provide information to the user or for verifying user's instructions. Bank may refuse to comply with the instructions without assigning any reason and shall not be under any duty to assess the prudence or otherwise of any instruction and have the right to suspend the operations through the Internet Banking if it has reason to believe that the User's instructions will lead or expose to direct or indirect loss or may require an indemnity from the Corporate before continuing to operate the Corporate Internet Banking Services.
Any instruction, order, direction, request entered/initiated using the password of the User shall be deemed to be an instruction, order, directive, request received from the User having a requisite mandate from Corporate. All instructions, requests, directives, orders, directions, entered/initiated by the User, either electronically or otherwise, are based upon the User's decisions and are the sole responsibility of the User and the Corporate. The User understands that entering /initiating an instruction, direction, order, request with Bank, either electronically or otherwise, does not guarantee execution of such instruction, direction, order or request. Bank shall not be deemed to have received any instruction, direction, order, request electronically transmitted by the User until it confirms the receipt of such instruction, direction, order, request.
Accuracy of Information
The Corporate is responsible for the correctness of information supplied to the Bank through the use of Internet Banking Services or through any other means, such as, electronic mail or written communication. The Bank accepts no liability for the consequences arising out of erroneous information supplied by the Corporate. If the Corporate suspects that there is an error in the information supplied to the Bank by him, he shall advise the Bank by the quickest means of communication. The Bank will endeavor to correct the error, wherever possible, on a 'best efforts' basis. If the Corporate notices an error in the information supplied to him through Internet Banking Service, he shall advise the BANK by the quickest means of communication. The Bank will endeavor to correct the error promptly, and adjust any interest or charges arising out of the error occurred at its end. The Bank accepts no liability for the consequences arising out of erroneous information supplied by the Corporate and shall not adjust any interest or charges arising out of such error.
Liability of the Corporate and the Bank
If the Corporate user has complied with the terms and advised the Bank in writing under acknowledgment of an authorized person of the Bank immediately after he / she suspects that his / her User ID or password(s) is / are known to another person and / or notices an unauthorised transaction(s) in his / her account, he / she shall not be liable for losses arising out of the unauthorised transaction(s) occurring in the accounts after the receipt of such advice by the Bank.
The Corporate user shall be liable for all loss of unauthorised transactions in the account(s) if he / she has breached the terms and conditions or contributed to or caused the loss by negligent actions, such as, the following:
1.	(a) in disclosing or failing to take all reasonable steps to prevent disclosure of the User ID and / or passwords to anyone including the Bank staff and / or failing to advise the Bank of such disclosure within a reasonable time; and/or
2.	(b) not advising the Bank in a reasonable time about unauthorised access to or erroneous transactions in the account(s) through the Internet Banking Services
The Bank shall not be liable for any unauthorised transaction(s) occurring through the use of Internet Banking Services, which can be attributed to the fraudulent or negligent conduct of the Corporate.
The Bank shall not be liable to the account holder(s) for any damages, whatsoever, whether such damages are direct, indirect, incidental, consequential and irrespective of whether any claim is based on loss of revenue, investment, production, goodwill, profit, interruption of business or any other loss of any character or nature, whatsoever, and whether sustained by the account holder(s) or any other person, if Internet Banking Services access is not available in the desired manner for reasons including but not limited to natural calamity, floods, fire and other natural disasters, legal restraints, faults in the telecommunication network or Internet or network failure, software or hardware error or any other reason(s) beyond the control of the Bank.
The Bank shall endeavor to take all reasonable steps to maintain secrecy and confidentiality of its Corporate account(s) and data/information but shall not be liable to the account holder(s) for any damages, whatsoever, caused on account of breach of secrecy/ confidentiality due to unauthorised access, damage, disruption, hacking, phishing, cyber attacks or technological errors in the system.
The Bank shall not be liable for any loss due to unauthorized transfer of funds through unauthorised access, phishing attacks, hacking, cyber attacks etc.
The Corporate agrees that the authentication of transactions effected by the Corporate Users on the Internet are done by the use of 'User ID' and 'passwords' and / or Digital Certificates including Corporate ID in Corporate Accounts. It is expressly agreed that any operation done by use of 'User ID' and 'passwords' including Corporate ID in the Corporate Accounts will be deemed to be genuine operation by the Corporate.
Disclaimer of Warranties
The User expressly agrees that use of the website is at its sole risk and cost. The services offered on the said website is provided on an "as is" and "as available" basis. Except as warranted in the Terms, Bank expressly disclaims all warranties of any kind, whether express or implied or statutory, including, but not limited to the implied warranties of merchantability, fitness for a particular purpose, data accuracy and completeness, and any warranties relating to non-infringement in Internet Banking. Bank does not warrant that access to the website and Internet Banking shall be uninterrupted, timely, secure, or error free nor does it make any warranty as to the results that may be obtained from the website or use, accuracy or reliability of Internet Banking. Bank will not be liable for any virus or computer contaminant that may enter the user's system as a result of the user using Internet for accessing Internet Banking. Bank does not guarantee to the user or any other third party that access to Internet Banking using Internet would be virus or computer contaminant free.
Indemnity
In consideration of Bank providing the Corporate the Internet Banking Services, the Corporate shall, at his own expense, indemnify and hold Bank, its directors and employees, representatives, agents and/or sub-agents as the case may be, indemnified against all losses and expenses on full indemnity basis which Bank may incur, sustain, suffer or is likely to suffer in connection with Bank execution of the Corporate's instructions and against all actions, claims, demands, proceedings, losses, damages, costs, charges and expenses as a consequence or by reason of providing a service through Internet Banking for any action taken or omitted to be taken by Bank, its officers, employees, agents and/or sub-agents on the instructions of the Corporate. The Corporate will pay Bank such amount as may be determined by Bank to be sufficient to indemnify it against any such, loss or expenses even though they may not have arisen or are contingent in nature. Further, the Corporate agrees, at its own expense, to indemnify, defend and hold harmless Bank, its directors and employees, representatives, agents, and sub-agents against any claim, suit, action or other proceeding brought against Bank, its directors and employees, representatives, agents, and sub-agents by a third party, to the extent that such claim, suit, action of other proceeding brought against Bank, its directors and employees, representatives, agents, and sub-agents is based on or arises in connection with the user of Internet Banking with reference to:
1.	a violation of the Terms contained herein by the Corporate;
2.	any deletions, additions, insertions or alterations to, or any unauthorized use of, Internet Banking by the Corporate;
3.	any misrepresentation or breach of representation or warranty made by the Corporate contained herein; or
4.	any breach of any covenant or obligation to be performed by the Corporate hereunder. The Corporate agrees to pay any and all costs, damages and expenses, including, but not limited to, reasonable attorneys' fees and costs awarded against it or otherwise incurred by or in connection with or arising from any such claim, suit, action or proceeding attributable to any such claim.
The Corporate hereby agrees that under no circumstances, Bank's aggregate liability for claims relating to Internet Banking, whether for breach of in tort (including but not limited to negligence) shall be limited to the transaction charges/fees or consideration paid by the user within the previous six (06) months for Internet Banking, excluding any amount paid towards transactions
Disclosure of Corporate Information
The Corporate agrees that the Bank or its contractors/sub-contractors, agents/sub-agents may hold and process its NON PUBLIC INFORMATION on computer, computer network or otherwise in connection with Internet Banking Services as well as for statistical analysis and credit scoring. The Corporate also agrees that the Bank may disclose, in strict confidence, to other institutions, such NON PUBLIC INFORMATION as may be reasonably necessary for reasons inclusive of, but not limited to, the following: for participation in any telecommunication or electronic clearing network, in compliance with a legal directive, for credit rating by recognised credit rating agencies, for fraud prevention purposes, for prevention of money laundering or illegal activities
Proprietary Rights
The Corporate acknowledges that the software being used for the Internet Banking Services as well as other Internet related softwares, which are required for accessing Internet Banking Services, are the legal property of the respective vendors. The permission given by the Bank to access Internet Banking Services will not convey any proprietary or ownership rights in the above software to the Corporate. The Corporate shall not attempt to modify, translate, disassemble, recompile or reverse engineer the software being used for Internet Banking Services or create any derivative product based on the software.
Change of Terms and Conditions
The Bank has the absolute discretion to amend or supplement any of the terms at any time. . The Bank may introduce new services, or withdraw any of the existing services from Internet Banking Services, whenever considered necessary. The existence and availability of the new functions will be notified to the Corporate as and when the same become available. By using these new services, the Corporate agrees to be bound by the applicable terms and conditions. . The Corporate shall be responsible for regularly reviewing these Terms including amendments thereto as may be posted on the website.If in the opinion of the Corporate, the changes are to their disadvantage, the Corporate may at its discretion opt to close the Account and/or discontinue with the Internet Banking, intimating Bank of the same.
Non-Transferability
The grant of facility of Internet Banking Services to a Corporate is not transferable under any circumstances and shall be used by the Corporate only
Termination of Internet Banking Service
The Corporate may request for termination of the Internet Banking Services facility any time by giving a written notice through the authorized persons as per the bank record. The Corporate will remain responsible for any transactions made on his / her account(s) prior to the time of such cancellation of the Internet Banking Services.
The Bank may withdraw the Internet Banking facility anytime after giving reasonable notice to the User through the web-site.
The closure of account by the Corporate will automatically terminate the Internet Banking Services.
The Bank may suspend or terminate the Internet Banking Services without prior notice if the Corporate has committed breach of these terms and conditions or the Bank comes to know about:
(a) appointment of an administrator, provisional liquidator, conservator, receiver, trustee, custodian or other similar official for it or in respect of all or substantially all its assets, or
(b) resolution passed for its winding-up, official management or liquidation (other than pursuant to a consolidation, amalgamation or merger, or
(c) becoming insolvent or is unable to pay its debts or fails or admits in writing its inability generally to pay its debts as they become due, or
(d) results in a judgment of insolvency or bankruptcy or the entry of an order for relief or the making of an order for its winding-up or liquidation, or
(e) proposed acquisition of assets by financial institution(s),
The termination of the Internet Banking Service shall be without prejudice to the execution of all outstanding Transactions entered into between the Parties. The Bank shall be entitled to receive all fees and other monies becoming due up to the date of such termination. Bank shall be entitled to deduct any sum payable to it from any amounts Bank may have to remit to the Corporate on termination of the Service. Bank reserves the right to interrupt, suspend or terminate, at any time, without specifying any reason, the access of the Corporate to the Internet Banking Services offered hereunder and will make best efforts to give the Corporate appropriate notice of the same without assigning any reason and without being liable for any loss/damage/cost of any nature whatsoever to the Corporate.
Notices
Notices under these terms and conditions may be given by the Bank and the Corporate in the following manner: Electronically to the mailbox of either party. Such notices will be regarded as being in writing or alternativelyDelivering them by hand or sending them by post to the Corporate address as per our record and in case of Bank to the address mentioned below- Internet Banking Section, Information Technology Division, Bank Of Bussiness,,Head Office-BharaniVidhayalaya,vennamalai karur, The Bank may display notices of general nature applicable to all Corporate of Internet Banking Services on its website. Such notices will have the same effect as a notice served individually to each Corporate. The Corporate is hereby advised that in the event he chooses to send a notice electronically to the mailbox of the Bank, a true copy of the same notice shall also be delivered to the Bank's aforementioned address either by hand or by post. Notice and instructions will be deemed served 7 days after publication on website or upon receipt in the case of hand delivery, telegram, telex or facsimile.
Governing laws and Jurisdiction
These terms and conditions and / or operations in the accounts of the Corporate maintained by the Bank and / or the use of services provided through Internet Banking Services, shall be governed by the laws of Republic of India. The Corporate agrees to abide by prevailing laws in respect of Internet Banking Services applicable in Republic of India. Bank accepts no liability whatsoever, direct or indirect for non-compliance with the laws of any country other than Republic of India. The mere fact that Internet Banking Services can be accessed through Internet by a Corporate from a country other than India shall not be interpreted to imply that the laws of the said country govern these terms and conditions and/or the operations in the accounts of the User through Internet and/or the use of Internet Banking Services. It is the responsibility of the Corporate to comply with any regulations prevailing in the country from where he is accessing the Internet. The Parties hereby agree that any legal action or proceedings arising out of the Terms for Internet Banking shall be brought in the courts, tribunals or forums at New Delhi in India and irrevocably submit themselves to the jurisdiction of such courts, tribunals or forums.
Proprietary and Intellectual Property Rights
The copyright, trademarks, logos, slogans and service marks displayed on the website are registered and unregistered intellectual property rights of Bank or of respective intellectual property right owners. Nothing contained on the website should be construed as granting, by implication, estoppel, or otherwise, any license or right to use any intellectual property displayed on the website without the written permission of Bank or such third party that may own the intellectual property displayed on the website. The Bank neither warrants nor represents that the use of materials displayed on the website by the Corporate will not infringe patent, copyright or any intellectual property rights or any other rights of third parties not owned by Bank. Bank grants the right to access the website to the Corporate and use the Internet Banking Services in accordance with these Terms. The Corporate acknowledges that the Services including, but not limited to, text, content, photographs, video, audio and/or graphics, are either the property of, or used with permission by, Bank and/or by the content providers and may be protected by applicable copyrights, trademarks, service marks, international treaties and/or other proprietary rights and laws of India and other countries, and the applicable Terms and Conditions.The Corporate should assume that everything it sees or reads on the website (collectively referred to as "content") is copyrighted/ protected by intellectual property laws unless otherwise provided and may not be used, except as provided in these Terms, without the prior written permission of Bank or the relevant copyright owner.
Any breach of the restrictions on use provided in these terms is expressly prohibited by law, and may result in severe civil and criminal penalties. Bank shall be entitled to obtain equitable relief (including all damage, direct, indirect, consequential and exemplary) over and above all other remedies available to it, to protect its interests therein. The Corporate acknowledges that the software underlying the Internet Banking Services as well as other Internet related software which are required for accessing service are the legal property of the respective vendors. The permission given by Bank to access the Services shall not convey any patent, copyright and licence, proprietary, trade secret or ownership rights or other intellectual property rights in the above software.
Force Majeure / Technical Difficulties
The Corporate specifically agrees to hold Bank harmless from any and all claims, and agrees that Bank shall not be liable for any loss, actual or perceived, caused directly or indirectly by government restriction, exchange or market regulation, war, strike, virus attacks, denial of service attacks, equipment failure, communication line failure, system failure, security failure on the Internet, unauthorised access, hacking, theft, phishing, or any problem, technological or otherwise or other conditions beyond Bank's control, that might prevent Corporate from accessing/operating or Bank from executing/validating an instruction, order, direction. Corporate further agrees that the it will not be compensated by Bank for "lost opportunity" in the form of notional profits/gains on orders, instructions, directions which could not be executed.
Links to Websites
This website may contain links to other websites operated by other third parties. Such links are provided for the convenience of the Corporate only and Bank does not control or endorse such websites, and is not responsible for their contents. The use of such website is also subject to the terms of use and other terms and guidelines, if any, contained within each such website. The linked websites are not under the control of Bank and it is not responsible for the contents of any linked website or any link contained in a linked website, advertisements appearing in or Services offered by or any changes or updates to such websites.
Amendments and Modifications
The Bank has the absolute discretion to amend or supplement these Terms herein, by modifying or rescinding any of the existing provisions or conditions or by adding any new provision or condition, by conspicuously posting notice of such amendment on the website or by providing written notice to the Corporate. Continued use of Internet banking Services after such notice will constitute acknowledgment and acceptance of such amendment.
Survival of Obligations
The obligations of the Parties under these Terms shall survive the termination of any Transaction and/or this Agreement.
Remedies Cumulative
Except as provided in these Terms, the rights, powers, remedies and privileges provided in these Terms are cumulative and not exclusive of any rights, powers, remedies and privileges provided by law.
No Waiver of Rights
A failure or delay in exercising any right, power or privilege in respect of these Terms will not be presumed to operate as a waiver, and a single or partial exercise of any right, power or privilege will not be presumed to preclude any subsequent or further exercise, of that right, power or privilege or the exercise of any other right, power or privilege.
Severability
If any provision or condition of these Terms shall be held to be invalid or unenforceable by reason of any law, rule, administrative order or judicial decision by any court, or regulatory or self-regulatory agency or body, such invalidity or unenforceability shall attach only to such provision or condition. The validity of the remaining provisions and conditions of this Agreement shall not be affected thereby and these Terms shall be carried out as if any such invalid or unenforceable provision or condition was not contained herein.
Legality of the Terms
Bank's performance of these Terms is subject to existing laws and legal process, and nothing contained in these Terms is in derogation of Bank's right to comply with governmental, court and law enforcement requests or requirements relating to the use of this website by the Corporate or information provided gathered by Bank in respect of such use.
General
These Terms contain Bank's entire arrangement (except as otherwise expressly provided herein) and supersede and replace any previously made proposals, representations, understandings and agreements, express or implied, either oral or in writing between the Corporate and Bank for Internet Banking. The Corporate acknowledges that it has not relied on any representation made by Bank or any of its employees or agents and has made its own independent assessment of Internet Banking. No third party will have any rights or claims under these Terms.
Applicability of Terms
These Terms form the contract between the Corporate using the Internet Banking Service and Bank. By applying for Corporate Internet Banking Service and accessing the service the Corporate acknowledges and accepts these Terms. These Terms will be in addition to and not in derogation of the terms and conditions relating to any account of the Corporate with the Bank.



"""
    t.insert(tk.END,text)
    t.configure(state="disabled")
    
    
def logged_in_menu(accnt,name):
	#rootwn=tk.Tk()
	global rootwn
	rootwn=tk.Tk()
	rootwn.geometry("1600x500")
	rootwn.title("BANK OF BUSSINESS-"+name)
	#rootwn.configure(background="black")
	#fr1=tk.Frame(rootwn)
	#fr1.pack(side="top")
	bg_image = tk.PhotoImage(file ="money.gif")
	x = tk.Label (image = bg_image)
	x.place(y=1)
	l_title=tk.Message(rootwn,text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="black",bg="red",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	label=tk.Label(text="Logged in as: "+name,relief="raised",font="Cambria 15 bold",bg="black",fg="white",anchor="center",justify="center")
	label.pack(side="top")
	#filename=tk.PhotoImage(file="money.gif")
	#bglab=tk.Label(rootwn,image=filename)
	#bglab.place(x=0,y=0,relwidth=1,relheight=1)
	img2=tk.PhotoImage(file="credit.gif")
	myimg2=img2.subsample(2,2)
	img3=tk.PhotoImage(file="debit.gif")
	myimg3=img3.subsample(2,2)
	img4=tk.PhotoImage(file="balance1.gif")
	myimg4=img4.subsample(2,2)
	img5=tk.PhotoImage(file="transaction.gif")
	myimg5=img5.subsample(2,2)
	img6=tk.PhotoImage(file="pin.gif")
	myimg6=img6.subsample(2,2)
	img7=tk.PhotoImage(file="change.gif")
	myimg7=img7.subsample(2,2)
	img8=tk.PhotoImage(file="fund.gif")
	myimg8=img8.subsample(2,2)
	img9=tk.PhotoImage(file="help.gif")
	myimg9=img9.subsample(2,2)
	img11=tk.PhotoImage(file="fast.gif")
	myimg11=img11.subsample(2,2)
	img12=tk.PhotoImage(file="block.gif")
	myimg12=img12.subsample(2,2)
	b2=tk.Button(image=myimg2,command=lambda: Cr_Amt(accnt,name))
	b2.image=myimg2
	b3=tk.Button(image=myimg3,command=lambda: De_Amt(accnt,name))
	b3.image=myimg3
	b4=tk.Button(image=myimg4,command=lambda: disp_bal(accnt))
	b4.image=myimg4
	b5=tk.Button(image=myimg5,command=lambda: disp_tr_hist(accnt))
	b5.image=myimg5
	b7=tk.Button(image=myimg6,command=lambda: change_password(accnt))
	b7.image=myimg6
	b7.pack(side="top")
	b8=tk.Button(image=myimg7,command=lambda: edit_accnt(accnt))
	b8.image=myimg7
	b8.pack(side="top")
	b9=tk.Button(image=myimg8,command=lambda: fund_transfer(accnt))
	b9.image=myimg8
	b9.pack(side="top")
	b10=tk.Button(image=myimg9,command=lambda:ques())
	b10.image=myimg9
	b10.pack(side="top")
	b12=tk.Button(image=myimg11,command=lambda:fast_cash(accnt,name))
	b12.image=myimg11
	b12.pack(side="top")
	b13=tk.Button(image=myimg12,command=lambda: block_accnt(accnt,name))
	b13.image=myimg12
	b13.pack(side="top")
	img10=tk.PhotoImage(file="logout.gif")
	myimg10=img10.subsample(2,2)
	b11=tk.Button(image=myimg10,command=lambda: logout(rootwn))
	b11.image=myimg10
	

	
	b2.place(x=100,y=150)
	b3.place(x=100,y=220)
	b4.place(x=900,y=150)
	b5.place(x=900,y=220)
	b11.place(x=550,y=430)
	b7.place(x=550,y=220)
	b8.place(x=550,y=300)
	b9.place(x=550,y=150)
	b10.place(x=550,y=370)
	b12.place(x=100,y=290)
	b13.place(x=900,y=300)

	
def logout(master):
	
	messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
	master.destroy()
	Main_Menu()

def check_log_in(master,name,acc_num,pin):
	if(check_acc_nmb(acc_num)==0):
		master.destroy()
		Main_Menu()
		return

	if( (is_number(name))  or (is_number(pin)==0) ):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		Main_Menu()
	else:
		master.destroy()

		logged_in_menu(acc_num,name)


def log_in(master):
        global e3
        global e2
        global e1
        master.destroy()
        loginwn=tk.Tk()
        loginwn.geometry("920x500")
        loginwn.title("Login in")
        #loginwn.configure(bg="black")
        #fr1=tk.Frame(loginwn,bg="blue")
        bg_image = tk.PhotoImage(file ="money.gif")
        x = tk.Label (image = bg_image)
        x.place(y=0)
        l_tittle=tk.Message(loginwn,text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="black",bg="white",justify="center",anchor="center")
        l_tittle.config(font=("Courier","50","bold"))
        l_tittle.pack(side="top")
        l1=tk.Label(loginwn,text="ENTER NAME:",relief="raised",font="Algerian 23 bold",fg="white",bg="black",bd=12,width=20)
        l1.place(x=100,y=100)
        #l1.pack(side="top")
        e1=tk.Entry(loginwn,font="Cambria 20 bold",bg="white",relief="raised",bd=9,width=20)
        e1.place(x=550,y=100)
        #e1.pack(side="top")
        l2=tk.Label(loginwn,text="ENTER ACCOUNT NUMBER",font="Algerian 23 bold",relief="raised",fg="white",bg="black",bd=12)
        l2.place(x=100,y=170)
        #l2.pack(side="top")
        e2=tk.Entry(loginwn,font="Cambria 20 bold",bg="white",relief="raised",width=20,bd=12)
        e2.place(x=550,y=170)
        l3=tk.Label(loginwn,text="ENTER PIN",font="Algerian 23 bold",relief="raised",fg="white",bg="black",bd=12,width=20)
        l3.place(x=100,y=240)
        #l3.pack(side="top")
        e3=tk.Entry(loginwn,show="*",font="Cambria 20 bold",bg="white",bd=12,width=20,relief="raised")
        e3.place(x=550,y=240)
        #e3.pack(side="top")
        b=tk.Button(loginwn,text="SUBMIT",font="Cambria 20 bold",bg="black",fg="white",width=15,bd=12,command=lambda: check_log_in(loginwn,e1.get().strip(),e2.get(),e3.get().strip()))
        b.place(x=450,y=350)
        #b.pack(side="top")
        b1=tk.Button(text="HOME",relief="raised",font="Cambria 18 bold",bg="black",fg="white",width=15,bd=12,command=lambda: home_return(loginwn))
        b1.place(x=450,y=430)
        #b1.pack(side="top")
        #loginwn.bind("<Return>",lambda x:check_loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip())
        
        
	
def Create():
	
	crwn=tk.Tk()
	global check
	global rootwn
	rootwn.iconify()
	crwn.geometry("1600x1200")
	crwn.title("Create Account")
	fr1=tk.Frame(crwn,bg="blue")
	crwn.configure(bg="black")
	bg_image10 = tk.PhotoImage(file ="bv.gif")
	z3 = tk.Label (image = bg_image10)
	l_title=tk.Message(crwn,text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="black",bg="grey",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(crwn,text="ENTER NAME:",relief="raised",font="comicsansms 27 bold",bg="yellow",width=21,bd=12).place(x=100,y=100)
	#l1.pack(side="top")
	#lf1=tk.Label(crwn,text="dhayanandapathy",font="comicsansms 27 bold",bg="grey",bd=12).place(x=1030,y=150)
	e1=tk.Entry(crwn,font="comicsansms 27 bold",bg="white",bd=9)
	e1.place(x=600,y=100)
	#e1.pack(side="top",)
	l2=tk.Label(crwn,text="ENTER OPENING CREDIT:",relief="raised",font="comicsansms 27 bold",bg="yellow",width=21,bd=12).place(x=100,y=170)
	#l2.pack(side="top")
	e2=tk.Entry(crwn,font="comicsansms 27 bold",bg="white",bd=9)
	e2.place(x=600,y=170)
	#e2.pack(side="top")
	l3=tk.Label(crwn,text="SET PIN:",relief="raised",font="comicsansms 27 bold",bg="yellow",width=21,bd=12).place(x=100,y=240)
	lf1=tk.Label(crwn,text="IT SHOULD BE EXACT 4 DIGIT",font="comicsansms 16 bold",bg="black",fg="white",height=2).place(x=1030,y=240)
	#l3.pack(side="top")
	e3=tk.Entry(crwn,show="*",font="comicsansms 27 bold",bg="white",bd=9)
	e3.place(x=600,y=240)
	#e3.pack(side="top")
	l4=tk.Label(crwn,text="AADHAR CARD NUMBER",relief="raised",font="comicsansms 27 bold",bg="yellow",width=21,bd=12).place(x=100,y=310)
	lf2=tk.Label(crwn,text="EG:1111 2222 3333",font="comicsansms 16 bold",bg="black",fg="white",height=2,bd=2).place(x=1030,y=310)
	#l4.pack(side="top")
	e6=tk.Entry(crwn,font="comicsansms 27 bold",bg="white",bd=9)
	e6.place(x=600,y=310)
	#e6.pack(side="top")
	l5=tk.Label(crwn,text="PHONE NUMBER",relief="raised",font="comicsansms 27 bold",bg="yellow",width=21,bd=9).place(x=100,y=380)
	lf1=tk.Label(crwn,text="EG:9876543210",font="comicsansms 16 bold",bg="black",fg="white",height=2).place(x=1030,y=380)
	#l5.pack(side="top")
	e77=tk.IntVar()
	e7=tk.Entry(crwn,font="comicsansms 27 bold",bg="white",bd=9)
	e7.place(x=600,y=380)
	#e7.pack(side="top")
	l6=tk.Label(crwn,text="PAN NUMBER",relief="raised",font="comicsansms 27 bold",bg="yellow",width=21,bd=12).place(x=100,y=450)
	lf1=tk.Label(crwn,text="EG:ASDFG1020G",font="comicsansms 16 bold",bg="black",fg="white",height=2).place(x=1030,y=450)
	#l6.pack(side="top")
	e8=tk.Entry(crwn,font="comicsansms 27 bold",bg="white",bd=9)
	e8.place(x=600,y=450)
	l7=tk.Label(crwn,text="TYPE OF ACCOUNT",relief="raised",font="comicsansms 27 bold",bg="yellow",width=21,bd=12).place(x=100,y=520)
	e1.get()
	e2.get()
	e3.get()
	e6.get()
	e7.get()
	e8.get()
	var1 = tk.IntVar()
	tk.Radiobutton(crwn, text="CURRENT ACCOUNT",font="comicsansms 10 bold",bd=3,relief="raised",bg="white",command=abcd,value=1,variable=var1).place(x=600,y=520)
	tk.Radiobutton(crwn, text="SAVINGS ACCOUNT",font="comicsansms 10 bold",bd=3,relief="raised",bg="white",command=abce,value=2,variable=var1).place(x=600,y=550)
	tk.Checkbutton(crwn, text="I AGREE BANK TERMS AND CONDITIONS",font="comicsansms 10 bold",bd=3,relief="raised",bg="white",command=abc).place(x=800,y=590)
	b1=tk.Button(crwn,text="TEMS &CONDITONS",relief="raised",font="comicsansms 18 bold",bg="yellow",width=21,bd=10,command=lambda: terms_and_conditions()).place(x=500,y=640)
	#e8.pack(side="top")
	b=tk.Button(crwn,text="Submit",font="Cambria 20 bold",command=lambda: write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip(),e6.get().strip(),e7.get().strip(),e8.get().strip())).place(x=600,y=580)
	#b.pack(side="top")
	crwn.bind("<Return>",lambda x:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip(),e6.get().strip(),e7.get().strip(),e8.get().strip()))
	return
       

def abcd():
    global acctype
    acctype="current"
def abce():
    global acctype
    acctype="savings"
    

def abc():
    global check
    if check==0:
        check=1
    else:
        check=0



#def time():
    #root=Tk()
    #root.title('clock')
    #string=strftime('%H:%M:%S %p')
    #lbl=Label(rootwn,font=("Courier","50"))
#lbl.config(text=string)
#lbl.after(1000, time)
#lbl.pack(anchor='top')
#time()
    
def Main_Menu():


	#rootwn=tk.Tk()
	global rootwn
	rootwn=tk.Tk()
	rootwn.geometry("1600x1200")
	rootwn.title("BANK OF BUSSINESS")
	rootwn.configure(background='white')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	bg_image = tk.PhotoImage(file ="bank.gif")
	x = tk.Label (image = bg_image)
	x.place(y=0)
	l_title=tk.Message(text="BANK OF BUSSINESS",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	imgc1=tk.PhotoImage(file="new.gif")
	imglo=tk.PhotoImage(file="login.gif")
	imgc=imgc1.subsample(2,2)
	imglog=imglo.subsample(2,2)

	b1=tk.Button(image=imgc,command=Create)
	b1.image=imgc
	b2=tk.Button(image=imglog,command=lambda: log_in(rootwn))
	b2.image=imglog
	img6=tk.PhotoImage(file="quit.gif")
	myimg6=img6.subsample(2,2)

	b6=tk.Button(image=myimg6,command=rootwn.destroy)
	b6.image=myimg6
	b1.place(x=800,y=300)
	b2.place(x=800,y=200)	
	b6.place(x=800,y=450)
	l1=tk.Label(rootwn,text=
"""
CREATED & DEVELOPED BY S.DHAYANANDAPATHY.
FOR MORE DETAILS CONTACT dhayanandapathy@gmail.com
THANKS FOR USING MY PROGRAM """,relief="raised",font="comicsansms 10 bold",fg="black",bg="white",bd=5).place(x=800,y=550)

	rootwn.mainloop()

Main_Menu()
