from tkinter import *
from tkinter import ttk
import math 
window=Tk()
window.title("Заголовок окна программы")
window.geometry("1000x1000")
level1=Frame(window)
level2=Frame(window)
level3=Frame(window)
level4=Frame(window)

b1=Button(level3,text='1',width=7,height=4,bg='grey')
b2=Button(level3,text='2',width=7,height=4,bg='grey')
b3=Button(level3,text='3',width=7,height=4,bg='grey')
b4=Button(level2,text='4',width=7,height=4,bg='grey')
b5=Button(level2,text='5',width=7,height=4,bg='grey')
b6=Button(level2,text='6',width=7,height=4,bg='grey')
b7=Button(level1,text='7',width=7,height=4,bg='grey')
b8=Button(level1,text='8',width=7,height=4,bg='grey')
b9=Button(level1,text='9',width=7,height=4,bg='grey')
b0=Button(level4,text='0',width=7,height=4,bg='grey')
b_delete=Button(level1,text='C',width=7,height=4,bg='grey')
b_plus=Button(level2,text='+',width=7,height=4,bg='grey')
b_minus=Button(level3,text='-',width=7,height=4,bg='grey')
b_dash=Button(level4,text='/',width=7,height=4,bg='grey')
b_mult=Button(level4,text='*',width=7,height=4,bg='grey')
b_reset=Button(level4,text='AC',width=7,height=4,bg='grey')

def one():
    Label["text"]=Entry.get('1')
def two():
    Label["text"]=Entry.get('2')
def three():
    Label["text"]=Entry.get('3')
def four():
    Label["text"]=Entry.get('4')
def five():
    Label["text"]=Entry.get('5')
def six():
    Label["text"]=Entry.get('6')
def seven():
    Label["text"]=Entry.get('7')
def eight():
    Label["text"]=Entry.get('8')
def nine():
    Label["text"]=Entry.get('9')
def zero():
    Label["text"]=Entry.get('0')

self.b1.bind(1,one())
b1.bind(2,two())
b1.bind(3,three())
b1.bind(4,four())
b1.bind(5,five())
b1.bind(6,six())
b1.bind(7,seven())
b1.bind(8,eight())
b1.bind(9,nine())
b1.bind(0,zero())
ttk.Entry().pack(anchor=CENTER,padx=1,pady=1,fill=BOTH)
level1.pack()
level2.pack()
level3.pack()
level4.pack()
b0.pack(side=LEFT)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)
b5.pack(side=LEFT)
b4.pack(side=LEFT)
b6.pack(side=LEFT)
b7.pack(side=LEFT)
b8.pack(side=LEFT)
b9.pack(side=LEFT)
b_delete.pack(side=LEFT)
b_plus.pack(side=LEFT)
b_minus.pack(side=LEFT)
b_dash.pack(side=LEFT)
b_mult.pack(side=LEFT)
b_reset.pack(side=LEFT)
window.mainloop()
