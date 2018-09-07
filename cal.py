from tkinter import *

#on button click insert
def click(screen,number):
    screen.insert(END,number)
    if number == "=":
        screen.insert(END,)

def evaluate(screen):
    currentText = screen.get(1.0,END)
    try:
        screen.insert(END,"=")
        screen.insert(END,eval(currentText))
    except SyntaxError:
        screen.insert(END,'<ERROR>')
def clr(screen):
    screen.delete(1.0,END)

class Calculator:
    def __init__(self,master):
        self.master = master
        master.title("Calculator")
        master.geometry("360x360")

#calculation area
        screen =Text(master,width=20,height=2,borderwidth=4,highlightthickness=10,font=("Arial",22))
        screen.grid(row=0,column=0,columnspan=5,padx=4,pady=5)
#buttons
        btn1 = Button(bg="light blue",text='1',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: click(screen,1))
        btn1.grid(sticky="nsew",padx=2,row=1,column=0,pady=1,ipadx=10,ipady=10)
        btn2 = Button(bg="light blue",text='2',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: click(screen,2))
        btn2.grid(sticky="nsew",row=1,column=1,pady=1,ipadx=10,ipady=10)
        btn3 = Button(bg="light blue",text='3',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: click(screen,3))
        btn3.grid(sticky="nsew",row=1,column=2,pady=1,ipadx=10,ipady=10)
        btn4 = Button(bg="light blue",text='4',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: click(screen,4))
        btn4.grid(sticky="nsew",padx=2,row=2,column=0,pady=1,ipadx=10,ipady=10)
        btn5 = Button(bg="light blue",text='5',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: click(screen,5))
        btn5.grid(sticky="nsew",row=2,column=1,pady=1,ipadx=10,ipady=10)
        btn6 = Button(bg="light blue",text='6',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: click(screen,6))
        btn6.grid(sticky="nsew",row=2,column=2,pady=1,ipadx=10,ipady=10)
        btn7 = Button(bg="light blue",text='7',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: click(screen,7))
        btn7.grid(sticky="nsew",padx=2,row=3,column=0,pady=1,ipadx=10,ipady=10)
        btn8 = Button(bg="light blue",text='8',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: click(screen,8))
        btn8.grid(sticky="nsew",row=3,column=1,pady=1,ipadx=10,ipady=10)
        btn9 = Button(bg="light blue",text='9',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: click(screen,9))
        btn9.grid(sticky="nsew",row=3,column=2,pady=1,ipadx=10,ipady=10)
        btn0 = Button(bg="light blue",text='0',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: click(screen,0))
        btn0.grid(sticky="nsew",row=4,column=1,pady=1,ipadx=10,ipady=10)
        btne = Button(bg="light green",text='=',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: evaluate(screen))
        btne.grid(sticky="nsew",row=4,column=2,pady=1,ipadx=10,ipady=10)
        btnb = Button(text='C',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: clr(screen))
        btnb.grid(sticky="nsew",row=4,column=0,pady=1,ipadx=10,ipady=10)
        btna = Button(bg="light yellow",text='+',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: click(screen,"+"))
        btna.grid(sticky="nsew",row=1,column=3,pady=1,ipadx=10,ipady=10)
        btns = Button(bg="light yellow",text='-',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: click(screen,"-"))
        btns.grid(sticky="nsew",row=2,column=3,pady=1,ipadx=10,ipady=10)
        btnm = Button(bg="light yellow",text='x',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: click(screen,"*"))
        btnm.grid(sticky="nsew",row=3,column=3,pady=1,ipadx=10,ipady=10)
        btnd = Button(bg="light yellow",text='/',width=5,font=("Arial",12,"bold"),borderwidth=5,command=lambda: click(screen,"/"))
        btnd.grid(sticky="nsew",row=4,column=3,pady=1,ipadx=10,ipady=10)
#initialize
win = Tk()
cal = Calculator(win)
win.mainloop()
