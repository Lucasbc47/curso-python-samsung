"""
Escreva um programa que faz multiplicação (*) e divisão (/) 
usando os métodos __mul__ e __truediv__ aprendidos na unidade 21.

Assumindo que v1 = (30, 40) e v2 = (10, 20), 
codifique (escreva a declaração de saída) 
para retornar a saída abaixo como resultado
da multiplicação e divisão de dois vetores.

v1 * v2 = (300, 800)
v1 / v2 = (3.0, 2.0)
"""
class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, z):
        return Vetor(self.x * z.x, self.y * z.y)
    
    def __truediv__(self, z):
        return Vetor(self.x / z.x, self.y / z.y)

vet_1 = Vetor(30, 40)
vet_2 = Vetor(10, 20)

print(
    f"v1 * v2 = ({(vet_1 * vet_2).x}, {(vet_1 * vet_2).y})\n"
    f"v1 / v2 = ({(vet_1 / vet_2).x}, {(vet_1 / vet_2).y})",
)