print ('Vamos calcular a média do aluno')
nota1 = int(input('Digite a nota 1:'))
nota2 = int(input('Digite a nota 2:'))
nota3 = int(input('Digite a nota 3:'))
nota4 = int(input('Digite a nota 4:'))



media = (nota1 + nota2 + nota3 + nota4) / 4
print('A média do aluno é :', media)
if media >= 5:
    print('O aluno passou de ano!')
else:
    print('O aluno não passou de ano')
