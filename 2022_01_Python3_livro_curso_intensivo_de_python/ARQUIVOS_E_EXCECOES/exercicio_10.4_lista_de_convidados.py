
nome = ''
while nome != 'q': 
    nome = input('Digite seu nome ou "q" para sair: ')
    if nome != 'q':
        arq = input('Digite o nome do arquivo: ')
        path = ('/home/julio/Documentos/git/LivroCursoIntensivoDePython/ARQUIVOS_E_EXCECOES/' + arq)

        with open(path, 'a') as f_obj:                      # OCAO a NAO APAGA O CONTEUDO EXISTENTE ADICIONANDO NOVOS VALORES
            f_obj.write('\t\t')
            f_obj.write(nome)                               # CONTEÚDO EM name 
            f_obj.write('\n')                               # PROXIMA LINHA

        with open(path) as file_obj:
            arquivo = file_obj.read()
            print('\n\n\tSeu nome é: \n' + arquivo.rstrip())
            print('\n')

