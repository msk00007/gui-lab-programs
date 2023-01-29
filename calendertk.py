from tkinter import *
from datetime import date,datetime
root = Tk()
root.geometry("800x620")
root.minsize(800,620)
titleframe = Frame(root,bg="sky blue",width=640)
titleframe.pack(fill=BOTH)
Label(titleframe,text="Enter year : ",font=("Times","16","bold"),bg="sky blue",width=10,height=3).pack(side=LEFT)
y = StringVar()
year = Entry(titleframe,textvariable=y,font=("Times","16","italic"))
year.pack(side=LEFT)
def getcal():
    for i in range(10):
        for j in range(12):
            mycal[i][j].config(text=" ")
    mycal
    weekdays = {6:"Sun",0:"Mon",1:"Tue",2:"Wed",3:"Thu",4:"Fri",5:"Sat"}
    months = {1:"JAN",2:"FEB",3:"MAR",4:"APR",5:"MAY",6:"JUN",7:"JUL",8:"AUG",9:"SEP",10:"OCT",11:"NOV",12:"DEC"}
    myyear = int(y.get())
    start = date(myyear,1,1)
    val = start.weekday()
    num = 0
    for i in range(10):
        for j in range(12):
            if i<3 and j<5:
                mycal[i][j].config(relief=FLAT)
            if i==1 and j == 2:
                mycal[i][j].config(text=y.get())
            elif i>2 and j>4:
                if i==3 and j==5: 
                    mycal[i][j].config(text=weekdays.get(val))                
                elif i>3 and j ==5:
                    val = (val+1)%7
                    mycal[i][j].config(text=weekdays.get(val))  
                else:
                    mycal[i][j].config(text=weekdays.get((val+(j-5))%7))
            elif i>2 and j<=4:
                if j == 0:
                    num+=1
                    if num <10:            
                        mycal[i][j].config(text=str(num),fg="violet")  
                else:
                    if num+7*j<32:
                        if num+7*j<29:
                            mycal[i][j].config(text=str(num+7*j),fg="violet")
                        if num+7*j>28 and  num+7*j<31:
                            mycal[i][j].config(text=str(num+7*j),fg="light green") 
                        if num+7*j == 31:
                            mycal[i][j].config(text=str(num+7*j),fg="red")  
    for n in range(1,13,1):
        d = date(myyear,n,1).weekday()
        monthstartday = weekdays.get(d)
        for j in range(5,12):
            if mycal[3][j].cget("text")==monthstartday:
                k=0
                while mycal[k][j].cget("text")!=" ":
                    k+=1
                mycal[k][j].config(text = months.get(n))
                if j<8:
                    mycal[k][j].config(fg="red")
                if j==8 and k == 0:
                    mycal[k][j].config(fg="violet")
                elif  j==8 and k == 1:
                    mycal[k][j].config(fg="red")
                elif j == 8 and k == 2:
                    mycal[k][j].config(fg="light green")
                elif j>8 and k == 0:
                    mycal[k][j].config(fg="light green")
                else:
                    mycal[k][j].config(fg="red")



Button(titleframe,text="click me",font=("Times","10","bold"),command=getcal,relief=RAISED).pack(side=LEFT)
pagecalendar = Frame(root,bg="sky blue")
pagecalendar.pack(fill=X)
Label(pagecalendar,text="1 Page Calendar",font=("Times","18","bold"),width=57,height=2,relief=SOLID,borderwidth=2).pack(side=LEFT)
gridtable = Frame(root,bg="sky blue")
gridtable.pack(side=TOP,fill=BOTH)
mycal = [["" for x in range(12)] for x in range(10)]
for i in range(10):
    for j in range(12):
        labelname = Label(gridtable,text=" ",font=("Times","11","bold"),width=7,height=2,relief=SOLID,borderwidth=1)
        labelname.grid(row=i,column=j)
        mycal[i][j]=labelname
finalframe = Frame(root,bg="sky blue",width=100,height=180)
finalframe.pack(fill=BOTH)
root.mainloop()
