# Ejercicio 12: Manipular lista de listas

def list_of_lists(lista):
    primera = lista[0][:2]      
    segunda = lista[1][1:4]     
    tercera = lista[2][-2:]     

    return [primera, segunda, tercera]
print(list_of_lists([[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]))

print(list_of_lists([[], [4, 5, 6], [10, 11, 12]]))

print(list_of_lists([[1, 2], [], [12]]))
