#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os
'''
Funciona

num = []
contador = 0
while contador < 5:
    num.append(input('Digite um número inteiro: '))
    contador+=1

print(num)

'''

'''
Funciona

#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa
num = []
contador = 0
while contador < 10:
    num.append(input('Digite um número inteiro: '))
    contador+=1

print(num)
print(num[::-1])

'''

#Faça um Programa que leia 4 notas, mostre as notas e a média na tela
'''
Funciona

notas = []
contador = 0

while contador < 4:
    notas.append(float(input('Digite sua nota do semestre: ')))
    contador+=1
print(notas)
media = sum(notas)/contador
print(media)
'''

#Faça um Programa que leia um vetor de 10 caracteres, 
#e diga quantas consoantes foram lidas. Imprima as consoantes

consoante = []
vogal = []
contador = 0

while contador < 10:
    caractere = input('Digite um caractere: ')
    if caractere == 'a' or caractere == 'A' or caractere == 'e' or caractere == 'E' or caractere == 'i' or caractere == 'I' or caractere == 'o' or caractere == 'O' or caractere == 'u' or caractere == 'U':
        vogal.append(caractere)
        vogal.clear()
    elif not caractere.isalpha():
        print('Caracter inválido. Digite um caracter válido.. ')
    else:
        consoante.append(caractere)
    contador+=1
print(consoante)
print(len(consoante))