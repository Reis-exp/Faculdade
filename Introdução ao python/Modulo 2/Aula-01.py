#operações em sequencias
"""texto = ('Explorando a diversidade de linguagens de programação com Python.')
print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto }")
print(f'Quantidade de e no texto = {texto.count('e')}')
print(f'A primeiras 5 letras do texto são = {texto[:5]}')
print(f'Tem letra maiuscula no texto = {texto.isupper()}')"""

#Manipulção de listas
"""cores = ['vermelho', 'azul', 'verde','amarelo','rosa']
for cor in cores:
    print(f'Posição {cores.index(cor)}: {cor}')"""

#List comprehension
"""linguagens = ['Python', 'Java', 'JavaScript', 'C' ,'C#', 'C++', 'Swift', 'GO','Kotlin']
print('antes da listcomps =' , linguagens)
linguagens = [item.lower() for item in linguagens]
print('\ndepois da listcomps =', linguagens) """

#Função Map
"""precos_em_dolares = [100,50,75,120]
taxa_de_cambio = 5.25
precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))
print(precos_em_reais)"""

#função filter
"""numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_pares = list(filter(lambda x : x % 2 == 0, numeros))
print(numeros_pares)"""

#tuplas 
'''vogais = ('a','e','i','o','u') #sempre irá comecar a contar do 0 
print(f'Tipo do objeto vogais = {type(vogais)} ')
for p, x in enumerate(vogais):
    print(f'Posição = {p}, valor = {x}')'''

#Exercicio da aula
convidados = ('Alice','Bob','Carol','David','Eve') #tupla sempre entre parenteses
confirmados = ['Bob','Eve']
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]
print('Convidados que não confirmaram presença:')
for pessoa in nao_confirmados:
    print(pessoa)
print('\nEnviando lembrete para os não confirmados:')

