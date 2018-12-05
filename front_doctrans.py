#junk
# import tkinter as tk
#from tkinter import Tk, Label, Button, StringVar, Entry, Grid
from tkinter import *
#root = Tk()
import dt1backund
# modified above 1515Nov18 1900edt
# calls in the secondary program : like subroutine call
# above import fails and cmtd out  until later
rt=Tk()
# commenting out next line 15Nov18 200pm dt1backend
# rt = tk.Tk()
# rt=Tk()  alternate command to create a new window and call it rt
# rt.title ("Document Transitor Test Alternate")

# ==========================================
rt.title("Document Transistor 02Dec2018")
# window.title ("juboRasp") old junk

rt.geometry ("1000x600")
#label upcoming
# commented out next two lines 1515Nov18 220pm
#title = rt.Label (text="entry screen")

#title.grid (column=0, row=0)

#==== Labels for screen entry boxes=====
r=2
l0=Label(rt,text="Enter Transactn Below")
l0.grid(row=r-1,column=0)

l1=Label(rt,text="wheen ")
l1.grid(row=r+1,column=0)

l2=Label(rt,text="dlrs ")
l2.grid(row=r+2,column=0)

l3=Label(rt,text="who_store ")
l3.grid(row=r+3,column=0)

l4=Label(rt,text="pmt_kind ")
l4.grid(row=r+4,column=0)

# ====== data entry specifications for input variables [empty entry blocks for data] =
wheen=StringVar()
e1=Entry(rt,textvariable=wheen)
e1.grid(row=r+1,column=1)

dlrs=StringVar()
e2=Entry(rt,textvariable=dlrs)
e2.grid(row=r+2,column=1)

who_store=StringVar()
e3=Entry(rt,textvariable=who_store)
e3.grid(row=r+3,column=1)

pmt_kind=StringVar()
e4=Entry(rt,textvariable=pmt_kind)
e4.grid(row=r+4,column=1)

# ==Listbox Section : box sits below the entry field boxes ==GB===
# ===  scroll bar on right associated with Listbox ===
# lb01.configure(yscroll?????)
lb01=Listbox(rt,height=6,width=40)
lb01.grid(row=8,column=0, rowspan=8, columnspan=6)
sb01=Scrollbar(rt)
sb01.grid(row=7,column=5,rowspan=8)
lb01.configure(yscrollcommand=sb01.set)
sb01.configure(command=lb01.yview)

# ++++ COMMAND FUNCTIONS SECTION +++++
#=== a set of xxx_command lines "called by button (below) pushes by
# === "control" buttons ===================
# === below is view_command but needs editing for the lbl definition ===
# === lb01 relates to Listbox ====
def view_command():
    lb01.delete(0,END)
# === the below is a looping that sets otherwhere defined dt1backund.view as
#=== the variable rows  (so we have for each row in rows do the work) ====
    for row in dt1backund.view():
        lb01.insert(END,row)

"""
def add_command():
    if(len(wheen.get())!=0):
        dt1backund.addrec (wheen.get(),dlrs.get(),who_store.get(),pmt_kind.get())
"""
#===Phase Two: ====GB===
def add_command():
    if(len(wheen.get())!=0):
        dt1backund.addrec (wheen.get(),dlrs.get(),who_store.get(),pmt_kind.get())
#=== park or copy or list that record into the Listbox +++ ====
        lb01.delete(0,END)
        lb01.insert(END,(wheen.get(),dlrs.get(),who_store.get(),pmt_kind.get()))
# a tuple is created above on the insert by use of extra parens====
# ===== Phase Three =====16Nov18===
def dele_command():
    if(len(wheen.get())!=0):
        dt1backund.dele(tt[0])
#=======clearit_command()
#=======view_command()
# ==== the clearit_command ==== tt 18Nov18 =====
def clearit_command():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
# === end clearit_command =====
# ==== the findit command ==== tt 18Nov18 =====
def findit_command():
    lb01.delete(0,END)
#=== deletes everything showing in list box ===
    for row in dt1backund.findit(wheen.get(), dlrs.get(), who_store.get(), pmt_kind.get()):
        lb01.insert(END,row)
# ==at the end of work in the back end the ftn there "returns the call" ===
#== to the above "for row in dt1bakund ..." and the reply is ====
#=== "for row in rows"=== a funny re-construction on the reply ====
# ===== end the findit_command === makes call to backend file ===
# =======the update command === tt 18Nov18 ====
"""
#==GB code===

def updt_command():
    if(len(fn.get())!=0):
        be.updt(tt[0], fn.get(),ln.get(),dpt.get(),sal.get())
# ==tt notes that GB have no view_command() === 02Dec18 ===
#==end GB code==
"""
def updt_command():
    if(len(wheen.get())!=0):
        dt1backund.updt(tt[0],wheen.get(),dlrs.get(), \
        who_store.get(),pmt_kind.get())
