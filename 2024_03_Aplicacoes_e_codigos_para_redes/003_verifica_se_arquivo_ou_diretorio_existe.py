from pathlib import Path
import os

# se arquivo existe ********

arquivo = Path("arquivo.txt")


if arquivo.exists():
    print(f'arquivo {arquivo} existe')
else:
    print(f'arquivo {arquivo} nao existe')

# outro exemplo 

arquivo = ("arquivo.txt")

if os.path.exists(arquivo):
    print(f'arquivo existe')
else:
    print(f'arquivo nao existe')


# diretorio ***********
    
diretorio = "/home/jper"

if os.path.exists(diretorio):
    print(f'diretorio {diretorio} existe')
else:
    print(f'diretorio {diretorio} nao existe')