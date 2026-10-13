#Bibliotecas
import sys

#Recebendo os dados
seq = input("Insira sua sequência de dna: ")
seq = seq.replace(" ", "") #remove os espaços em branco
seq = seq.upper() #Joga tudo pra UPPER

#Verificando se é ATCG

for base in seq:
    if base not in "ATCG":
        print("Na sua sequência existem caracteres além de ATCG")
        sys.exit()

#Definindo as variáveis
A = 0
C = 0
T = 0
G = 0

#Contando as bases

for n in seq:
    if n == "A":
        A += 1
    elif n == "T":
        T += 1
    elif n == "C":
        C += 1
    elif n == "G":
        G += 1

#Mostrando os resultados
print("=================--===========")
print(f"A: {A}")
print(f"C: {C}")
print(f"T: {T}")
print(f"G: {G}")
print("=================--===========")