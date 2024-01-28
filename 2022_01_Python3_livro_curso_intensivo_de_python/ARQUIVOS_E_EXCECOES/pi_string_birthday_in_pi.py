# LER O ARQUIVO pi_digits.txt

print(f'MOSTRA CONTEUDO DO ARQUIVO SEM ESPACOS:')
file_path = '/home/julio/Documentos/git/LivroCursoIntensivoDePython/ARQUIVOS_E_EXCECOES/pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''                          # CRIA VARIAVEL VAZIA

for line in lines:                      # AGREGA A LISTA line REMOVENDO ESPAÇOS COM rstrip()
    pi_string += line.rstrip()

birthday = input('Entre com seu aniversário no formato mmddyy: ')
if birthday in pi_string:
    print('Sua data de aniversário aparece no primeiro milhão de digitos de pi!')
else:
    print('Sua data de aniversário não aparece no primeiro milhão de digitos de pi')

    