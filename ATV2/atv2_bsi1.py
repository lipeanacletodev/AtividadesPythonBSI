# -*- coding: utf-8 -*-
"""
1 - Fazer um algoritmo para ler o valor do lado de um quadrado e mostrar sua área
( lado²
) e seu perímetro ( 4 x lado ).
"""

lado = int(input("Digita o tamanho do lado do quadrado: "))
print(f"Sua área é de: {lado ** 2}" )
print(f"Seu perimetro é de: {lado * 4}")

"""2 - Elaborar um algoritmo para ler o nome e a quantidade de filhos de uma pessoa.
Mostrar a mensagem: “Fulano tem 5 filhos.”
"""

nome = input("Digite seu nome: ")
qtdfilhos = int(input("Digite quantos você tem: "))
print(f"{nome} tem {qtdfilhos} filhos")

"""3 - Fazer um algoritmo para ler os valores da base e altura de um retângulo e mostrar
seu perímetro ( 2 x ( base + altura ) ) e sua área ( base x altura ).
"""

base = int(input("Digite o valor da base do retângulo: "))
altura = int(input("Digite o valor da altura do retângulo: "))
perimetro = 2 * (base+altura)
area = base*altura
print(f"Sua base é de {base} e sua altura é de {altura}")

"""4 - Fazer um algoritmo para ler o valor do lado de um cubo e
mostrar sua área (6 x lado²) e seu volume ( lado³
).
"""

lado = int(input("Digite o valor do lado do cubo: "))
area = 6*lado**2
volume = lado**3
print(f"sua area é de {area} e seu volume é de {volume}")

"""5 - Elaborar um algoritmo para ler dois números e mostrar o quociente e o resto da
divisão inteira do primeiro pelo segundo número.
"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
print(f"O quociente é de {n1/n2} e o resto da divisão é de {n1%n2}")

"""6 - Criar um algoritmo para ler a base e a altura de um triângulo e
mostrar a sua área ( ( base x altura ) / 2 ).
"""

base = int(input("Digite a base do triangulo: "))
area = int(input("Digite a altura do triangulo: "))
print(f"A área desse triangulo é de {(base*altura)/2}")

"""7 - Construir um algoritmo para ler o raio de uma circunferência e
mostrar o perímetro ( 2 x π x raio ) e a área ( π x raio²).
"""

import math
raio = int(input("Digite o raio da circunferência: "))
perimetro = 2*math.pi*raio
area = math.pi*raio**2
print(f"O perimetro desta circunferência é de {perimetro :.2f}, e a area é de  {area :.2f}")