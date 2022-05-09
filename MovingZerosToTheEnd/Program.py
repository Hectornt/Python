def move_zeros(array):
# Resuelto con comprension de listas
    NuevoArreglo = [n for n in array if n > 0]
    while NuevoArreglo.count(0)<array.count(0):
        NuevoArreglo.append(0)
    return NuevoArreglo
# Primer intento
"""    for n in array:
        if n > 0:
            NuevoArreglo.append(n)
    print(NuevoArreglo)
    while NuevoArreglo.count(0)<array.count(0):
        NuevoArreglo.append(0)
    return NuevoArreglo"""
 

arreglo = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
print(move_zeros(arreglo))