"""
Escreva um programa que usa a função map() para realizar operações de multiplicação com os itens 
da lista n_list = [10, 20, 30]. O programa deve imprimir 2x e 3x os valores de n_list.
"""
n_list = [10, 20, 30]

def multiplicar(x, y):
    return x * y

print(f"2x: {list(map(lambda n: multiplicar(n, 2), n_list))}\n"
    f"3x: {list(map(lambda n: multiplicar(n, 3), n_list))}",
)