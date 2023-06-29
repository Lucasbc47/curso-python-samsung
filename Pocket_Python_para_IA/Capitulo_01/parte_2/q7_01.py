"""
Você é maior de idade? (digite 1 se sim, 0 se não): 1
Você é casado(a)? (digite 1 se sim, 0 se não): 0
Você é maior de idade e solteiro.
"""
maior = int(input("Voce e maior de idade? [sim:1|nao:0]:\n"))
casado  = int(input("Voce e casado(a)? [sim:1|nao:0]:\n"))
print(f"Você é {'maior' if maior == 1 else 'menor'} de idade e {'casado' if casado == 1 else 'solteiro'}")