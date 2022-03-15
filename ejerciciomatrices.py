#Una matriz es una tabla que tienes filas que son las listas, y columnas que son los valores que tiene cada una de las listas.

matris1 = [[1,2,3],[7,8,9],[13,14,15]]
matris2 = [[4,5,6],[10,11,12],[16,17,18]]

matris3 = [[1,2,3],[7,8,9],[13,14,15]]

for rowPosition, value in enumerate(matris1):

    for columPosition, value2 in enumerate(value):

        matris3[rowPosition][columPosition] = matris1[rowPosition][columPosition] + matris2[rowPosition][columPosition]

print(matris3)


