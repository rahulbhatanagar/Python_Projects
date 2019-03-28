from tkinter import*
wn=Tk()
wn.title('Phone book')
wn.geometry('300x200')

fr1=Frame(wn)
fr1.pack(fill=Y)
labN=Label(fr1,text='Name')
labN.grid(row=0,column=0)
enN=Entry(fr1)
enN.grid(row=0,column=1)
labT=Label(fr1,text='Telephone')
labT.grid(row=1,column=0)

enT=Entry(fr1)
enT.grid(row=1,column=1)

def delF():
    index=contacts.curselection()[0]
    contacts.delete(index)

def addF():
    name=enN.get()
    tel=enT.get()
    if name=='' or tel=='':
        labE.config(text='Fields are Empty')
    else:
        contacts.insert(END,name+' - '+tel)
        enN.delete(0,END)
        enT.delete(0,END)
        labE.config(text='')

def editF():
    index=contacts.curselection()[0]
    name=enN.get()
    tel=enT.get()
    if name=='' or tel=='':
        labE.config(text='Fields are Empty')
    else:
        contacts.delete(index)
        contacts.insert(index,name+' - '+tel)
        enN.delete(0,END)
        enT.delete(0,END)
        labE.config(text='')

fr2=Frame(wn)
fr2.pack()
addB=Button(fr2,text='Add Contact',command=addF)
addB.grid(row=0,column=0)
delB=Button(fr2,text='Delete Contact',command=delF)
delB.grid(row=0,column=1)
editB=Button(fr2,text='Edit Contact',command=editF)
editB.grid(row=0,column=2)

fr3=Frame(wn)
fr3.pack()
scroll=Scrollbar(fr3)
scroll.pack(side=RIGHT)
contacts=Listbox(fr3,yscrollcommand=scroll.set,height=10)
scroll.config(command=contacts.yview)
contacts.pack(side=LEFT)
labE=Label(fr3,text='',fg='red')
labE.pack()
contacts.insert(END,'Number1','Number2','Number3')
