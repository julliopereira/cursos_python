# VAMOS CONTAR QUANTAS PALABRAS x TEMOS NO TEXTO y

def contar_palavras(file,palavra):
    with open(file, 'r') as f_obj:
        arquivo = f_obj.read()
        total = arquivo.lower().count(palavra)
        print(f'\n\tNo arquivo "{file}", a palavra "{palavra}", aparece "{total}" vezes.')

files = input(f'\nDigite o nome do(s) arquivo(s): ').split()
palavra = input(f'\nDigite a palavra a ser procurada no texto: ')
for file in files:
    contar_palavras(file,palavra)
            