   
   
from tkinter import *
import random
root=Tk()
root.title("picnick list")
root.geometry("500x500")
enternamem = Entry(root)
enternamem.place(relx=0.5,rely=0.2,anchor=CENTER)
frendlist=Label(root)
randomnumber=Label(root)
bestfind=Label(root) 
list1=[]
def addfrind() :
    frindname=enternamem.get()
    list1.append(frindname)
    frendlist["text"]="picnick list"+str(list1)
    
    
def no1():
    length=len(list1)
    randomno1=random.randint(0,length-1)
    randomnumber["text"]=str(randomno1)
    bestfind["text"]="your best is "+str(list1[randomno1])

bts=Button(root,text="add baglist",command=addfrind)
bts.place(relx=0.5,rely=0.3,anchor=CENTER)
frendlist.place(relx=0.5,rely=0.4,anchor=CENTER)
bts1=Button(root,text="",command=no1)
bts1.place(relx=0.5,rely=0.5,anchor=CENTER)
randomnumber.place(relx=0.5,rely=0.6,anchor=CENTER)
bestfind.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()

            