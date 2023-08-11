"""
As classificações dadas por três usuários a, b, e c, para 4 filmes são expressas com o vetores da seguinte forma.

a = [4, 5, 2, 2]
b = [4, 0, 2, 0]
c = [2, 2, 0, 1]

1) Encontre a distância euclidiana entre a, b, e c. 
Quais são os dois usuários mais próximos? E quais são os dois usuários que estão mais distantes?

2) Encontre a distância do cosseno entre a, b, e c. 
Quais são os dois usuários mais próximos? E quais são os dois usuários que estão mais distantes?
"""
import numpy as np


a = np.array([4, 5, 2, 2])
b = np.array([4, 0, 2, 0])
c = np.array([2, 2, 0, 1])

def euclidean_distance(a, b):
    return np.linalg.norm(a - b)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print(f"""
- Distância euclidiana - 
    dab(a, b): {euclidean_distance(a, b): .4f}
    dac(a, c): {euclidean_distance(a, c): .4f}
    dbc(b, c): {euclidean_distance(b, c): .4f}
""")
print(f"""
- Distância do cosseno) - 
    sim_cos(a, b): {cosine_similarity(a, b): .4f}
    sim_cos(a, c): {cosine_similarity(a, c): .4f}
    sim_cos(b, c): {cosine_similarity(b, c): .4f}
""")

"""
Distância Euclidiana
ab: 5.39 
ac: 4.24 
bc: 3.61 
Usuários mais próximos: bc
Usuários mais distantes: ac

Distância do Cosseno
ab: 0.696 
ac: 0.783 
bc: 0.336
Usuários mais próximos: ac 
Usuários mais distantes: bc 
"""