"""
Calcule o resultado do código manualmente.
"""
def calc_digit(n):
    def final(digit):
        return digit**n
    return final

num_list = []
for num in range(1, 6):
    num_list.append(calc_digit(num))
    print(num_list[num - 1](num))
"""
Minha resposta:

Primeiramente precisamos entender que o código se trata de potenciação ao mesmo número que for passado na função,  apenas observando pela função final.

Em calc_digit(n) é esperado o argumento n -> número, temos uma função implementada dentro dela, final(digit) que vai retornar digit potenciado ao n e depois retornamos a função para ser executada ao chamar calc_digit.

Após isso foi feita uma lista pra poder colocar o resultados da potencia ao quadrado, de 1 até 5 (não 6 pq começa em 0) então a saída (output) e calculo seria:

1^1 = 1
2^2 = 2 * 2 = 4
3^3 = 3 * 3 * 3 = 27
4^4 = 4 * 4 * 4 * 4 = 256
5^5 = 5 * 5 * 5 * 5 * 5 = 3125
"""