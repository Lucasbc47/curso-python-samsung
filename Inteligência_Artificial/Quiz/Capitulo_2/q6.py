"""
(Esta pergunta está relacionada à pergunta Q5).

Encontrar o vetor de peso w quando o problema do preço das casas em Boston for resolvido com o modelo de previsão linear    pelo método dos mínimos quadrados. Os dados matriciais e vetoriais podem ser obtidos da seguinte forma.

from sklearn.datasets import load_boston
boston=load_boston()
X=boston.data
y=boston.target

O significado de cada coluna da matriz X é o seguinte.
-  CRIM: taxa de criminalidade
-  INDUS: Relação da área comercial não comercial
-  NOX: Concentração de óxido nítrico
-  RM: Número de quartos por casa
-  LSTAT: Proporção da classe inferior da população
-  B: Proporção de pessoas negras na população
-  PTRATIO: Razão Estudante/Professor
-  ZN: Porcentagem de áreas residenciais que excedem 25.000 metros quadrados
-  CHAS: 1 se localizado na fronteira com o Rio Charles, 0 caso contrário
-  AGE: Porcentagem de casas construídas antes de 1940
-  RAD: Distância até a rodovia radial
-  DIS: Distância média ponderada para 5 Centros de Emprego em Boston
-  TAX: Taxa de imposto predial

1) Execute o código acima para verificar se a magnitude ou sinal do vetor de peso obtido com a execução do programa é consistente com a noção comum. 
Para encontrá-la, interprete a saída impressa para todos os fatores sugeridos acima (escreva sua resposta abaixo com suas interpretações dos resultados, como por exemplo "O preço das casas é inversamente proporcional à taxa de de criminalidade - CRIM").

2) Explique como o resultado difere do valor obtido na Pergunta Q5.
"""
from sklearn.datasets import load_boston
import numpy as np

boston = load_boston()
X = boston.data
y = boston.target
