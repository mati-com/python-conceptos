#Los arreglos multidimensionales se caracteriza por tener 2 o mas dimesiones, tendremos "arreglos dentro de arreglos"
"""
shoes = [
 ["tenis1","tenis2","tenis3"],
 ["tenis4","tenis4","tenis5"],
 ["tenis6","tenis7","tenis8"]]

print(shoes[1][2])
"""
#ahora vamos a utilizar diccionarios ((CLAVES Y VALOR))
"""
shoes = [
 {"Nike":"tenis1","Coverse":"tenis2","Adidas":"tenis3"},
 {"Nike":"tenis4","Coverse":"tenis5","Adidas":"tenis6"},
 {"Nike":"tenis7","Coverse":"tenis8","Adidas":"tenis9"}]

print(shoes[2]["Adidas"])
"""
#tambien podemos tener un diccionario principal y dentro de este tener varias listas.
"""
shoes = {
    "Nike":["tenis1","tenis2","tenis3"],
    "Adidas":["tenis4","tenis5","tenis6"],
    "Coverse":["tenis7","tenis8","tenis9"]}

print(shoes["Nike"][1])
"""

#Recorrer Arreglos Multidimensionales
#Aqui vamos a a hacer ciclos anidados ((UN "FOR" DENTRO DE OTRO "FOR"))

"""
shoes = {
    "Nike":["tenis1","tenis2","tenis3"],
    "Adidas":["tenis4","tenis5","tenis6"],
    "Coverse":["tenis7","tenis8","tenis9"]}

for key, list in shoes.items():
    for value in list:
     print("Estos son los tenis ", key , value)
"""

#Asi vamos a obtener la posicion de un vector 

numbers = [1,2,3,4,5,6,7]

for posicion, value in enumerate(numbers):
    print("Posición ",posicion," ",value)

#Podemos obtener un valor directamente colocando la lista corchetes ([]), y agregando la posicion,
#Cuando inicie mi FOR va obtener el valor 0 por que es en que iniciamos, me imprime la posicion que es 0
#Y me obtiene el valor que se encuentra en la posicion 0.