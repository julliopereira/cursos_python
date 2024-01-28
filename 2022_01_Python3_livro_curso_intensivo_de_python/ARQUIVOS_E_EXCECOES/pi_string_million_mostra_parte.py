# LER O ARQUIVO pi_digits.txt

print(f'MOSTRA CONTEUDO DO ARQUIVO SEM ESPACOS:')
file_path = '/home/julio/Documentos/git/LivroCursoIntensivoDePython/ARQUIVOS_E_EXCECOES/pi_million_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''                          # CRIA VARIAVEL VAZIA

for line in lines:                      # AGREGA A LISTA line REMOVENDO ESPAÇOS COM rstrip()
    pi_string += line.rstrip()

print(f'pi: {pi_string[:52]} ...')               # MOSTRA CONTEUDO DE pi_strip (apenas 52 caracteres)
print(f'tamanho: {len(pi_string)} caracteres ')     # MOSTRA O TAMANHO DA STRING