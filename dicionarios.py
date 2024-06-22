#conjunto não ordenado de pares de chave:valor
#exemplo
pessoa = {"nome": "Diego", "idade": 22}
print(pessoa)
#ou 
pessoa = dict(nome='Diego', idade=22)
print(pessoa)
#ou
pessoa['telefone'] = '22 997824245'
print(pessoa)

#acessar o valor
print(pessoa['nome'])
#pode alterar
pessoa['nome'] = 'Maria'
print(pessoa['nome'])
#pode aninhar dict um dentro do outro
#ex
contatos = {
    'aninha@gmail.com' : {'nome': 'Ana', 'idade': 20},
    'alvaro@gmail.com' : {'nome': 'Álvaro', 'idade': 27},
    'diegof@gmail.com' : {'nome': 'Diego', 'idade': 22},
    'YodaSL@gmail.com' : {'nome': 'Peter', 'idade': 29},
}
print(contatos)
print(contatos['diegof@gmail.com']['idade'])
contatos['diegof@gmail.com']['telefone'] = '997824245'
print(contatos['diegof@gmail.com']['telefone'])

#fromkeys cria chaves
dict.fromkeys(['nome','telefone'])
#ou
dict.fromkeys(['nome','telefone'],"vazio")

#get acessa tbm valor no dicionario
print(contatos.get('chave'))
#ou
print(contatos.get('chave', {}))
#items retorna lista de tuplas
print(contatos.items())
#keys
print(contatos.keys())
#pop
print(contatos.pop('alvaro@gmail.com'))

#popitem
resultado = contatos.popitem()
print(resultado)
#setdefault
contato = {'nome': 'Guilherme', 'telefone':'3333-4532'}
contato.setdefault('nome','Giovanna')
print(contato)
contato.setdefault('idade',28)
print(contato)
#update deixa atualizar o dicionario
#values retorna os valores das chaves no dict
print(contatos.values())

#in retorna TRUE ou FALSE para saber se chave existe