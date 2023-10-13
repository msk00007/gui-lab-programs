from tkinter import*
var=Tk()
var.geometry("320x390")
var.minsize(320,390)
Label(var,text="factorial",bg="black",fg="white",font= ("conicasansms",14,"bold"),borderwidth=10,relief= SUNKEN).pack(side = TOP,fill=X)
def fact():
    ft = int(t.get("1.0","end-1c"))
    if ft == 0 or ft == 1:
        t1.delete("1.0", "end-1c")
        t1.insert(END, "1")
    else:
        result = 1
        for i in range(1,ft+1):
            result = result*i
        t1.delete("1.0", "end-1c")
        t1.insert(END,result)
t = Text(var,bg="light green",font="Courior 14 bold",width=15,height=4.4,borderwidth=5,relief=SUNKEN)
t.pack(side = TOP,fill=X)
Button(var,text = "Compute",bg="blue",fg="white",width=14,height=5,command=fact,borderwidth=3,relief=SUNKEN).pack(side=TOP)
Label(var,text="Result",bg="black",fg="white",font= ("conicasansms",14,"bold"),borderwidth=10,relief= SUNKEN).pack(side = TOP,fill=X)
t1 = Text(var,bg="light green",font="Courior 14 bold",width=15,height=4.5,borderwidth=5,relief=SUNKEN)
t1.pack(side = TOP,fill=X)
var.mainloop()
# adding comment
#adding it from git hub
