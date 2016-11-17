"""
ACC Python GUI Demo: Using Tkinter

Python GUI programming using tkinter demo program. This code will run on windows,linux and mac (Needs python to run unless compiled) *You can copy paste codes from here into your appications or use this as reference.
See Guthub page for more info.
"""

# !/usr/bin/python3
from tkinter import *
import tkinter.scrolledtext as ScrolledText

def helloCallBack():
    label['state']="normal"
    label.delete("1.0", "end")
    label.insert(INSERT,str(atbashCipher(E1.get(1.0,END))))
    label['state']="disabled"

# >Atbash Cipher Encoding / Decoding Function
def atbashCipher(atbashInput):
    atbashOutput = ""
    for x in atbashInput:
        temp = x
        #Add support for uppercase charachters
        charIsUpper = False
        if ord(x) >= 65 and ord(x) <=90:
            charIsUpper = True
        if (ord(temp) >=97 and ord(temp) <=122) or charIsUpper == True:
            temp = temp.lower()
            outCharCode = abs(ord(temp)-122) + 97
            if charIsUpper == True:
                atbashOutput = atbashOutput + chr(outCharCode).upper()
            else:
                atbashOutput = atbashOutput + chr(outCharCode)
        else:
            atbashOutput = atbashOutput + x
    return atbashOutput

top = Tk()
top.geometry("300x500")
top.wm_title("Atbash Cipher Encoder/Decoder [ACC 2016 Tkinter Demo]")
E1 = ScrolledText.ScrolledText(top,bd=5,height=13)
label = ScrolledText.ScrolledText(top,state=DISABLED)
inputLabel = Label(top,text="Normal Text: ",anchor="w")
outputLabel = Label(top, text="Ciphered / Deciphered Result: ",anchor="w")
lb1 = Label(top,bd=6)
B = Button(top, text ="Encipher / Decipher", command = helloCallBack)

inputLabel.pack(fill=BOTH)
E1.pack(side = TOP,fill=BOTH)
B.pack(side = TOP,fill=BOTH)
outputLabel.pack(fill=BOTH)
label.pack(fill=BOTH, expand=1)


top.mainloop()
