# json.dump() - ACEITA DOIS ARGUMENTOS:
# PRIMEIRO ARG:   O QUE SERÁ ARMAZENADO
# SEGUNDO ARG:    ONDE SERÁ ARMAZENADO (ARQUIVO)

import json

numbers = [2, 3, 5, 7, 11, 13]            # CONTROI UMA LISTA COM NUMEROS

filename = 'numbers.json'                 
with open(filename, 'w') as f_obj:        # ESCREVE 'w' NO ARQUIVO numbers.json (SE NÃO EXISTIR ELE CRIA O ARQUIVO)
    json.dump(numbers, f_obj)             # UTILIZA json.dump PARA ARMAZENAR O CONTEUDO numbers NO ARQUIVO GRAVADO EM f_obj