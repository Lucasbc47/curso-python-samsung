"""
Crie exemplos de:
- vetor zerado
- vetor com uns
- matriz quadrada 
- matriz diagonal
- matriz identidade 
- matriz simétrica um por um 
representando os vetores e matrizes com NumPy.

https://github.com/Lucasbc47/curso-python-samsung
"""

import numpy as np

matriz_zerada = np.zeros(4)
matriz_um = np.ones(5)
matriz_diagonal = np.diag([1, 2, 3, 4])
matriz_identidade = np.eye(4)
matriz_quadrada = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
matriz_simetrica = np.array([
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
])
matrizes = [
    f"Zerada:\n{matriz_zerada}",
    f"Com 1:\n{matriz_um}",
    f"Diagonal:\n{matriz_diagonal}",
    f"Identidade:\n{matriz_identidade}",
    f"Quadrada:\n{matriz_quadrada}",
    f"Simetrica:\n{matriz_simetrica}"
]
for x in matrizes:
    print(x)
