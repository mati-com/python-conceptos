def plusNumbers(list):
    even = 0
    odd = 0
    plus = 0
    for value in list:
        if value % 2 ==0:
            even = even + value
        else:
            odd = odd + value
    
    print ("Suma de numeros pares ",even)
    print ("Suma de numeros impares ",odd)

plusNumbers([1,2,3,4,5,6,7,8,9])