from cgitb import text
from tkinter import*
root = Tk()
root.title("Division")
root.geometry("720x640")
Label(root,text="num1",font="italic 14 bold",bg="light blue",width=15,height=1,borderwidth=3,relief=SUNKEN).grid()
Label(root,text="num2",bg="light blue",font="italic 14 bold",width=15,height=1,borderwidth=3,relief=SUNKEN).grid()
Label(root,text="result",bg="light blue",font="italic 14 bold",width=15,height=1,borderwidth=3,relief=SUNKEN).grid(row=3)
number1 =StringVar()
number2 = StringVar()

def devide():
    try:
        n1 = int(e1.get())
        n2 = int(e2.get())
        r = n1/n2
        res.config(bg="light green")  
        res.delete("1.0","end-1c")
        res.insert(END,r) 
    except ZeroDivisionError:
        res.delete("1.0","end-1c")
        res.config(bg="red")  
        res.insert(END,"zero devision")
    except:
        res.delete("1.0","end-1c")
        res.config(bg="red")  
        res.insert(END,"invalid devision enter correct nums")   
e1 = Entry(root,textvariable=number1,font="italic 14 bold",width=25,highlightbackground="light yellow")
e1.grid(row=0,column=1)
e2 = Entry(root,textvariable=number2,font="italic 14 bold",width=25,highlightbackground="light yellow")
e2.grid(row=1,column=1)
Button(root,text="Devide",command=devide,width=10,borderwidth=3).grid(row=2,column=1)
res = Text(root,bg="light green",width=30,height=1,font="italic 14 bold",borderwidth=3,relief=SUNKEN,)
res.grid(row=3,column=1)
root.mainloop()