import tkinter as tk


main=tk.Tk()
main.geometry("900x600")
main.title("TRANSLATOR")
main.configure(background="light blue")
fr1=tk.Frame(main)
fr1.pack(side="top")
b1=tk.Label(main,text="TAMIL TO THAMIZHI",font="Cambria 20 bold",bg="red",relief="raised",bd=9)
b1.place(x=300,y=100)
#b1.pack(side="top")
b3=tk.Label(main,text="ENTER YOUR TAMIL WORD",font="Cambria 20 bold",bg="black",fg="white",relief="raised",bd=9)
b3.place(x=100,y=200)
#b3.pack(side="top")
trans=tk.Entry(main,font="Cambria 20 bold",bg="white",relief="raised",bd=9,width=20)
trans.place(x=500,y=200)
#b4.pack(side="top")
b2=tk.Button(main,text="SUBMIT",font="Cambria 20 bold",bg="green",relief="raised",bd=9,width=20,command=lambda: translate(trans) )
b2.place(x=300,y=300)
#b2.pack(side="top")
    
def translate(trans):
    #global b4
    transwn=tk.Tk()
    transwn.geometry("1000x900")
    transwn.title("Translation")
    fr1=tk.Frame(transwn)
    fr1.pack(side="top")
    b1=tk.Label(transwn,text="YOUR TRANSLATION",font="Cambria 20 bold",bg="white",relief="raised",bd=9,width=20)
    b1.pack(side="top")
    #t=tk.Text(transwn,height=50,width=550,font="Courier 12 bold",bg="light green")
    #t.pack()
    #text="""

#"""
    #t.insert(tk.END,text)
    ast=tk.Label(transwn,text="TAMIL",font="Cambria 20 bold",bg="red",relief="raised",bd=9,width=20)
    ast.place(x=50,y=100)
    g=tk.Label(transwn,text="TAMIZHI",font="Cambria 20 bold",bg="red",relief="raised",bd=9,width=20)
    g.place(x=500,y=100)
    a=tk.Entry(transwn,font="Cambria 110 bold",bg="white",relief="raised",width=5)
    a.place(x=50,y=200)
    b=tk.Entry(transwn,font="Cambria 110 bold",bg="white",relief="raised",width=5)
    b.place(x=500,y=200)
    print(trans)
    #print(b4)

    subm=tk.Button(transwn,text="SUBMIT",font="Cambria 20 bold",bg="green",relief="raised",bd=9,width=20)
    subm.place(x=350,y=500)
    
    
