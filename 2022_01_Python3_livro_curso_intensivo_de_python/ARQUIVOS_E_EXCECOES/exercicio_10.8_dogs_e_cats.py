# LER OS ARQUIVOS dogs.txt E cats.txt 
# COLEQUE O PROGRAMA EM UM BLOCO try-except PARA CAPTURAR O ERRO FileNotFoundError


def ler_arquivo(file):
    try:
        with open(file, 'r') as f_obj:
            arquivo = f_obj.read()
    except FileNotFoundError:
        print(f'\n\tArquivo "{file}" não encontrado!\n')
    else:
        print(f'Arquivo {file}:')
        print(f'\n{arquivo}')
    

arquivos = input(f'Quais arquivos deseja ler?(espaço entre eles): ')
files = arquivos.split()            # JOGA OS NOMES DOS ARQUIVOS EM UMA LISTA
for file in files:
    ler_arquivo(file)