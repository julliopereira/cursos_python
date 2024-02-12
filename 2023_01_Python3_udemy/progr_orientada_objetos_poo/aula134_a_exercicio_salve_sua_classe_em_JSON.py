# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

# ------------ MEU CODIGO -------------

# import json

# class Roteador:
#     def __init__(self, device):
#         self.device = device
#         self.uptime()
#         self.latencia()
#         self.perdas()
#         self.drops()
#         self.colisao()

#     def uptime(self):
#         resultado = []
#         arquivo_json = 'aula134_uptime.json'
#         resultado.append(f'"{self.device}" uptime  :  X minutos')
#         with open(arquivo_json, 'w') as arquivo:
#             json.dump(
#                 resultado, 
#                 arquivo,
#                 indent=2
#             )

#     def latencia(self):
#         resultado = []
#         arquivo_json = 'aula134_latencia.json'
#         resultado.append( f'"{self.device}" latencia:  X ms')
#         with open(arquivo_json, 'w') as arquivo:
#             json.dump(
#                 resultado, 
#                 arquivo,
#                 indent=2
#             )
    
#     def perdas(self):
#         resultado = []
#         arquivo_json = 'aula134_perdas.json'
#         resultado.append( f'"{self.device}" perdas  :  X pacotes')
#         with open(arquivo_json, 'w') as arquivo:
#             json.dump(
#                 resultado, 
#                 arquivo,
#                 indent=2
#             )
    
#     def drops(self):
#         resultado = []
#         arquivo_json = 'aula134_drops.json'
#         resultado.append( f'"{self.device}" drops   :  X drops')
#         with open(arquivo_json, 'w') as arquivo:
#             json.dump(
#                 resultado, 
#                 arquivo,
#                 indent=2
#             )
    
#     def colisao(self):
#         resultado = []
#         arquivo_json = 'aula134_colisao.json'
#         resultado.append( f'"{self.device}" colisoes:  X colisoes')
#         with open(arquivo_json, 'w') as arquivo:
#             json.dump(
#                 resultado, 
#                 arquivo,
#                 indent=2
#             )

# Roteador('cisco')


# ------------ PROFESSOR  -------------

import json

CAMINHO_ARQUIVO = 'aula134_prof.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Joao', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Paulo', 11)
bd = [vars(p1), vars(p2), vars(p3)]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)