"""

 def updt_command():
    if(len(fn.get())!=0):
        be.updt(tt[0], fn.get(),ln.get(),dpt.get(),sal.get())
#       view_command  #rem out ==02Dec18 tt ===

# === junk   if(not(e1.get("1.0",END))=="\n"):
# === junk       zbe.updt(tt[0], e1.get("1.0",END),e2.get("1.0",END))
# === junk    view_command()
"""
# ==== end commands section of code stack ==============


# ======== Fetch the Records from Database section ==================
# === define the gtr =====

"""
def gdr(event): # gtr = get the record
    global tt       # target tuple
    yoid=lb1.curselection()[0] # gets the
                                               # actual nbr
                                               # in: listbox
    # lb1.curselection()[0] <== order nbr in dbase & listbox
    tt=lb1.get(yoid) # get rec assoc'd w/yoid

    # lb1.curselection()[0] <== order nbr in dbase & listbox
    # tt[0] is the primary field: id, of that record.
    # print(lb1.curselection()[0],tt[0])
    e1.delete(0,END)
    e1.insert(END,tt[1])
    e2.delete(0,END)
    e2.insert(END,tt[2])
    e3.delete(0,END)
    e3.insert(END,tt[3])
    e4.delete(0,END)
    e4.insert(END,tt[4])

"""
# ====== gtr = get the record or gdr = get dat record === vernacular 
def gdr(event):
    global tt # = tuple()
# ========= target tuple === gbobal variable declared
    yoid=lb01.curselection()[0]
    # gets the actual nbr in listbox = lb01 (name of listbox)
    # lb1.curselection()[0] <== order nbr in dbase & listbox
    tt=lb01.get(yoid)
    # get rec assoc'd w/yoid

    # lb1.curselection()[0] <== order nbr in dbase & listbox
    # tt[0] is the primary field: id, of that record.
    # print(lb1.curselection()[0],tt[0])
    e1.delete(0,END)  # ==wheen==
    e1.insert(END,tt[1])
    e2.delete(0,END)  # === dlrs ===
    e2.insert(END,tt[2])
    e3.delete(0,END)    # === who_store ===
    e3.insert(END,tt[3])
    e4.delete(0,END)     # === pmt_kind===
    e4.insert(END,tt[4])

# ===== end the fetch the records section of code stack =====
#===========Bind function============
# === tf forgot to put in this section earlier ===
# === tf was wondering where the gdr was called 04Dec2018===
lb01.bind('<<ListboxSelect>>', gdr)
"""
lb1.bind('<<ListboxSelect>>', gdr)
# we gotta define the func gdr
# in the define cmds area, at the top
# g=get  d=dat   r=record
"""

# ++++ BUTTON DEFINITIONS SECTION +++++
# ====instantiate button on screen to activate the manipulation of data in 
#===== entry fields to the database ====
# =======Button : btn01 =======
btn01=Button(rt,text="NuRcd:Add", width=15, command=add_command)
btn01.grid(row=0,column=1)
#=======================end Button :btn01 ================
# ======== Phase Three : additional buttons different by text - xxx_command
# ====== and screen - position ==== grayed out for now ===
# ==== GB has changed my btn01 to be second button ====
#=== below Buttons : btn02-07 : tt made 16Nov18 0800edt +++++===
# === each button has a corresponding def command type section so as to issue \
# === a call to the database ======

btn02=Button(rt,text="Read:Lst", width=15, command=view_command)
btn02.grid(row=0,column=0)

