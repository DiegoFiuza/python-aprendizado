#usa o def
def exibir_mensagem():
    print('Olá mundo')

def exibir_mensagem2(nome):
    print(f"seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem2(nome='Diego')

#utilizando return pode retornar mais de um valor
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero +1

    return antecessor, sucessor

print(calcular_total([10,20,34]))
print(retorna_antecessor_sucessor(10))

#args e kwargs (*args ou **kwargs) tupla e dicionario respectivamente
def exibir_poema(data_extenso,*args,**kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}:{valor}' for chave,valor in
                            kwargs.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

exibir_poema('Zen of Python','Beautiful ir better than ugly.', autor='Tim Peters',ano=1999)

