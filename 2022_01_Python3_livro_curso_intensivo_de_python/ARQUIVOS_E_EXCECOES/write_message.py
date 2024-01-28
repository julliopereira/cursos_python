
filename = '/home/julio/Documentos/git/LivroCursoIntensivoDePython/ARQUIVOS_E_EXCECOES/programming.txt'
with open(filename, 'w') as file_object:              # ABRIR O ARQUIVO filename COMO ESCRITA w 
    file_object.write("I love program\n")             # ESCREVER NO ARQUIVO I love program
    file_object.write("I love creating new games\n")

with open(filename) as file_object:
    arquivo = file_object.read()
    print(arquivo)

"""

PYTHON ESCREVE SOMENTE str()
para escrever números no arquivo é necessário converter em str()

"""