"""
Há uma pontuação tupla como se segue.
Esta tupla contém informações sobre quatro alunos. 
Nesta informação, o nome do aluno e as notas em inglês, matemática e ciências formam um tuple. 
Por exemplo, 'Davi' tem uma nota de 88 em inglês, 95 em matemática e 90 em ciências.

notas = (('Davi',  88,  95, 90), ('Felipe', 83, 98, 81), ('Luciano', 81, 97, 98), ('Rodrigo', 82, 89, 83))
Extrair somente as notas matemáticas, usando a função zip na tupla da nota. 
Escreva um código que calcula a média das pontuações de matemáticas extraídas.
"""
## Inglês | Matemática | CIências
notas = (
    ('Davi',  88,  95, 90), 
    ('Felipe', 83, 98, 81), 
    ('Luciano', 81, 97, 98), 
    ('Rodrigo', 82, 89, 83)
)
## notas: [1], [2], 3
notas_de_matematica = [nota[1] for nota in notas]
media_de_matematica = sum(notas_de_matematica) / len(notas_de_matematica)
print(f"A média das notas de matemática é {round(media_de_matematica)}")
