#Primeiro exercicio para mostrar if, else e elif(exemplo aula)
"""idade = int(input('Digite a sua idade: '))
if idade < 18:
    print('Você é menor de idade')
elif idade >= 18 and idade < 50:
    print('Você é maior de idade')
else:
    print('Você é idoso')
"""
#Segundo exercício para mostrar if, else e elif(ideia nicolas)

filme1 = 'Carros'
filme2 = 'Harry Potter'
filme3 = 'Deadpool'
horario_filme1 = '14:00'
horario_filme2 = '16:00'
horario_filme3 = '18:00'
quantidade_ingressos = 5
ingresso_inteiro = 20
ingresso_meia = 10

print('Digite a sua idade:')
idade = int(input())
if idade <= 12:
    print('O filme disponível para essa idade é:', filme1)
    print('Horário:', horario_filme1)
elif idade >= 13 and idade < 17:
    print('O filme disponível é:', filme2)
    print('Horário:',horario_filme2)
else:
    print('O filme disponível é:', filme3)
    print('Horário:',horario_filme3)

print('Quantos ingressos você deseja comprar?')
quantidade_ingressos = int(input())
if quantidade_ingressos <= 5:
    print('Todos os ingressos Disponíveis, Aproveite!')
else:
    print('Desculpe, não temos ingressos suficientes.')

print('Você tem direito a meia entrada? (s/n)')
meia_entrada = input()
if meia_entrada == 's':
    valor_total = (quantidade_ingressos * ingresso_meia)
    print('O valor total da sua compra é:', valor_total)
else:
    valor_total = (quantidade_ingressos * ingresso_inteiro)
    print('O valor total da sua compra é:', valor_total)