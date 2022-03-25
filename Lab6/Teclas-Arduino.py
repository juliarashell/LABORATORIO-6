from tkinter import Button
import pyfirmata
import time

# Conectar con Arduino.
board = pyfirmata.Arduino('COM3')
print("Conectado con Arduino")

# Crear variables de boton y leds.
button = board.digital[2]
LedA = board.digital[12]
LedV = board.digital[8]

Led_encendido = 0
button_enc = 0

# Inicilizar el Iterador
it = pyfirmata.util.Iterator(board)
it.start()

# Definir variables intermitentes por tiempo indefinido.
def Inter():
    encender = input("Ingresar teclas AY para encender LEDS: ").upper()
    if encender == 'AY':
        while True:
            LedA.write(1)
            LedV.write(1)
            time.sleep(.5)
            LedA.write(0)
            LedV.write(0)
            time.sleep(.5)
            print("Encendidos")

#Si en caso ingresan teclas incorrectas mostrar el siguiente mensaje:
    else:
        print("Teclas incorrectas\n")

#Repetir ciclo
while True:
    Inter()
