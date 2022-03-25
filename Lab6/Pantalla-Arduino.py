# Librería tkinter para crear el botón en pantalla.
from tkinter import *
#Estilo de letra
import tkinter as tk
import serial, time

arduino = serial.Serial("COM3", 9600)
time.sleep(0.01)

# Crear instancia de tkinter frame.
win= Tk()

# Definir tamaño de la ventana.
win.geometry("300x150")

# Funciones a utilizar.
def encenderled(e):
   print("DOBLE CLIC, LED ENCENDIDO")
   arduino.write(b'1')
   time.sleep(10)
   print("LED APAGADO")

def close_window ():
    win.destroy()

# Crear botones
tk.Button(win, text= "ENCENDER LED", command=lambda:encenderled).pack(pady=20)
tk.Button(win, text= "SALIR", command=close_window).pack(pady=20)

# Enlazar el doble clic con el controlador.
win.bind('<Double-Button-1>', encenderled)

# Cambiar color de la ventana
win['bg'] = 'yellow'
win.mainloop()