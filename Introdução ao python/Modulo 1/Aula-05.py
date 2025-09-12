valor_produto = float(input('Digite o valor do produto: R$'))
percentual_desconto = float(input('Digite o percentual de desconto: '))

if percentual_desconto <0 or percentual_desconto >100:
    print("o percentual de desconto deve estar entre 0 e 100")
else:
    desconto = valor_produto * (percentual_desconto / 100)
valor_final = valor_produto - desconto
print(f'O valor final do produto com desconto é: R${valor_final:.2f}')
