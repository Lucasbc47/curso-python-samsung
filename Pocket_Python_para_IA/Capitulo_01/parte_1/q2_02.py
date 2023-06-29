"""
Escreva um programa que recebe um número inteiro positivo do usuário e diz se é um número par ou ímpar. Use o pseudo-código para se guiar:
print 'Digite um número inteiro positivo:'
n = input()
se resto da divisão por 2 é igual a 0:
    print 'n é par'
se não:
    print 'n é ímpar'
"""
n = int(input("Digite um número:\n"))
print(f"{n} é par" if n % 2 == 0 else f"{n} é ímpar")




