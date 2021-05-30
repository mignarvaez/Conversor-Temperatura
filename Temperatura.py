from tkinter import Tk, Label, Entry, Button, CENTER
from PIL import Image, ImageTk

ventana = Tk()
ventana.title("Conversor Temperatura")
ventana.resizable(False,False)
ventana.config(bg="#1F1B1C")

def fahrenheit_to_celsius():
    fahrenheit = ent1.get()
    celsius = (5/9) * (float(fahrenheit)-32)
    lbl_result["text"] = f"{round(celsius,2)} °C"

def celsius_to_fahrenheit():
    celsius = ent2.get()
    fahrenheit = ((9/5)*float(celsius))+32
    lbl2_result["text"] = f"{round(fahrenheit,2)}°F"

titulo_label = Label(ventana,text="CONVERSOR DE TEMPERATURA",anchor=CENTER, fg="white",bg="#1F1B1C")
titulo_label.config(font=("Lucida Console",15))
titulo_label.grid(row=0,column=0,columnspan=4,pady=5)

img = Image.open("Termometro.png")
img = img.resize((200,200))
img = ImageTk.PhotoImage(img)
img_lbl = Label(ventana, image=img, bg="#1F1B1C")
img_lbl.image = img
img_lbl.grid(row=1, column=0, columnspan=4,padx=5, pady=5)


ent1= Entry(ventana, width=10)
lbl1_temp = Label(ventana, text="°F")

ent2= Entry(ventana, width=10)
lbl2_temp = Label(ventana, text="°C")

ent1.grid(row=2, column=0, sticky="e", padx=5,pady=10)
lbl1_temp.grid(row=2, column=1, sticky="w")

ent2.grid(row=3, column=0, sticky="e", padx=5,pady=10)
lbl2_temp.grid(row=3, column=1, sticky="w")

btn1 = Button(ventana, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)
lbl_result = Label(ventana, text="°C")

btn2 = Button(ventana, text="\N{RIGHTWARDS BLACK ARROW}", command=celsius_to_fahrenheit)
lbl2_result = Label(ventana, text="°F")

btn1.grid(row=2, column=2, padx=10)
lbl_result.grid(row=2, column=3, padx=10)

btn2.grid(row=3, column=2, padx=10)
lbl2_result.grid(row=3, column=3, padx=10)

ventana.mainloop()
