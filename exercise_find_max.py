# Ejercicio 5: Encontrar el máximo en una lista

def find_max(lista):
    """
    Encuentra y retorna el valor máximo en una lista de números.
    Si la lista está vacía, retorna None.

    Args:
        lista: Una lista de números

    Returns:
        El valor máximo de la lista o None si está vacía
    """
   
    if not lista:
        return None
    return max(lista)
   
print(find_max([3, 7, 2, 9, 1]))   # 9
print(find_max([-5, -2, -8, -1]))  # -1
print(find_max([]))                # None