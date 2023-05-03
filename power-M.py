# power.off
A text script to shut down Windows
#fuck_you_editor
from tkinter import*
import os
w=Tk()
w.title("shout down,restart")
w.geometry("400x250")
w.configure(background="green")
def shutdown():
    os.system("shutdown /s /t 1")
def restart():
    os.system("shutdown /r /t 1")
btn=Button(w,text="download auth",font="arial 12 bold",background="blue",fg="yellow",command=shutdown)
btn.place(x=10,y=80)
btn1=Button(w,text="auth",font="arial 12 bold",background="red",fg="yellow",command=restart)
btn1.place(x=320,y=80)
btn=Button(w,text="click",font="ariald 12 bold",background="black",fg="orange")
w.mainloop()
#good bye
