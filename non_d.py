from asyncio.windows_events import NULL
from calendar import c
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint



#creating main window
window =Tk()
window.title("DE Info")
window.configure (width=500,height=500)
window.configure(bg="lightgray")

#some text
label=Label(text="Equation : dx/dt=ax^2+bx+c",background="lightgray",width=100 ,height=5)
label.pack()

#listener for button
def listener():
    InputWindow()
    

#button that starts the program
b2=Button(window,text="Start",width =10,command=listener);
b2.pack(pady=20)



#creates UI for parameter inputs
def InputWindow():
    label.pack_forget()
    b2.pack_forget()
    lbl=Label(text="Input the parameters of your DE (dx/dt=ax^2+bx+c) : ",background="lightgray",width=100,height=5)
    lbl.pack(pady=10)
    global txt_fieldA
    global txt_fieldB
    global txt_fieldC
    txt_fieldA=Entry(window)
    txt_fieldB=Entry(window)  
    txt_fieldC=Entry(window)
    lblA=Label(text="a = ",background="lightgray")
    lblB=Label(text="b = ",background="lightgray")
    lblC=Label(text="c = ",background="lightgray")
    lblA.pack(pady=5)
    txt_fieldA.pack(pady=5)
    lblB.pack(pady=5)
    txt_fieldB.pack(pady=5)
    lblC.pack(pady=5)
    txt_fieldC.pack(pady=5)
    b1=Button(window,text="OK",width =10,command=DEWindow)
    b1.pack(pady=10)

#window with the results    
def DEWindow():
    global a
    global b
    global c
    a=(txt_fieldA.get())
    b=(txt_fieldB.get())
    c=(txt_fieldC.get())
    A=a+"x^2 + "
    B=b+"x "
    C=" + "+c
    if(a=="0" or a==""): A=""; a=0
    if(b=="0" or b==""): 
        B="" 
        b=0
        if (A!=""):A=a+"x^2 "
        if(A=="" and B==""): C=c
    if(c=="0" or c==""): C="";c=0
    newWindow=Toplevel(window)
    newWindow.title("ODE")
    newWindow.configure (width=500,height=500);
    ode="dx/dt = "+ A+B+C
    lbl2=Label(newWindow ,text=ode,font=("Arial",20)).pack()
    a=float(a)
    b=float(b)
    c=float(c)
    #non-dimentionalization
    if (a==0):
        if (b==0):
            non_d="dX/dT = " + str(c)
            xs="ts"
            ts="xs"
        else:
            if (c!=0):
                non_d="dX/dT = X +" + str(c)
            else:
                non_d="dX/dT = X"
            xs="{:.4f}".format(1/b)
            xs=str(xs)
            ts=xs
    if (b==0 and a!=0):
        if (c!=0):
            non_d="dX/dT = X^2 +" + str(c) +"(ts/xs)"
        else:non_d="dX/dT = X^2 "
        xs="1/("+str(a)+"*ts)"
        ts="1/("+str(a)+"*xs)"
    if (a!=0 and b!=0):
        if(c!=0):
            non_d="dX/dT = X^2 + X +" + str("{:.4f}".format(c*(a/b)))
        else:
            non_d="dX/dT = X^2 + X"
        xs="{:.4f}".format(b/a)
        ts="{:.4f}".format(1/b)
        xs=str(xs)
        ts=str(ts)
    lbl4=Label(newWindow ,text="Non-dimentionalized equation : "+non_d,font=("Arial",15)).pack()
    lbl5=Label(newWindow ,text="Parameters : X=x/xs | T=t/ts",font=("Arial",15)).pack()
    lbl7=Label(newWindow ,text="With  xs= "+ xs +" and ts = "+ts,font=("Arial",15)).pack()






#function returning dy/dx
def model(x,t):
    dxdt=a*x**2+ b*x+ c
    return dxdt
#initial condition
y0=0


#time/distance/ etc. points

x=np.linspace(0,20,100)

#solve ode


window.mainloop();