"""
Escreva um programa que recebe dois pontos no plano cartesiano,
(x1, y1) e (x2, y2) e imprime a distância entre esses 2 pontos.
"""
def distancia_pontos(x1, x2, y1, y2):
    # dAB = √(xb - xa)² + (yb - ya)² 
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

x1, y1, x2, y2 = map(int, input("Digite valores de: (x1, y1, x2, y2) separados por ',': ").split(','))
print(distancia_pontos(x1, x2, y1, y2))