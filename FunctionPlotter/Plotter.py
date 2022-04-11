from dataclasses import replace
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from PIL import ImageTk,Image
import os
import sys

def input_refine(func):
        x = func.replace("cos","np.cos").replace("sin","np.sin").replace("tan",
                        "np.tan").replace("^","**").replace("sqrt","np.sqrt").replace("ln","np.log10").replace("e","np.exp")
        #print(x)
        return x
# a function that will be called by our button from gui to plot graphs with given data
def graph():
    plt.clf()
    try:
        func = str(entry_func.get()).lower()
        mi = int(entry_min.get())
        ma = int(entry_max.get())
    except:
        messagebox.showinfo("error message","please enter right values in textbox")
        os.execl(sys.executable, sys.executable, *sys.argv) # restart the program

    x = np.linspace(mi,ma,num=1001) # x limits
    # see if the user enterd int only then we will plot function y = number
    try:
        if(isinstance(int(func),int)):
            ylist = np.linspace(int(func),int(func),num=1001)
            print("aloo")
    except:
            try:
                f = input_refine(func)
                ylist = eval(f)
            except NameError:
                messagebox.showinfo("error message","Something Wrong please enter function in x")
            except SyntaxError:
                messagebox.showinfo("error message","something Wrong please enter function using + - / * ^ cos() sin() tan() abs(")
            except ValueError:
                messagebox.showinfo("error message","Something Wrong please enter function in x")
            except:
                messagebox.showinfo("error message","Something went Wrong make sure of your inputs")

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    #plt.figure(num=0,dpi=120)
    plt.ylabel('some numbers')
    plt.plot(x,ylist,linewidth=2.5)
    plt.show()

# The Gui Part I used Tkinter
root = Tk()
root.title('Function plotter')
root.geometry("400x200")

L_func = Label(text = "Enter the function in x:", font=('Arial',14),fg='black')
L_func.grid(row=0,column=0,padx=0,pady=10)

L_min = Label(text = "Enter the Minmum Limit:", font=('Arial',14),fg='black')
L_min.grid(row=1,column=0,padx=0,pady=10)

L_max = Label(text = "Enter the Maximum Limit:", font=('Arial',14),fg='black')
L_max.grid(row=2,column=0,padx=5,pady=10)

entry_func = Entry(root,width=20)
entry_func.grid(row=0,column=2)
entry_max = Entry(root,width=20)
entry_max.grid(row=1,column=2)
entry_min = Entry(root,width=20)
entry_min.grid(row=2,column=2)

my_button = Button(root,text = "plot Graph", command=graph)
my_button.grid(row=3,column=2)

root.mainloop()