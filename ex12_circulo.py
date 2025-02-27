"""
Programa: 
Descrição: Este programa calcula a área de um círculo e o comprimento de sua circunferência.
Autor: Mayara Binsfeld
Data: 27/02/2025
Versão: 0.0.1

"""
import math

# Alocação de memória
raio = 0

# Entrada de dados 
raio = float(input("Qual o raio do círculo?"))

# Processamento de dados

circunferencia = 2*math.pi*raio
area = math.pi*raio**2

# Saída de dados
print(f"A área do círculo é {area}")
print(f"A circunferência do círculo é {circunferencia:.2f}")