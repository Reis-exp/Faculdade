class Pessoa:
    #o metodo _init_ é um construtor, chamado quando um objeto da classe é criado, ele é responsavel por iniciar os atributos da classe.
    def __init__(self, nome, idade, genero):
        self.nome  = nome
        self.idade = idade
        self.genero = genero
    
    def cumprimentar(self):

        return f"Olá meu nome é {self.nome}."

    def aniversario(self):
        self.idade +=1

pessoa1 = Pessoa("João", 30, 'Masculino')

print(pessoa1.cumprimentar())
print(f"Idade:{pessoa1.idade}")

pessoa1.aniversario()

print(f"Nova idade: {pessoa1.idade}")