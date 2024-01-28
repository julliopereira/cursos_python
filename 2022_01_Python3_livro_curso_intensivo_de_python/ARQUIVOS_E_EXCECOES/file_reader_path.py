# LER O ARQUIVO pi_digits.txt

file_path = '/home/julio/Documentos/git/LivroCursoIntensivoDePython/ARQUIVOS_E_EXCECOES'
with open(file_path + '/pi_digits.txt') as file_object:      # ABRIR AQUIVO pi_digits.txt 
    contents = file_object.read()               # USAR O read() PARA LER O ARQ 
    print(contents)                             # MOSTRAR CONTEÚDO DE contents

    print('=' * 30)
#------------------------------------------------------------------------
# OUTRA FORMA DE USAR O PRINT

with open(f'{file_path}/pi_digits.txt') as file_object:      # ABRIR AQUIVO pi_digits.txt 
    contents = file_object.read()               # USAR O read() PARA LER O ARQ 
    print(contents)                             # MOSTRAR CONTEÚDO DE contents