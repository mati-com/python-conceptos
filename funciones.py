def saludar (nombre):
    return "Hola {} bienvenido al juego de Maty".format(nombre) #Aqui le pasamos el "nombre"a nuestro primer elemento "{}"

print("Ingresa tu nombre")
nombre = input() #Aqui pedimos al usuario darnos su nombre y lo almacenamos en una variable "nombre", luego imprimimos la funcion "saludar".
print(saludar(nombre))