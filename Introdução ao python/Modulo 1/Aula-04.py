# função Len()
'''numeros = [1, 2, 3, 4, 5]
# Usa a função len() para calcular o comprimento da lista
comprimento = len (numeros)
# imprime o comprimento da lista
print('O comprimento da lista é:',comprimento) '''

#criando funções
'''def soma(a,b):
    resultado = a + b
    return resultado
resultado_soma = soma(2,3)
print('O resultado da soma é:', resultado_soma) '''
# definindo função e_par
"""def e_par(numero):
    #operador módulo (%)
    if numero % 2 == 0:
        return True
    else:
        return False
    
numero = 26126171
if e_par(numero):
    print(f'{numero} é par')
else:
    print(f'{numero} é impar')"""
#Função lambda
"""soma = lambda a,b: a + b
resultado = soma(5,3)
print('O resultado da soma é:', resultado)"""
#########################################################
#exercio aula 4

notas = [7.5, 8.0, 6.5, 9.0, 7.0] # Lista de notas dos alunos
def calcular_media(notas):
    total = sum(notas) # Calcula a soma das notas
    media = total / len(notas)
    return media
#funcao lambda para arredondar a media
arredondar_media = lambda media: round(media,2)
media = calcular_media(notas)
media_arredondada = arredondar_media(media)
#Verificar se foram aprovados
situacao = "APROVADO" if media_arredondada >=7 else "REPROVADO"
#RESULTADO
print('notas dos estudantes:',notas)
print('Média das notas:', media_arredondada)
print('Situação do estudante:', situacao)