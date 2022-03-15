numbers = [1,2,3,4,5]
#          0,1,2,3,4

#print (numbers[4])

#los arreglos tienen diferente nombres dependiendo el lenguaje de progracion, en Python se llama [Listas],
#Una lista tienen que ir separador por , y el conjunto entre corchetes, es mutable, por podemos suprimir y agregar nuevos datos.


colores = ["Verde", "Morado", "Amarillo"]

#print (colores[1])

#los arreglos asociativos o tambien conocidos como diccionario en Python, estos nos permiten almacenar cualquier tipo de valor,
#enteros, cadenas, listas, y otras funciones, ademas estos "diccionario", nos permite identificar los elementos por una clave.
#La diferencia es que vamos a hacer uso de una clave y de una valor. "Para los diccionarios se usan las LLAVES {}".

colors = ["Verde", "Morado","Amarillo"]
person = {"name":"Marines", "lastName":"Mendez", "age":24}

#print (person.get("age"))

#si queres obtener todos los datos de una lista o diccionario, tene que poner la posicion o la clave como en el ej anterios
#para evitar que esto se haga tedioso, tenemos el CICLO FOR, con esto evitamos repetir el mismo codigo varias veces.


#colors = ["Verde", "Morado","Amarillo"]
#person = {"name":"Marines", "lastName":"Mendez", "age":24}

#for value in colors:
    #print(value)

#for key, value in person.items():
    #print(key," ",value)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#una lista es mutable, pero no solo con las lista se puede hacer esto si no que tambien con los diccionario.
#Estos son algunos de esos metodos que nos ayudan a hacer estas acciones.

colors = ["Verde", "Morado","Amarillo","Verde"]
numbers = [1,2,3,4,5]
person = {"name":"Marines", "lastName":"Mendez", "age":24}
animal = {"name":"oso", "color":"blanco", "age":6}
colors[0]="Azul"

numbers.extend(colors)

print(len(colors))
print(len(person))

for value in colors:
    print(value)

for key, value in person.items():
    print(key," ",value)

