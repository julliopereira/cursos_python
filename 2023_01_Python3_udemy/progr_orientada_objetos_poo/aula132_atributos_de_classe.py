# Atributos de classe
class Pessoa:
    ano_atual = 2022  # <<<< atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(f'ano atual',Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(f'ano de nascimento {p1.nome}:',p1.get_ano_nascimento())
print(f'ano de nascimento {p1.nome}:',p2.get_ano_nascimento())