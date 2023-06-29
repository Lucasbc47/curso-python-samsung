"""
Usando os operadores lógicos "and", "or" e "not" 
escreva um programa que, dado x = 1 e y = 0, 
imprima os seguintes resultados: 
0
1
False
True 
"""
x = 1 
y = 0
print(int(x not in list(range(0,10))))
print(int(x not in list(range(20,30))))
print(x > 20 and x > 300)
print(x > 10 or x < 10)
