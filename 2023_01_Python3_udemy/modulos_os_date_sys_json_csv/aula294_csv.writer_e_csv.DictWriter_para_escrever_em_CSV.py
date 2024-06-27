# csv.reader le o CSV em formato de lista
# csv.DictReader le o CSV em formato de dicionário
# csv.writer escreve em um arquivo CSV

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula294.csv'

lista_clientes = [
    {'Nome': 'Luiz Otavio', 'Endereco': 'Av sao joao 22'},
    {'Nome': 'Julio pereira', 'Endereco': 'Av sao menezes 23'},
    {'Nome': 'Junior pereira', 'Endereco': 'Av sao gabriel 24'}
] 


# EXEMPLO COM WRITER:
# with open(CAMINHO_CSV, 'w') as arquivo:
#     nome_colunas = lista_clientes[0].keys()
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for clinte in lista_clientes:
#         # print(clinte.values())
#         escritor.writerow(clinte.values())

# EXEMPLO COM DICTWRITER:
with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )                      

    escritor.writeheader()      # escreve o cabecalho das colunas

    for cliente in lista_clientes:
        # print(clinte.values())
        print(cliente)
        escritor.writerow(cliente)