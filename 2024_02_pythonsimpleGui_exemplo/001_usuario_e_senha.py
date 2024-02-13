import PySimpleGUI as sg

# Layout da janela
layout = [
    [sg.Text("usuario:"),sg.Text(''),sg.Input(key='usuario')],
    [sg.Text("password:"),sg.Input(key='password', password_char='*')],
    [sg.Button('login')],
    [sg.Text('Aguardando entrada de dados', key='mensagem')]
]

# Criar a janela
janela = sg.Window("Autenticação",layout=layout, size=(250,150))

# Ler eventos da janela
while True:
    evento, valores = janela.read()

    # Sair do programa
    if evento == sg.WIN_CLOSED:
        break

    elif evento == 'login':
        
        # geralmente verificado usuario e password com BD, criarei um pequeno banco para checar
        senha_correta = '123456'
        usuario_correto = 'julio'
        usuario = valores['usuario'].strip()
        senha = valores['password']

        if senha == senha_correta and usuario == usuario_correto:
            janela['mensagem'].update('Login realizado com sucesso!')
        else:
            janela['mensagem'].update('Senha ou usuario invalido!')

    # Imprimir o valor do botão
    if evento == "Clique aqui":
        print(valores)

# Fechar a janela
janela.close()
