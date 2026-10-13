#Bibliotecas
import sys

#Recebendo os dados do usuário

a = input("Digite o lado (a) do triângulo: ")
b = input("Digite o lado (b) do triângulo: ")

#Verificando inteiro ou não
if not a.isdigit() or not b.isdigit():
    print("Insira somente números inteiros!")
    sys.exit()

# Convertendo para inteiros
a = int(a)
b = int(b)

# Verificando se são maiores que 500
if a > 500 or b > 500:
    print("Insira somente números menores que 500!")
    sys.exit()

#calculando o quadrado da hipotenusa
z2 = (a**2) + (b**2)

#Mostrando a resposta
print("================--=============--=========")
print(f"O quadrado da hipotenusa para o triangulo retângulo com lados a= {a} e b= {b}, é {z2}")
print("================--=============--=========")