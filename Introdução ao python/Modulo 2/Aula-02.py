'''##add(), in e remove()
#criando e adicionando elementos a um conjunto
meu_conjunto = set()
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)
print('Conjunto apos adicionar os elementos:', meu_conjunto)
#verificando se um elemento esta presente no conjunto
elemento = 20
if elemento in meu_conjunto:
    print(f'{elemento} está no conjunto.')
else:
    print(f'{elemento} não está no conjunto.')
#Removendo um elemento do conjunto
meu_conjunto.remove(20)
print('Conjunto apos remover o elemento 20:', meu_conjunto)'''
#IDEIA NICOLAS: DA PARA CRIAR UM PROGRAMA DE ESTOQUE USANDO CONJUNTOS E QUANTIDADE COM VARIAVEL DIRETA, TIPO UM DICIONARIO, AI DA PARA ADICIONAR, REMOVER E VERIFICAR SE TEM O PRODUTO NO ESTOQUE
#Mapping usando distribuição de chave e valor separados
"""dici_1 = {}
dici_1 ['Nome'] = 'Nicolas'
dici_1 ['Idade'] = 18
#Mapping usando distribuição de chave e valor juntos
dici_2 = {'Nome': 'Nicolas', 'Idade': 18}
#mapping criando dicionario com uma lista em tuplas representando chave e valor
dici_3 = dict([('Nome', 'Nicolas'), ('Idade', 18)])
#Criação de dicionario com zip () e duas listas uma lista para chave e outra para valor
dici_4 = dict(zip(['Nome', 'Idade'], ['Nicolas', 18]))
print(dici_1 == dici_2 == dici_3 == dici_4) 
print(dici_1) """
#utilização da biblioteca NumPy
'''import numpy as np
my_array = np.array ([1,2,3,4,5])
print('Array original:')
print(my_array)
#Iremos fazer contas utilizando o primeiro array
squared_array = my_array ** 2
print('\nArray ao quadrado')
print(squared_array)
sum_of_elements = np.sum (my_array)
print('\nA soma de todos os numéros do array original é:',sum_of_elements)
#Iremos acessar somente um único valor dentro do array
element_at_index_2 = my_array[2]
print('O segundo valor do array original é:', element_at_index_2)'''
#Exercicio da Aula-02


import numpy as np
participantes = [
    {
    "nome": "Alice",
    "localizacao" : "EUA",
    "afiliacao" : "Universidade A",
    "interesses" : ["Física" , "Astronomia"]
},
{
    "nome": "Bob",
    "localizacao" : "Brasil",
    "afiliacao" : "Instituto B",
    "interesses" : ["Biologia" , "Astronomia"]
},
{
    "nome": "Charlie",
    "localizacao" : "India",
    "afiliacao" : "Instituto C",
    "interesses" : ["Quimica" , "Engenharia"]
}
]

regioes = set(participante["localizacao"] for participante in participantes)

afiliacoes = {}
for participante in participantes:

    afiliacao = participante["afiliacao"]
    
    if afiliacao not in afiliacoes:
    
        afiliacoes[afiliacao] = []
    
    afiliacoes[afiliacao].append(participante["nome"])

areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante["interesses"]])

interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)

area_mais_popular = interesses_unicos[np.argmax(contagem)]

print('Regioes dos participantes:', regioes)
print('Afiliacao dos participantes:')
for afiliacao, nomes in afiliacoes.items():
    print(f'{afiliacao}: {', '.join(nomes)}')
print('area de interesse mais popular:', area_mais_popular)