import tkinter as tk
from tkinter import Label, Text, messagebox
from tkinter import *
from tkinter import font
from tkinter.ttk import *

wBill = tk.Tk()
wBill.geometry("400x375")
wBill.configure(bg = 'yellow')

#background image used
bg = PhotoImage(file = r"C:\Users\Dennis\Desktop\ACP_FINAL\acp.png")
  
# Show image using label
label1 = Label( wBill, image = bg)
label1.place(x = 0, y = 0)

wBill.iconphoto(False, tk.PhotoImage(file=r'C:\Users\Dennis\Desktop\ACP_FINAL\calcu.png'))

def Calculate():
    global presRead, presInput, prevRead, presLbl, prevLbl, prevInput, prevInt, presInt, initRead, finalRead, lessRead, bill1, bill2, finalBill

    prevInput = prevRead.get("1.0", "end")
    presInput = presRead.get("1.0", "end")
    prevInt = float(prevInput)
    presInt = float(presInput)
    initRead = presInt - prevInt
    finalRead = initRead / 2
    lessRead = finalRead - 200
    bill1 = lessRead * 0.35
    bill2 = 90
    finalBill = bill1 + bill2

    messagebox.showinfo("Bill", f"Initial Read: {initRead}\nFinal Reading: {finalRead}\nFirst 200kL: {bill1}\nOther Bills: {bill2}\nWater Bill Amount: {finalBill}")

def Try():
    global presRead, presInput, prevRead, prevInput, prevInt, presInt, initRead, finalRead, lessRead, bill1, bill2, finalBill

    prevRead.delete("1.0", "end")
    presRead.delete("1.0", "end")
    prevInput = None
    presInput = None
    prevInt = None
    presInt = None
    initRead = None
    finalRead = None
    lessRead = None
    bill1 = None
    bill2 = None
    finalBill = None

presRead = Text(height=1, width=14, font = ('Century Gothic', 16))
presRead.place(x=210, y=168)

prevRead = Text(height=1, width=14, font = ('Century Gothic', 16))
prevRead.place(x=210, y=210)

calBtn = tk.Button(text="Calculate", height=1, width=20, command=Calculate, font = ('Century Gothic', 16))
calBtn.place(x=60, y=270)

tryBtn = tk.Button(text="Try Again", height=1, width=20, command=Try, font = ('Century Gothic', 16))
tryBtn.place(x=60, y=320)

wBill.resizable(False, False)

wBill.mainloop()