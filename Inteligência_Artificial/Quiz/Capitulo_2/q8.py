"""
Encontre os valores próprios da seguinte matriz usando a equação característica.

D = [2 1 1 2]
imagem: [https://sicbrasil.org.br/asset-v1:LSI-TEC+SIC202+2023_T1+type@asset+block@2023-07-29-120531.png]

"""
# Assunto de Álgebra linear. numpy resolve tranquilamente.
# recomendo ver: https://www.youtube.com/watch?v=PFDu9oVAE-g&ab_channel=3Blue1Brown
# "Autovetores e autovalores"

import numpy as np

D = np.array([
    [2, 1],
    [1, 2]
])
print("R:", [f"λ = {λ}" for λ in np.linalg.eigvals(D)])