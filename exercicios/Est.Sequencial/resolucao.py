# Faça um Programa que peça dois números e imprima a soma.
"""
Funciona
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
print(f"A soma desses números é {soma}")
""" 

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

Funciona corretamente ***
print("Abaixo irei solicitar as notas de seus 4 bimestres e irei informar a média. Para passar, precisa ter a média acima de 7\n")

nota1 = float(input('Digite a nota do 1 semestre: '))
nota2 = float(input('Digite a nota do 2 semestre: '))
nota3 = float(input('Digite a nota do 3 semestre: '))
nota4 = float(input('Digite a nota do 4 semestre: '))

media_nota = (nota1 + nota2 + nota3 + nota4) / 4
print(f'Sua média final foi {media_nota}')
if media_nota > 7:
    print('Você foi aprovado!!')
else:
    print('Você foi para a recuperação :(')

"""

#Faça um Programa que converta metros para centímetros
"""
Funfa
metro = float(input('Digite um número em metros para ser convertido para cm: '))

centimeter = metro*100

print(f'O número informado em centímetros é {centimeter} centímetros')

"""

"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
    """


"""
*** Funciona perfeitamente ***
print('Me informe seu salário por hora e horas trabalhadas e irei te informar seu salário bruto, descontos e salário líquido!!!')

ganho_hora = float(input('Digite seu ganho por hora em R$: '))
hora_trab = int(input('Digite a quantidade de horas do mês '))
salario_bruto = ganho_hora*hora_trab
print(f'Seu salário bruto mensal é de R${salario_bruto :.2f}')
inss = salario_bruto * (8/100)
print(f'Pagou ao INSS R${inss :.2f}')
ir = salario_bruto*(11/100)
print(f'Pagou ao IR R${ir:.2f}')
sindicato = salario_bruto* (5/100)
print(f'Pagou ao Sindicato: R${sindicato :.2f}')
salario_liquido = salario_bruto - inss - ir - sindicato
print(f'Seu salário líquido descontado é R${salario_liquido}')

"""

"""
Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

print('Irei informar a quantidade de latas a serem utilizadas e o preço a partir de informações abaixo.')
tamanho_area = int(input('Informe a área em metros quadrados que irá ser pintada: '))
litro_necessario = tamanho_area/3
print(litro_necessario)
lata = litro_necessario/18
valor = lata*80.0
if lata <= 1:
    print('Você precisará de 1 lata e seu valor será de R$ 80,00')
else:
    print(f'Você precisará de {lata :.2f} latas e ficará no valor de R${valor :.2f} reais')
