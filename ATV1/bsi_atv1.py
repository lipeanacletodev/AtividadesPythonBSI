"""
1 - Faça um programa que peça dois números inteiros e imprima a soma desses dois números.
"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1+n2
print(f"A soma desses dois números é de {soma}",)

"""
2 - Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
"""

metro = float(input("Digite um valor em metros: "))
mm = metro*1000
print(f"Esse valor em metros convertidos para cm equivale a {mm} centimetros")

"""
3 - Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o
total em segundos.
"""

dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("minutos: "))
segundos = int(input("Segundos: "))
conversaoparasegundos = (dias*86400)+(horas*3600)+(minutos*60)+segundos
print(f"Esses dias, horas, minutos e segundos totalizam {conversaoparasegundos} segundos")

"""
4 - Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
porcentagem do aumento. Exiba o valor do aumento e do novo salário.
"""

salario = float(input("Digite seu salario: "))
aumento = float(input("Digite a porcentagem de aumento: "))
salarioaumentado = salario*((aumento/100+1))
print(f"Seu salario passará a ser de {salarioaumentado :.2f} reais")

"""
5 - Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a
pagar.
"""

valormercadoria = float(input("Digite o valor da mercadoria: "))
desconto = int(input("Digite o percentual de desconto: "))
valorfinal = valormercadoria*(1-(desconto/100))
desconto = valormercadoria-valorfinal
print(f"O valor final do produto sera de {valorfinal} reais e o desconto será de {desconto} reais")

"""
6 - Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
esperada para a viagem.
"""

distancia = int(input("Digite a distancia a ser percorrida em km: "))
velocidade = int(input("Digite a velocidade média em km/h: "))
tempo = distancia/velocidade
print(f"A viagem levará {tempo} horas")

"""
7 - Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32 . Faça agora o
contrário, de Fahrenheit para Celsius.
"""

c = int(input("Digite a temperatura em Celsius: "))
cparaf = 9*c/5+32
print(f"{c}º Celsius equivalem a {cparaf :.2f}º Fahrenheit")
f = int(input("Digite um valor para Fahrenheit: "))
fparac = (f-32)*5/9
print(f"{f}º Fahrenheit equivalem a {fparac :.2f}º Celsius")

"""
8 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o
carro custa RS 60,00 por dia e RS 0,15 por km rodado.
"""

diasalugados = int(input("Digite a quantidade de dias que o carro foi alugado: "))
kmpercorrido = float(input("Digite quantos km foram percorridos com o carro: "))
precoapagar = (diasalugados*60)+(kmpercorrido*0.15)
print(f"O preço total a ser pago pelo uso do carro será de {precoapagar :.2f} Reais")

"""
9 - Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade
de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos
de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
"""

cigarrospordia = int(input("Digite quantos cigarros você fuma por dia: "))
tempo = int(input("Digite a quantos anos você fuma: "))
tempofumando = (tempo*365*cigarrospordia*10)
tempofumando = (tempofumando/60)/24
print(f"Você perdeu {tempofumando :.0f} dias de vida.")

"""
10 - Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um
milhão.
"""

numero = 1000000
numeroconvertido = str(numero)
numdigitos = len(numeroconvertido)
print(f"Há {numdigitos} digitos")