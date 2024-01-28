# CONCATENAÇÃO = ESCREVEMOS MAIS INFORMAÇÕES NO ARQUIVO ALÉM DAS QUE JÁ ESTÃO

filename = '/home/julio/Documentos/git/LivroCursoIntensivoDePython/ARQUIVOS_E_EXCECOES/programming.txt'
with open(filename, 'a') as file_object:                                      # ABRIR O ARQUIVO filename COMO ESCRITA w 
    file_object.write("I also love finding meaning in large datasets.\n")     # ESCREVER NO ARQUIVO I love program
    file_object.write("I love creating apps that can run in a browser\n")

with open(filename) as file_object:
    arquivo = file_object.read()
    print(arquivo)
