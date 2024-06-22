''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
''' 
    TODO  Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se
    "encaixa" ou "não encaixa" para cada uma das relações N vezes.
'''
N = int(input())

def ultimos_digitos(num):
  return num % 100
for i in range(N):
  A = int(input())
  B = int(input())
  ultimos_digitos_1 = ultimos_digitos(A)
  ultimos_digitos_2 = ultimos_digitos(B)
  if ultimos_digitos_2 == ultimos_digitos_1:
    print('encaixa')
  else:
    print('não encaixa')