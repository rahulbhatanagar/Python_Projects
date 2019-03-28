from tkinter import *
from math import *
a=Tk(className="Calculator")
e=Entry(a,width=40,bd=10)
e.grid(columnspan=5)
def sine():
       e.insert(END,"sin")
def cosine():
       e.insert(END,"cos")
def trc():
       e.insert(END,"ten")
def openbrac():
       e.insert(END,"(")
def closebrac():
       e.insert(END,")")
def add():
       e.insert(END,"+")
def delete():
       e.delete(0,END)
       e.insert(END,0)
def zero():
       e.insert(END,"0")
def clear():
       e.delete(0)
       #e.insert(END,8)
def mns():
       e.insert(END,"-")
def mply():
        e.insert(END,"*")     
def div():
        e.insert(END,"/")
def dec():
       e.insert(END,".")
def addmns ():
       e.insert(END,"+-")
def one():
       e.insert(END,"1")                                                                                        
def two():
       e.insert(END,"2")
def three():
       e.insert(END,"3")
def four():
       e.insert(END,"4")
def five():
       e.insert(END,"5")
def six():
       e.insert(END,"6")
def seven():
       e.insert(END,"7")
def eight():
       e.insert(END,"8")
def nine():
       e.insert(END,"9")

def eq():
        s=eval (e.get())
        e.delete (0,END)
        e.insert (0,s)

b=Button(a,text="+",command=add,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b.grid(row=3,column=4)
b1=Button(a,text="-",command=mns,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b1.grid(row=2,column=4)
b2=Button(a,text="*",command=mply,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b2.grid(row=1,column=3)
b3=Button(a,text="/",command=div,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b3.grid(row=1,column=2)
b4=Button(a,text=".",command=dec,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b4.grid(row=5,column=2)
b4=Button(a,text="1",command=one,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b4.grid(row=4,column=1)
b5=Button(a,text="2",command=two,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b5.grid(row=4,column=2)
b6=Button(a,text="3",command=three,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b6.grid(row=4,column=3)
b7=Button(a,text="4",command=four,bg="cyan",relief="raised",underline=0,state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b7.grid(row=3,column=1)
b8=Button(a,text="5",command=five,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b8.grid(row=3,column=2)
b9=Button(a,text="6",command=six,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b9.grid(row=3,column=3)
b10=Button(a,text="7",command=seven,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b10.grid(row=2,column=1)
b11=Button(a,text="8",command=eight,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b11.grid(row=2,column=2)
b12=Button(a,text="9",command=nine,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b12.grid(row=2,column=3)
b13=Button(a,text="+-",command=addmns,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b13.grid(row=5,column=3)
b14=Button(a,text="0",command=zero,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b14.grid(row=5,column=1)
b15=Button(a,text="C",command=delete,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b15.grid(row=1,column=1)
b18=Button(a,text="D",command=clear,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b18.grid(row=1,column=4)
b19=Button(a,text="(",command=openbrac,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b19.grid(row=4,column=4)
b20=Button(a,text=")",command=closebrac,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b20.grid(row=5,column=4)
b23=Button(a,text="SIN",command=sine,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b23.grid(row=6,column=1)
b24=Button(a,text="COS",command=cosine,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b24.grid(row=6,column=2)
b25=Button(a,text="TEN",command=trc,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b25.grid(row=6,column=3)

b17=Button(a,text="=",command=eq,bg="cyan",relief="raised",state="active",activebackground="gray",activeforeground="blue",width=7,height=2)
b17.grid(row=6,column=4)

