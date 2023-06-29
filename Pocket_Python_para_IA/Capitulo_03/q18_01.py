"""
Um palíndromo é uma frase ou palavra que se lê da mesma forma da esquerda pra direita e vice-e-versa. 
Por exemplo: radar.
Escreva um programa que usa uma função recursiva para determinar se uma string é um palíndromo ou não.
"""
def palindromo(palavra: str): 
    def inverter(palavra: str):
        return palavra[::-1]
    return inverter(palavra) == palavra
    
palavra = "radar"
print(palavra, "é um palíndromo" if palindromo(palavra) else "não é um palíndromo")