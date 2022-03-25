#Importar la librería firmata, para enviar y recibir datos de Arduino.
#Importar la librería time, para almacenar los valores de tiempo.
import pyfirmata
import time
if __name__ == '__main__':

    # Inicializando comunicación con arduino
    board = pyfirmata.Arduino('COM3')
    print("Conectado con Arduino")
    
    # Crear variables del boton y los led
    button = board.digital[4]
    LED_AMARILLO = board.digital[12]
    LED_VERDE = board.digital[8]
   
    LEDs = [LED_AMARILLO, LED_VERDE]
    LED_index = 0
    previous_button_state = 0
    
    # Iniciar iterador para recibir datos de entrada
    it = pyfirmata.util.Iterator(board)
    it.start()
    counter = 0
    last_status = False
    
    # Configuración del PushBotton.
    button.mode = pyfirmata.INPUT
    
    def __init__(self, write, board):
        self.write = write
        self.board = board
    
        
    for LED in LEDs:
        LED.write(0)
    
    while True:

        # Velocidad con la que inicia el ciclo.
        time.sleep(0.1)
            
        # Obtención del estado actual del botón.
        button_state = button.read()       
             
        # Configuración del botón cuando se ha pulsado y cuando se ha soltado.
        if button_state != previous_button_state:
            if button_state is True:
                if button_state != last_status:
                    counter += 1
                    if counter == 2:
                        print("LED ENCENDIDO")
                        LEDs[LED_index].write(1)
                        time.sleep(5)
                        print("LED APAGADO")
                        LEDs[LED_index].write(0)
                        counter = 0
                        LED_index += 1
                        if LED_index > len(LEDs):
                            LED_index = 0
                
            
        # Guardar el estado actual del botón como anterior para la siguente repetición.
        previous_button_state = button_state 