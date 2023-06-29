"""
Um número Armstrong é um número inteiro de três dígitos 
que é igual à soma dos cubos de cada dígito. 
Encontre todos os números Armstrong entre números inteiros de três dígitos e imprima-os.

Exemplo: 
153 é um número Armstrong, pois 1³+5³+3³ = 1+125+27 = 153
"""
def is_armstrong_number(number: str):
	result = 0
	for n in number:
		print(int(n) ** 3)
		result += (int(n) ** 3)
		
	print(f"r: {result} ")

if __name__ == '__main__':
	is_armstrong_number('153')