btn03=Button(rt,text="Drp:Del", width=15, command=dele_command)
btn03.grid(row=0,column=2)
""" ===GB button no4 ===
b4=Button(rt,text="Update", width=10, command=updt_command)
b4.grid(row=0,column=4)
=== end GB button no4 ===
"""
# tt btn04 enabled 02Dec18 0900 edt===
btn04=Button(rt,text="Mod:Updt", width=15, command=updt_command)
btn04.grid(row=0,column=3)
btn05=Button(rt,text="Sch:Fnd", width=15, command=findit_command)
btn05.grid(row=0,column=4)
btn06=Button(rt,text="Clear:Blnk", width=15, command=clearit_command)
btn06.grid(row=0,column=5)
btn07=Button(rt,text="Exit:Clse", width=10, command=rt.destroy)
btn07.grid(row=0,column=7)
# === exit button needs no associated commands or funtion calls===
# ===== delete definitions section ======
"""

def dele_command():
    if(not(e1.get("1.0", END)=="\n")):
        x1=int(tt[0])
        print(x1)
        zbe.dele(x1)
        # print("Record: ",selected_tuple[0], "deleted")
        e1.delete("1.0",END)
        e2.delete("1.0",END)
        print(str(tt))
        # lb1.delete(0,END)
        # lb1.insert(END,"Deleted:" + str(tt))
        view_command()
"""
# below old code from GB that commented out ======
"""
def dele2_command():
    be.dele(selected_tuple[0])
    print("Record: ",selected_tuple[0], "deleted")
    e1.delete("1.0",END)
    e2.delete("1.0",END)
    view_command()
"""
# ====== clearit_command section used to clear ======
"""
def clearit_command():
    e1.delete('1.0',END)
    e2.delete('1.0',END)
    # e3.delete(0,END)
    # e4.delete(0,END)
"""
# ======== Update section of code from GB
"""
def updt_command():
    if(not(e1.get("1.0",END))=="\n"):
        zbe.updt(tt[0], e1.get("1.0",END),e2.get("1.0",END))
        view_command()
"""
# ======= view the record from GB ????? say tlf
"""
def view_command():
    lb1.delete(0,END)
    for row in zbe.view():
        lb1.insert(END,row)
"""
# ======== Find the record GB copy ===tlf say seems wrap issue on one line below ====
"""
def findit_command():
    lb1.delete(0,END)
    for row in zbe.findit(e1.get("1.0", 'end-1c').strip(), e2.get("1.0",'end-1c').strip()):
        lb1.insert(END,row)
"""
# ============ Add a record section GB copy =============
"""
def add_command():
    if(not(e1.get("1.0", END)=="\n")):
        zbe.addrec(e1.get("1.0", END),e2.get("1.0", END))
        lb1.delete(0,END)
        lb1.insert(END,(e1.get("1.0", END),e2.get("1.0", END)))
        clearit_command()
        view_command()

"""

# ================================================
# ===functions are done say GB =========
#===== Labels for side of program GB origin =========
"""
r=2
#l0=Label(rt,text="")
# l0.grid(row=1,column=0)
# tlf say no know about this r=2 funny assignment

# ======= Data Entry Variables section =========

e1=Text(rt, height=6, width=20, font=('arial',24,'bold'))
e1.grid(row=r,column=1)

e2=Text(rt, height=6, width=35, font=('arial',24,'bold'))
e2.grid(row=r,column=2)

"""

# ====== Listbox section ================
"""
lb1=Listbox(rt,height=9, width = 50, font=('arial',24,'bold'))
lb1.grid(row=4, column=1,rowspan=9,columnspan=2)

sb=Scrollbar(rt)
sb.grid(row=3,column=4,rowspan=7)

lb1.configure(yscrollcommand=sb.set)
sb.configure(command=lb1.yview)

"""
# ===== bind function section =======
"""
lb1.bind('<<ListboxSelect>>', gdr)
# we gotta define the func gdr
# in the define cmds area, at the top
# g=get  d=dat   r=record

"""
# ======= buttion section from GB code ======
""""
b1=Button(rt,text="Q&A Recs", width=10,command=view_command)
b1.grid(row=0,column=0)

b2=Button(rt,text="Delete", width=10, command=dele_command)
b2.grid(row=1,column=0)

b3=Button(rt,text="Add Rec", width=10, height=5,command=add_command)
b3.grid(row=2,column=0)

b4=Button(rt,text="Update", width=10, height=5,command=updt_command)
b4.grid(row=3,column=0)

b5=Button(rt,text="Find", width=10,command=findit_command)
b5.grid(row=4,column=0)

b6=Button(rt,text="Clear", width=10, height=4,command=clearit_command)
b6.grid(row=5,column=0)

b7=Button(rt,text="Exit", width=10,command=rt.destroy)
b7.grid(row=6,column=0)

"""
# ==== old buttons section ======
"""
button100 = tk.Button(text="push button 01")

button100.grid(column=0,row=1)
# ==== old entry section ====
entry_field100 = tk.Entry()
entry_field100.grid(column=0, row=2)
"""
# ========================= primary window creation ======
rt.mainloop()  # alternate expression for GB model advanced
# window.mainloop()
