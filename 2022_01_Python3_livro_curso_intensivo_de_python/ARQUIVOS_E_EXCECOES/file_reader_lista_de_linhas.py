# LER O ARQUIVO pi_digits.txt

print(f'MOSTRA CONTEUDO DO ARQUIVO SEM ESPACOS:')
file_path = '/home/julio/Documentos/git/LivroCursoIntensivoDePython/ARQUIVOS_E_EXCECOES'
with open(file_path + '/pi_digits.txt') as file_object:           # ABRIR AQUIVO pi_digits.txt 
    lines = file_object.readlines()                               # ARMAZENA CADA LINHA DE ARQUIVO EM UMA LISTA

print(lines)                                                      # MOSTRA A LISTA COMPLETA

for line in lines:
    print(line.rstrip())                                          # MOSTRAR CONTEÚDO DE line SEM ESPACOS