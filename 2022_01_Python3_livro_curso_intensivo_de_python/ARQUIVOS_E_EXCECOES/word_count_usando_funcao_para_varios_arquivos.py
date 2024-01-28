# DEFININDO UMA FUNÇÃO
from fileinput import filename


def count_words(file):
    filename = ('/home/julio/Documentos/git/LivroCursoIntensivoDePython/ARQUIVOS_E_EXCECOES/' + file)
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print(f'\n\t- Desculpe, Arquivo "{filename}" inexistente!')
    else:
        # Conta o numero aproximado de palavras no arquivo
        palavras = contents.split()
        num_palavras = len(palavras)
        print(f'\n\t- A quantidade de palavras no livro "{file}" é: {str(num_palavras)} \n')

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'acasadepapel.txt']
for file in filenames:
    count_words(file)