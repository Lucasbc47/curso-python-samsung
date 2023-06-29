"""
A matriz bidimensional a contém os valores [[1, 2], [3, 4], [5, 6]]. 
Mude esta matriz bidimensional para uma matriz unidimensional como 
[1, 2, 3, 4, 5, 6], e imprima-a.
Dica: Use um for loop. 
Defina uma nova matriz e coloque os elementos de uma nessa matriz.
"""
matriz_bidimensional = [[1, 2], [3, 4], [5, 6]]
matriz_unidimensional = []

for x, y in matriz_bidimensional:
    matriz_unidimensional.append(x)
    matriz_unidimensional.append(y)