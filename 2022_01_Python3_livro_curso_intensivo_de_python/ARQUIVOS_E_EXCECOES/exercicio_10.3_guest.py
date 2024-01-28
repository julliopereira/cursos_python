# ESCREVER UM PROGRAMA QUE PEÇA O NOME DO USUARIO E GRAVE NO ARQUIVO CHAMADO guest.txt

nome = input('Digite seu nome: ')
arq = input('Digite o nome do arquivo: ')
path = ('/home/julio/Documentos/git/LivroCursoIntensivoDePython/ARQUIVOS_E_EXCECOES/' + arq)

with open(path, 'a') as f_obj:                      # OCAO a NAO APAGA O CONTEUDO EXISTENTE ADICIONANDO NOVOS VALORES
    f_obj.write('\t\t')
    f_obj.write(nome)                               # CONTEÚDO EM name 
    f_obj.write('\n')                               # PROXIMA LINHA

with open(path) as file_obj:
    arquivo = file_obj.read()
    print('\n\n\tSeu nome é: \n' + arquivo.rstrip())


