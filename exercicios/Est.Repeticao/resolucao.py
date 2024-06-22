#Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

---Funciona ---
while True :
    nota = int(input('Digite um número de 0 à 10: '))
    if nota >=0 and nota <= 10:
        print('>>> Valor válido <<<')
        break
    else:
        print('''
        >>>>  Inválido  <<<<
    ...Digite um valor válido...
    ...Solicitando novo input...
''')
        
        """

'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
 mostrando uma mensagem de erro e voltando a pedir as informações.
'''


while True:
    nome = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')
    if senha.title() == nome.title():
        print("""
            ####  Error  ####
            Informe novamente seu usuário e senha. Eles não podem ser iguais!!!
""")
    else:
        print(f"""
            >>> Bem Vindo de Volta {nome} <<<
""")
        break
    