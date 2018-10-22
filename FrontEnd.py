
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
from datetime import date
import fk as f
import tkinter as tk
import datetime
import string
#var declaration

now= datetime.datetime.now()
tdate=now.strftime("%Y-%m-%d")



window = Tk()
 
window.title("ExpMan")
window.geometry('400x400')   


v = tk.StringVar()
tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4= ttk.Frame(tab_control)
tab_control.add(tab1, text='Entry')
tab_control.add(tab2, text='Check')
tab_control.add(tab3, text='Search with date')
tab_control.add(tab4 , text='Search with Name ')
#tab1 stuff 
lbl = Label(tab1, text="Entry", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)

    
s_lbl1=Label(tab1 , text = "Name")
s_lbl1.grid(column=0,row=1)
s_lbl2=Label(tab1 ,text="Amount")
s_lbl2.grid(column=0,row=2)
s_txt = Entry(tab1,width=20)
s_txt.grid(column=1, row=1)
s_txt1 = Entry(tab1,width=20)
s_txt1.grid(column=1, row=2)
#radio buttons
#function for raddio buttons
def chk(ck):
    if len(ck.get())==0:
        messagebox.showinfo('Warning', 'Fields cant be empty')
        return False
    else:
        return True
#for default selection of checkbox

v = IntVar()
v.set(1)


rad1 = Radiobutton(tab1,text='Expense', value=1,variable=v) 
rad2 = Radiobutton(tab1,text='Income', value=2,variable=v)

typ=''

rad1.grid(column=0, row=3)
rad2.grid(column=1, row=3)
def clicked():
    if chk(s_txt) and chk(s_txt1) :
        nm=s_txt.get()
        amnt=s_txt1.get()
        if v.get() is 1:
            typ=True
        elif v.get() is 2:
            typ=False
        else:
            typ=True
        f.add(nm,amnt,tdate,typ)
        
    
btn = Button(tab1, text="Click Me", command=clicked) 
btn.grid(column=1, row=4)

#tab2 stuff
l_lbl=Label(tab2, text="Check if You can spent ",font=("Arial Bold", 10))
l_lbl.grid(column=0, row=0)
l_lbl1=Label(tab2 , text = "Amount")

l_lbl1.grid(column=0,row=1)
l_lbl2=Label(tab2 , text = "Check")

l_lbl2.grid(column=0,row=2)

l_lbl3=Label(tab2 , text = "Remaining")
l_lbl3.grid(column=0,row=3)

l_txt = Entry(tab2,width=20)
l_txt.grid(column=1, row=1)

d_lbl = Label(tab2, text=" ")
d_lbl.grid(column=1, row=2)


d_lbl2 = Label(tab2, text=" ")
d_lbl2.grid(column=1, row=3)

def clicked2():
        inf=l_txt.get()
        state,ans=f.check(int(inf),tdate)
        if state:
            d_lbl.configure(text="yes")
        else:
            d_lbl.configure(text="No")
            
        d_lbl2.configure(text=ans)
       
btn1 = Button(tab2, text="Click Me", command=clicked2) 
btn1.grid(column=1, row=4)

#tab3 stuff
#start date

l_lbl2=Label(tab3, text="Start",font=("Arial Bold", 10))
l_lbl2.grid(column=0, row=0)

spin = Spinbox(tab3, from_=1, to=31, width=5)
spin.grid(column=0,row=1)

spin1 = Spinbox(tab3, from_=1, to=12, width=5)
spin1.grid(column=1,row=1)

spin2 = Spinbox(tab3, from_=2000, to=2019, width=5)
spin2.grid(column=2,row=1)

#end date


l_lbl3=Label(tab3, text="End",font=("Arial Bold", 10))
l_lbl3.grid(column=0, row=2)

spi = Spinbox(tab3, from_=1, to=31, width=5)
spi.grid(column=0,row=3)
    
spi1 = Spinbox(tab3, from_=1, to=12, width=5)
spi1.grid(column=1,row=3)

spi2 = Spinbox(tab3, from_=2000, to=2019, width=5)
spi2.grid(column=2,row=3)

l_bl3=Label(tab3, text="")
l_bl3.grid(column=1, row=5) 
        
    
def newform():
    l_l2=Label(tab3, text="Name")
    l_l2.grid(column=0, row=6)
    l_l3=Label(tab3, text="Name of Expnese ")
    l_l3.grid(column=0, row=6)
    s_t = Entry(tab3,width=20)
    s_t.grid(column=1, row=6) 
    
    l_l4=Label(tab3, text="Money Spent")
    l_l4.grid(column=0,row=7)
    l_l5=Label(tab3, text="")
    l_l5.grid(column=1,row=7)
    
    def clicked4():
        val=s_t.get()
        neval="'"+val+"'"
        startDate,endDate=clicked3()    
        answer=f.createView1(startDate,endDate,neval)
        l_l5.configure(text=answer)
    
    bn2 = Button(tab3, text="Click Me", command=clicked4) 
    bn2.grid(column=1, row=8)
    

    
    

def clicked3():
    sd1=spin.get()
    sd2=spin1.get()
    sd3=spi2.get()
    if int(sd2)<10:
        sd2='0'+sd2
    if int(sd1)<10:
        sd1='0'+sd1
    
    ed1=spi.get()
    ed2=spi1.get()
    ed3=spi2.get()
    
    if int(ed2)<10:
        ed2='0'+ed2
    
    if int(ed1)<10:
        ed1='0'+ed1
        
    #merging of dates
    startDate= "'"+sd3+"-"+sd2+"-"+sd1+"'"
    endDate = "'"+ed3+"-"+ed2+"-"+ed1+"'"
    #total expenses in these dates
    dis=f.createView(startDate,endDate)
    l_bl3.configure(text=dis)
    newform()
    return startDate,endDate
    

btn2 = Button(tab3, text="Click Me", command=clicked3) 
btn2.grid(column=1, row=4)
    
#tab4 stuff
tbl2=Label(tab4, text="Name of Expense or Income")
tbl2.grid(column=0, row=0)
tbt = Entry(tab4,width=20)
tbt.grid(column=1, row=0)
tbl3=Lable(tab4,text="")
tbl3.grid(column=1,row=4)                                                                                                                                                                                                                                               
v = IntVar()
v.set(1)

nrad1 = Radiobutton(tab4,text='Expense', value=1,variable=v) 
nrad2 = Radiobutton(tab4,text='Income', value=2,variable=v)

nrad1.grid(column=0, row=3)
nrad2.grid(column=1, row=3)

def clkd():
    
    par=tbt.get()
    par="'"+par+"'"
    if v.get() is 1:
        prnt=f.find(par,'EXPENSE')
        tbl3.configure(text=prnt)
    else:
        prnt=f.find(par,'INCOME')
        tbl3.configure(text=prnt)
        
fbtn2 = Button(tab4, text="Click Me", command=clkd) 
fbtn2.grid(column=1, row=5)


tab_control.grid() 
window.mainloop()