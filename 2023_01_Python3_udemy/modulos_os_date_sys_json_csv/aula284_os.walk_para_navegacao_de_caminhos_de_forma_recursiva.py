# os.walk
# os.walk é uma função que permite percorrer uma estrutura de diretórios de 
# maneira recursiva. Ele gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).

import os
from itertools import count

caminho = os.path.join('/home', 'jper', 'Documentos', 'git')
counter = count()

for root, dirs, files in os.walk(caminho):
    contador = next(counter)
    print(contador, 'Pasta atual', root)

