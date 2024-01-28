# CONTAR QUANTIDADE DE PALABRAS NO TEXTO DO ARQUIVO alice.txt

filename = '/home/julio/Documentos/git/LivroCursoIntensivoDePython/ARQUIVOS_E_EXCECOES/alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print(f'\n\t- Desculpe, Arquivo "{filename}" inexistente!')