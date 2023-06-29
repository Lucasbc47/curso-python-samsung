"""
Escreva duas strings, s1 e s2, com o conteúdo 
"Eu amo", "Eu gosto de" e "Panqueca", "Suco de laranja", "Café" respectivamente. 
O programa deve ter o seguinte resultado:

Eu amo Panqueca.
Eu amo Suco de laranja.
Eu amo Café.
Eu gosto de Panqueca.
Eu gosto de Suco de laranja.
Eu gosto de Café.
"""
s1 = "Eu amo"
s2 = "Eu gosto de"
lista = ["Panqueca.", "Suco de laranja.", "Café."]

for item in lista:
    print(f"{s1} {item}")

for item in lista:
    print(f"{s2} {item}")