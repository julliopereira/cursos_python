# USANDO ARQUIVO remember_me_jason.py e username.txt PARA LEMBRAR O USUARIO.

import json

filename = 'username.json'
with open(filename, 'r') as f_obj:
    username = json.load(f_obj)
print(f'Bem vindo de volta "{username}"')

