#utiliza o set para eliminar el duplicados. É uma coleção de obj que possuem el unicos
numeros = set([1,2,3,1,3,4])
print(numeros)
letras = set(("abacaxi"))
print(letras)
#Conjuntos não são indexaveis, para acessar os dados precisam ser transformados em lista

letras = list(letras)
print(letras[3])

#pode usar for com set
letras = set(("abacaxi"))
for letra in letras:
    print(letra)

#union
conjunto_a = {1,2}
conjunto_b = {3,4}
print(conjunto_a.union(conjunto_b))

#intersection

conjunto_c = {1,2,3}
conjunto_d = {3,4,1}
print(conjunto_c.intersection(conjunto_d))

#difference
print(conjunto_c.difference(conjunto_d))
print(conjunto_d.difference(conjunto_c))

#symmetric_difference
print(conjunto_c.symmetric_difference(conjunto_d))

#issubset se é ou nao subconjunto

print(conjunto_a.issubset(conjunto_b))
#issuperset contrario de subset
#isdisjoint não estão presentes no outro conjunto
#add  adiciona um elemento no conjunto, se for elemento iggual e ele é ignorado
#clear limpa o conjunto
#copy gera uma cópia
#discard. descarta um valor do conjunto
num = {1,2,1,3,4,5,6,7,8,98}
num.discard(2)
print(num)
num.discard(80)
print(num)