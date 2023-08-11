"""
O problema do preço das casas em Boston é um problema de prever o preço das casas de cada bairro de Boston, 
EUA, usando características como a taxa de criminalidade e a poluição do ar na área. 
Ele pode ser importado do pacote scikit-learn.

Encontre o vetor de peso x quando o problema do preço das casas em Boston for resolvido com o modelo de previsão linear.
Os dados matriciais e vetoriais podem ser obtidos da seguinte forma. 

Aqui, para simplificar o problema, limitamos os dados de entrada à 
    - taxa de criminalidade (CRIM), 
    - qualidade do ar (NOX), 
    - número de quartos (RM),
    - idade (AGE), e apenas estes quatro dados foram utilizados.

Execute o código abaixo para verificar se a magnitude ou o sinal do vetor de peso obtido com a execução do programa 
é consistente com a noção comum. 
Para encontrá-la, interprete a saída impressa para todos os fatores: CRIM, NOX, RM e AGE.

from sklearn.datasets import load_boston
boston = load_boston()
X = boston.data
y = boston.target
A = X[:4, [0, 4, 5, 6]]  # ‘CRIM’, ’NOX’, ’RM’, ’AGE’
b = y[:4]

Escreva sua resposta abaixo com suas interpretações dos resultados, como por exemplo 
"O preço das casas é inversamente proporcional à taxa de criminalidade (CRIM)"'
"""

# pip install scikit-learn==0.24.2 
# -> load_boston não está disponiveis nas mais recentes

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston = load_boston()
X = boston.data
y = boston.target
A = X[:4, [0, 4, 5, 6]]  # 'CRIM', 'NOX', 'RM', 'AGE'
b = y[:4]

model = LinearRegression()
model.fit(A, b)

print(f"""
- CRIM: {round(model.coef_[0], 2)}
- QUALIDADE DO AR:: {round(model.coef_[1], 2)}
- NUMERO DE QUARTOS: {round(model.coef_[2], 2)}
- IDADE DAS CASAS: {round(model.coef_[3], 2)}
""")
"""
Q5:

- CRIM: 4.67428537
- QUALIDADE DO AR: -14.88095928 
- NUMERO DE QUARTOS: 15.10925633
- IDADE DAS CASAS:  -0.08745065

[!] Taxa de criminalidade (CRIM):
Se o preço das casas aumentam a taxa de criminalidade também aumenta.

[!] Qualidade do ar (NOX): 
Se levarmos em conta preços das casa conseguimos ter uma melhor qualidade do AR.
Isso se deve estrutura da casa provavelmente e como a mesma contribui ao ecossistema.

[!] Número de quartos (RM): 
O aumento do preço das casas explica o número de quartos da casa.

[!] Idade das Casas (AGE): 
As casas são mais atrativas pelo seu preço, isso explica a longevidade das mesmas.
"""