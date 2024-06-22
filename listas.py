listas = 'Listas'
print(listas.upper().center(10,"#"))

frutas = ['laranja', 'maça', 'uva']
print(frutas)
frutas =[]
print(frutas)
letras = list('python')
numeros = list(range(10))

print(letras)
print(numeros)

carro = ['Lamborghini', 'Veneno' , 42000, 2024, 100, True]
print(carro)

#acessando os indices da lista

print(carro[0])
print(carro[3])

#lista aninhada
matriz = [
    [1,"a",2],
    ['b',3,4],
    [6,5,'c']
]
#vira matriz ij

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])
print(matriz[1][2])
print(matriz[2][0])

#fatiamento
lista = ['p','y','t','h','o','n']
print(lista[2:])
print(lista[:2])
print(lista[1:3]) #INICIAL/FINAL/ o final é sempre o indice indicado -1
print(lista[0:3:2]) #incial/final/step
print(lista[::])
print(lista[::-1])

#iterar lista

carros = ['Gol','Celta','Astra']

for carro in carros:
    print(carro)

#enumerate 
for indice,carro in enumerate(carros):
    print(f'{indice}:{carro}')

#compreensao de lista
numeros = [1,30,21,2,9,65,34]
pares = []
for numero in numeros:
    if numero%2 ==0:
        pares.append(numero)
print(pares)
#ou 
pares = [numero for numero in numeros if numero%2 ==0]
print(pares)


print('Metodo Class list')

#[].append adiciona um elemento na lista
lista = []
lista.append(1)
lista.append('Python')
print(lista)

#.clear
lista.clear()
print(lista)

lista = []
lista.append(1)
lista.append('Python')
#.copy[]
l2 = lista.copy() #copia a lista com uma instancia diferente
print(l2)
print(id(l2), id(lista))

#.count

cores = ['Vermelho','Azul','Verde','Azul']

print(cores.count('Vermelho'))
print(cores.count('Verde'))
print(cores.count('Azul'))
#extend adiciona varios elementos em uma lista

ling = ['python','js','c']
print(ling)
ling.extend(['java','laravel'])
print(ling)

#index descobre a ocorrencia de um obj em lista
#exemplo
print(ling.index('java'))
print(ling.index('c'))

#.pop (vai tirando o ultimo elemento da lista ou um elemento de um index info)
ling.pop()
print(ling)
ling.pop()
print(ling)
ling.pop(1)
print(ling)

#remove (diferente do pop, ele informa o obj ao inves do index)
ling.remove('python')
print(ling)

ling = ['python','c','csharp','js','laravel']
print(ling)
print('Reverse abaixo')
ling.reverse() # ou print(ling[::-1])
print(ling)

#Sort (ordena a lista)
ling.sort()
print(ling)
ling.sort(reverse=True) #espelha o sort
print(ling)
ling.sort(key=lambda x: len(x)) #ordena do tamanho da palavra - para +
print(ling)
ling.sort(key=lambda x: len(x), reverse=True)
print(ling)

#len (tamanho)
print(len(ling))

#sorted (serve tbm para ordena)
sorted(ling, key=lambda x: len(x))
print(ling)
sorted(ling, key=lambda x: len(x), reverse=True)
print(ling)