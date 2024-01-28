# CONCATENAÇÃO = ESCREVEMOS MAIS INFORMAÇÕES NO ARQUIVO ALÉM DAS QUE JÁ ESTÃO

lista = [ '01', '02', '03' ]
filename = '/home/julio/Documentos/git/LivroCursoIntensivoDePython/ARQUIVOS_E_EXCECOES/concatenando2.txt'
with open(filename, 'a') as file_object:                                      # ABRIR O ARQUIVO filename COMO ESCRITA w 
    #file_object.write("I also love finding meaning in large datasets.\n")     # ESCREVER NO ARQUIVO I love program
    #file_object.write("I love creating apps that can run in a browser\n")
    file_object.write(str(lista))

with open(filename) as file_object:
    arquivo = file_object.read()
    print(arquivo)
