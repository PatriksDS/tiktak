from tkinter import*
from tkinter import messagebox

mansLogs=Tk()
mansLogs.title("TikTacToe")

speletajsX=True
count=0

def disablebButtons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)
    return 0

def reset():
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn1['text']=''
    btn2['text']=''
    btn3['text']=''
    btn4['text']=''
    btn5['text']=''
    btn6['text']=''
    btn7['text']=''
    btn8['text']=''
    btn9['text']=''

btn1=Button(mansLogs,text="",width=6,height=3,command=lambda:btnClick(btn1),font=('Helvica'))
btn2=Button(mansLogs,text="",width=6,height=3,command=lambda:btnClick(btn2),font=('Helvica'))
btn3=Button(mansLogs,text="",width=6,height=3,command=lambda:btnClick(btn3),font=('Helvica'))
btn4=Button(mansLogs,text="",width=6,height=3,command=lambda:btnClick(btn4),font=('Helvica'))
btn5=Button(mansLogs,text="",width=6,height=3,command=lambda:btnClick(btn5),font=('Helvica'))
btn6=Button(mansLogs,text="",width=6,height=3,command=lambda:btnClick(btn6),font=('Helvica'))
btn7=Button(mansLogs,text="",width=6,height=3,command=lambda:btnClick(btn7),font=('Helvica'))
btn8=Button(mansLogs,text="",width=6,height=3,command=lambda:btnClick(btn8),font=('Helvica'))
btn9=Button(mansLogs,text="",width=6,height=3,command=lambda:btnClick(btn9),font=('Helvica'))

galvenaIzvelne=Menu(mansLogs)
mansLogs.config(menu=galvenaIzvelne)

opcijas=Menu(galvenaIzvelne,tearoff=False)
galvenaIzvelne.add_cascade(label="Opcijas",menu=opcijas)

opcijas.add_command(label="jauna spēle",command=reset)
opcijas.add_command(label="Iziet",command=mansLogs.quit)

btn1.grid(row=0,column=0)
btn2.grid(row=1,column=0)
btn3.grid(row=2,column=0)
btn4.grid(row=0,column=1)
btn5.grid(row=1,column=1)
btn6.grid(row=2,column=1)
btn7.grid(row=0,column=2)
btn8.grid(row=1,column=2)
btn9.grid(row=2,column=2)



def btnClick(button):
 global speletajsX,count
 if button["text"]==""and speletajsX==True:
    button["text"]="X"
    speletajsX=False
    count+=1
    chechWinner()
 elif button["text"]=="" and speletajsX==False:
    button["text"]="O"
    speletajsX=True
    count+=1
    chechWinner()
 else:
     messagebox.showerror("TicTacToe","Šeit jau ir x vai O")



def chechWinner():
    global winner
    if (btn1["text"]=="X" and btn2["text"]=="X" and btn3["text"]=="X"
    or btn4["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X" 
    or btn7["text"]=="X" and btn8["text"]=="X" and btn9["text"]=="X"
    or btn1["text"]=="X" and btn5["text"]=="X" and btn9["text"]=="X"
    or btn1["text"]=="X" and btn4["text"]=="X" and btn7["text"]=="X"
    or btn2["text"]=="X" and btn4["text"]=="X" and btn8["text"]=="X"
    or btn3["text"]=="X" and btn6["text"]=="X" and btn9["text"]=="X"
    or btn3["text"]=="X" and btn5["text"]=="X" and btn7["text"]=="X"):

        winner=True
    
        messagebox.showinfo("TicTacToe","SpeletajsX ir uzvarējis")

    elif(btn1["text"]=="O" and btn2["text"]=="O" and btn3["text"]=="O"
    or btn4["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O" 
    or btn7["text"]=="O" and btn8["text"]=="O" and btn9["text"]=="O"
    or btn1["text"]=="O" and btn5["text"]=="O" and btn9["text"]=="O"
    or btn3["text"]=="O" and btn5["text"]=="O" and btn7["text"]=="O"
    or btn1["text"]=="O" and btn4["text"]=="O" and btn7["text"]=="O"
    or btn2["text"]=="O" and btn4["text"]=="O" and btn8["text"]=="O"
    or btn3["text"]=="O" and btn6["text"]=="O" and btn9["text"]=="O"):

        winner=True
        messagebox.showinfo("TicTacToe","SpeletajsO ir uzvarējis")

    elif count==9 :
      winner=False
      messagebox.showinfo("TicTacToe","Neizšķirts")
    return

mansLogs.mainloop()