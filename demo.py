from tkinter import *

root=Tk()
 
def b_click(number):
  cur = e.get()
  e.delete(0,END)
  e.insert(0,str(cur)+str(number))

def b_clear():
	e.delete(0,END)

def b_add():
	global f_num
	f_num=int(e.get())
	e.delete(0,END)

def b_equal():
	s_num = e.get()
	e.delete(0,END)
	sum = int(f_num) + int(s_num)
	e.insert(0,sum)
	f_num = int(sum)
    
def b_mul():
 return

def b_sub():
 return

def b_div():
 return

root.title("simple calculator")
e=Entry(root)
e.grid(row=0,column=0,columnspan=3)

b1=Button(root,text='1',padx=10,pady=5,command=lambda:b_click(1))
b2=Button(root,text='2',padx=10,pady=5,command=lambda:b_click(2))
b3=Button(root,text='3',padx=10,pady=5,command=lambda:b_click(3))
b4=Button(root,text='4',padx=10,pady=5,command=lambda:b_click(4))
b5=Button(root,text='5',padx=10,pady=5,command=lambda:b_click(5))
b6=Button(root,text='6',padx=10,pady=5,command=lambda:b_click(6))
b7=Button(root,text='7',padx=10,pady=5,command=lambda:b_click(7))
b8=Button(root,text='8',padx=10,pady=5,command=lambda:b_click(8))
b9=Button(root,text='9',padx=10,pady=5,command=lambda:b_click(9))
b0=Button(root,text='0',padx=10,pady=5,command=lambda:b_click(0))

b_add=Button(root,text='+',padx=15,pady=5,command=b_add)
b_equal=Button(root,text='=',padx=20,pady=5,command=b_equal)
b_clear=Button(root,text='C',padx=25,pady=5,command=b_clear)

b_mul=Button(root,text='*',padx=20,pady=5,command=b_mul)
b_sub=Button(root,text='-',padx=20,pady=5,command=b_sub)
b_div=Button(root,text='/',padx=20,pady=5,command=b_div)


b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b0.grid(row=4,column=0)

b_clear.grid(row=4,column=1,columnspan=2)
b_add.grid(row=5,column=0)
b_equal.grid(row=5,column=1,columnspan=2)

b_mul.grid(row=6,column=0)
b_sub.grid(row=6,column=1)
b_div.grid(row=6,column=2)


root.mainloop()