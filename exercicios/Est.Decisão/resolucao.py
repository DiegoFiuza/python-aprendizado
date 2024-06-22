"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento
    """
'''Funciona
print('Informe seu salário abaixo para informarmos o reajuste! ')
salario = float(input('Digite seu salário atual: '))
if salario <= 280:
    percentual = 20/100
    aumento = salario * percentual
    novo_salario = salario + aumento
elif salario >280 and salario <=700:
    percentual = 0.15
    aumento = salario * percentual
    novo_salario = salario + aumento
elif salario > 700 and salario <= 1500:
    percentual = 0.1
    aumento = salario * percentual
    novo_salario = salario + aumento
else:
    percentual = 0.05
    aumento = salario * percentual
    novo_salario = salario + aumento

print(f'Salário antes do reajuste era de R$ {salario}')
print(f'O perceuntual do reajuste é de {percentual}')
print(f'O aumento foi de R$ {aumento}')
print(f'O salário após o reajuste é de R$ {novo_salario}')

'''

#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida
'''
FUNCIONA

print('Informe uma data no formado dd/mm/aaaa abaixo.')
dia = int(input('Informe um dia: '))
mes = int(input('Informe um mês: '))
ano = int(input('Informe um ano: '))

if dia == 0 or dia > 31 or mes == 0 or mes >12:
    print('Data inválida!!')
else:
    print(f'A data informada é {dia}/{mes}/{ano}')

    '''

'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
 O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
 Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
 entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
 Caso contrário, ele será classificado como "Inocente"
'''

print('Irei te fazer algumas perguntes sobre um crime ocorrido. Responda com "s" para sim e "n" para não')
pergunta_1 = input("Telefonou para a vítima?")
pergunta_2 = input("Esteve no local do crime?")
pergunta_3 = input("Mora perto da vítima?")
pergunta_4 = input("Devia para a vítima?")
pergunta_5 = input("Já trabalhou com a vítima?")
sim = "s"
contador_de_sim = 0
if pergunta_1 == sim:
    contador_de_sim = contador_de_sim + 1
if pergunta_2 == sim:
    contador_de_sim +=1
if pergunta_3 == sim:
    contador_de_sim +=1
if pergunta_4 == sim:
    contador_de_sim +=1
if pergunta_5 == sim:
    contador_de_sim +=1

if contador_de_sim == 2:
    print('>>> Suspeita <<<')
elif contador_de_sim > 2 and contador_de_sim <= 4:
    print('>>> Cúmplice <<<')
elif contador_de_sim == 5:
    print('>>> Assassino <<<')
else:
    print('>>> Inocente <<<')
    
        