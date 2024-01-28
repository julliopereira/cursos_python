# LER O ARQUIVO pi_digits.txt

print(f'MOSTRA CONTEUDO DO ARQUIVO SEM ESPACOS:')
file_path = '/home/julio/Documentos/git/LivroCursoIntensivoDePython/ARQUIVOS_E_EXCECOES/pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''                          # CRIA VARIAVEL VAZIA

for line in lines:                      # AGREGA A LISTA line REMOVENDO ESPAÇOS COM rstrip()
    pi_string += line.rstrip()

print(pi_string)                        # MOSTRA CONTEUDO DE pi_strip
print(len(pi_string))                   # MOSTRA O TAMANHO DA STRING

pi_string = float(pi_string)            # ALTERA O TIPO PARA float
print(type(pi_string))                  # MOSTRA O TIPO DO CONTEUDO DA VARIÁVEL pi_string