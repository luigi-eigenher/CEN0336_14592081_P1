#Bibliotecas
import sys

#Recebendo os dados
dados1 = input("Insira sua sequência e as coordenadas que delimitam as regiões codificante, separadas por espaços:")
seq, n1, n2, n3, n4, n5, n6 = dados1.split()
lista = [n1, n2, n3, n4, n5, n6]
seq = seq.upper() #Joga tudo pra UPPER

#Conferindo os dados
for base in seq:
    if base not in "ATCG":
        print("================================--==========================")
        print("Na sua sequência existem caracteres além de ATCG!")
        print("================================--==========================")
        sys.exit()

for n in lista:
    if not n.isdigit():
        print("================================--==========================")
        print(f"A coordenada {n} não é um número inteiro! Digite somente números inteiros!")
        print("================================--==========================")
        sys.exit()
    elif int(n) > len(seq):
        print("================================--==========================")
        print(f"A coordenada {n} excede o tamanho da base!")
        print("================================--==========================")
        sys.exit()

#Transformando em int:

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)
n5 = int(n5)
n6 = int(n6)

#Extraindo as CDS

cds1 = seq[(n1-1):n2] # CDS1
cds1_ver = cds1[0:3]
if cds1_ver == "ATG":
    print("================================--==========================")
    print("O CDS1 começa com o códon inicial (ATG)")
else:
    print("================================--==========================")
    print("O CDS1 não começa com o códon inicial (ATG)")
    print("================================--==========================")
    sys.exit()

cds2 = seq[(n3-1):n4] # CDS2

cds3 = seq[(n5-1):n6] # CDS3
cds3_ver = cds3[-3:]
if cds3_ver == "TAG":
    print("================================--==========================")
    print("O CDS3 termina com a sequência (TAG)")
    print("================================--==========================")
elif cds3_ver == "TAA":
    print("================================--==========================")
    print("O CDS3 termina com a sequência (TAA)")
    print("================================--==========================")
elif cds3_ver == "TGA":
    print("================================--==========================")
    print("O CDS3 termina com a sequência (TGA)")
    print("================================--==========================")
else:
    print("================================--==========================")
    print("O CDS3 não termina com nenhum códon de parada")
    print("================================--==========================")
    sys.exit()

#Concatenando as strings

final = cds1 + cds2 + cds3

print("A sequência concatenada é:")
print(final)

