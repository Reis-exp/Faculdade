'''num = [1,2,3,4,5,6,7,8,9,10]
for n in num:
    print(n)''' #Exemplo de for

"""numero = int(input('Digite um número (ou digite 0 para sair): '))
while numero !=0:
    if numero % 2 == 0:
        print('O numero é par.')
    else:
        print('O numero é impar.')
    numero = int(input('Digite um número (ou digite 0 para sair): '))""" #Exemplo de while

#Exemplo de range
#repetição por quantidade
"""for x in range(5):
    print(x)

#Limites inicial ou superior
for y in range(2,7):
    print(y)

#com incremento
for z in range(1,11,2):
    print(z) """
#Exemplo de break
"""for numero in range (1,11):
    if numero % 2 == 0:
        print('Este número é par:', numero)
        break """

#Exemplo de continue
for numero in range (1,11):
    if numero == 5:
        continue
    print(numero)