# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.


# ------------ PROFESSOR  -------------

import json

from aula134_a_exercicio_salve_sua_classe_em_JSON import CAMINHO_ARQUIVO, Pessoa


with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)

    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)










# CAMINHO_ARQUIVO = 'aula134_prof.json'

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# p1 = Pessoa('Joao', 33)
# p2 = Pessoa('Helena', 21)
# p3 = Pessoa('Paulo', 11)
# bd = [vars(p1), vars(p2), vars(p3)]

# with open(CAMINHO_ARQUIVO, 'w') as arquivo:
#     json.dump(bd, arquivo, ensure_ascii=False, indent=2)