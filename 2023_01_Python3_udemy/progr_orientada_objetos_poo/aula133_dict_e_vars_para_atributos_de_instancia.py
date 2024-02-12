# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 43)
# p1.nome = 'EITA'
# print(p1.idade)
# print(p1.__dict__)  # load onde está guardado minha entrada (é um dicionário)
# print(vars(p1))     # vars também mostra a mesma coisa, mesmo conteudo
# print(p1.outra)
# print(p1.nome)
# print(vars(p1))
print(p1.nome)
print(p1.get_ano_nascimento())

