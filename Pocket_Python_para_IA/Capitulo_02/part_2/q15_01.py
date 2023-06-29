"""
Declarar um dicionário school, como a seguir:
school = { 'kim': {'age': 16, 'hei': 170, 'grade': 3}, 'lee': {'age': 15, 'hei': 168, 'grade': 2}, 'choi': {'age': 14, 'hei': 173, 'grade': 1}}
Em seguida, use a função deepcopy() do módulo de copy para escrever um programa que 'copie' para outra variável, school2.
(Verifique se school e school2 são variáveis diferentes através do operador is).
Dica: Imprimir para que o resultado da school seja school2 é falso.
"""
from copy import deepcopy

school = {
    'kim': {
        'age': 16, 
        'hei': 170, 
        'grade': 3
    },
    'lee': {
        'age': 15, 
        'hei': 168, 
        'grade': 2
    }, 
    'choi': {
        'age': 14, 
        'hei': 173, 
        'grade': 1
    }
}

school2 = deepcopy(school)
print(school is school2)
# False
