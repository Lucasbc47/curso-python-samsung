"""
Entre os números naturais positivos diferentes de 1, um número que não é 
primo é chamado de número composto. 
Imprima os números primos e compostos de 2 a 12.

Uma expressão deve determinar se o número é primo ou composto, 
caso seja composto, deve ser impresso na tela.
"""
def primo(numero):

    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
        
    return True

if __name__ == "__main__": 
    for numero in range(2, 13):
        if primo(numero):
            print(f"Primo: {numero}")
        else:
            print(f"Composto: {numero}")