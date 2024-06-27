# csv.reader e csv.DivtReader
# csv.reader le o CSV em formato de lista
# csv.DictReader le o CSV em formato de dicionario

import csv
from pathlib import Path

# CAMINHO_CSV = Path(__file__).parent
CAMINHO_CSV = Path(__file__).parent / 'aula293_.cvs'

# print(CAMINHO_CSV)

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    # print(next(leitor))

    for linha in leitor:
        print(linha['Nome'],',', linha['Idade'],',',linha['Endereço'])

