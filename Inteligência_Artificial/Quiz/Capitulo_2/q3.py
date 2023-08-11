"""
Quando o seguinte código é executado, todos os dados da imagem numérica MNIST são convertidos em vetores 
para criar uma única matriz X em NumPy. Use esta matriz para resolver o seguinte problema.

from sklearn.datasets import load_digits
X=load_digits().data

1) Encontre a semelhança entre a primeira imagem e a décima imagem usando dot product.
2) Encontre a semelhança para uma combinação de todas as imagens usando o dot product, 
como seria eficiente implementá-lo (dica: usando matrizes e multiplicação de matrizes)
"""

# pip install scikit-learn
from sklearn.datasets import load_digits
import numpy as np

X = load_digits().data

primeira = np.array(X[0])
decima = np.array(X[9])

primeira_norm = primeira / np.linalg.norm(primeira)
decima_norm = decima / np.linalg.norm(decima)

valor = np.dot(primeira_norm, decima_norm)
norm = X / np.linalg.norm(X, axis=1, keepdims=True)
similiaridade = np.dot(norm, norm.T)

print(f"[1] - A semelhanca entre a primeira e a decima e: {valor}")
print(f"[2] - A semelhanca de todas imagens e: {np.mean(similiaridade)}")