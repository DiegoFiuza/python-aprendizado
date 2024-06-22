curso = 'pYthOn'

print(curso.upper())

print(curso.lower())

print(curso.title())

#elimina espaço em branco
curso = '   Python'
print(curso.strip()) #elimina o espaço da equerda e direita
print(curso.lstrip()) #elimina o espaço somente da esquerda
print(curso.rstrip())#elimina o espaço somente da direita

#junção e centralização

curso = 'Python'
print(curso.center(10, "#")) #centraliza a string
print(".".join(curso)) #junta a string com o caractere, passa letra a letra, e a cada passada ad o caracter

interp = 'interpolação de variáveis'

print(interp.upper().center(29, "*"))

#metodo format

nome = 'Diego'
idade = 22
profissao = 'Programador'
linguagem = 'Python'

print('Olá meu nome é {}. Tenho {} anos e sou um {}, utilizo em meu trabalho a linguagem {}.'.format(nome,idade,profissao,linguagem))

#ou
print("Olá meu nome é {0}. Tenho {1} anos e sou um {2}, utilizo em meu trabalho a linguagem {3}.".format(nome,idade,profissao,linguagem))#indexa/smp comeca no 0

#f-string

print(f"Olá meu nome é {nome}. Tenho {idade} anos e sou um {profissao}, utilizo em meu trabalho a linguagem {linguagem}.")
PI = 3.14159
print(f'O valor de PI é {PI:.2f}')

fatiamento = 'Fatiamento de String'
print(fatiamento.upper().center(28, "*"))

nome = 'Diego Nasser Fiuza'

nome[0]
print(nome[:5])
print(nome[:9])
print(nome[:]) #nome todo
print(nome[::-1]) #ao contrario ou espelhamento da string
print(nome[0])
print(nome[0:7:2])
print(nome[0:17:4])
print(nome[-1])

multi_linha = 'Multi linhas'
print(multi_linha.upper().center(28, "*"))

nome = 'Diego'

print(f""" 
    Olá meu nome é {nome},
    E eu estou aprendendo Python
""")
#str tripla utiliza aspas triplas e ele conserva a formatação