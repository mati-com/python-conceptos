def validar(message):
    #while se ejecutara varias veces finalizara cuadno se ejecute return
    while True: 
        try: 
            #En esa linea pedimos un valor de tipo flotante 
            data = float(input("Coloca " + message))
            #Si el valor es de tipo flotante regresamos el valor
            return data
        except ValueError:
            #Se imprime el mensaje cuadno surge un error en el try
            print("Ingresa un número decimal o entero")

#Datos de entrada
largo= validar("Colocar largo en metros: ")
ancho= validar("Colocar ancho en metros: ")
m2xcaja= validar("Colocar los metros cuadrados de la caja: ")
precioXm2= validar("Coloca el precio del metro cuadrado: ")
"""Reglas de tres
1m2=162$
1.5m2=?
"""
precioXcaja= (m2xcaja * precioXm2)
#Obtenemos el m2 que tiene el cuarto
m2Cuarto= largo * ancho
#Cuantas baldosas entrar en el cuarto
cajas= m2Cuarto/m2xcaja
#Obtiene el precio total 
precioTotal= cajas + precioXcaja

print("Total de cajas que se necesitan es: ", cajas)
print("Precio total: ", precioTotal)