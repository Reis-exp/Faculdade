#Vamos calcular as notas dos alunos
aluno1 = input('Digite o nome do aluno:')
nota1 = float(input('Digite a nota 1:'))
nota2 = float(input('Digite a nota 2:'))
nota3 = float(input('Digite a nota 3:'))
notas = [nota1, nota2, nota3]
#notas ele vai ser uma lista para fazer a média na proxima linha
media = sum(notas) / len(notas)
#aqui vai calcular a média somando as notas e dividindo pela quantidade de notas
if media >= 7:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')
    print('----------------------')
#tive que pesquisar para lembrar o pq do f antes das aspas
print('Relatório final:')
print(f'Aluno: {aluno1}')
print(f'Notas: {notas}')
print(f'Média: {media:.2f}')
print('FIM')
#depois de mostrar o resultado ele pergunta se quer calcular a média de outro aluno e repete o processo até que o usuário digite 'n'
repeat = input('Deseja calcular a média de outro aluno? (s/n)')
if repeat == 's':
    aluno1 = input('Digite o nome do aluno:')
    nota1 = float(input('Digite a nota 1:'))
    nota2 = float(input('Digite a nota 2:'))
    nota3 = float(input('Digite a nota 3:'))
    notas = [nota1, nota2, nota3]

    media = sum(notas) / len(notas)
    if media >= 7:
        print('Aluno aprovado!')
    else:
        print('Aluno reprovado!')
        print('----------------------')
    print('Relatório final:')
    print(f'Aluno: {aluno1}')
    print(f'Notas: {notas}')
    print(f'Média: {media:.2f}')
    print('FIM')
else:
    print('Programa encerrado.')
#fiquei em duvida se queria um aluno por vez ou colocar varios alunos, entao fiz para dois alunos, mas da pra repetir o processo quantas vezes quiser