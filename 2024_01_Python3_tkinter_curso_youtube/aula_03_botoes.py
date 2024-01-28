import tkinter as tk

root = tk.Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_de_tela()
        self.criando_botoes()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de clientes")     # nome da janela
        self.root.configure(background='#251024')   # cor de fundo
        self.root.geometry("700x568")               # tamanho da janela
        self.root.resizable(True, True)             # impedir aumento eixo X ou Y
        self.root.maxsize(width=900, height=700)    # limites max X e Y
        self.root.minsize(width=580, height=450)    # limites min X e Y

    def frames_de_tela(self):
        self.frame_1 = tk.Frame(self.root, bd=4, bg='gray', 
                                highlightbackground='#AAAAAA', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = tk.Frame(self.root, bd=4, bg='gray', 
                                highlightbackground='#AAAAAA', highlightthickness=3)        
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def criando_botoes(self):
        # Criando botao limpar
        self.bt_limpar = tk.Button(self.frame_1, text='limpar')    # botao dentro do frame_1
        self.bt_limpar.place(relx=0.05, rely=0.02 , relwidth=0.1, relheight=0.07)

        self.bt_buscar = tk.Button(self.frame_1, text='buscar')    # botao dentro do frame_1
        self.bt_buscar.place(relx=0.18, rely=0.02 , relwidth=0.1, relheight=0.07)

        self.bt_novo = tk.Button(self.frame_1, text='novo')    # botao dentro do frame_1
        self.bt_novo.place(relx=0.60, rely=0.02 , relwidth=0.1, relheight=0.07)

        self.bt_alterar = tk.Button(self.frame_1, text='alterar')    # botao dentro do frame_1
        self.bt_alterar.place(relx=0.73, rely=0.02 , relwidth=0.1, relheight=0.07)

        self.bt_apagar = tk.Button(self.frame_1, text='apagar')    # botao dentro do frame_1
        self.bt_apagar.place(relx=0.86, rely=0.02 , relwidth=0.1, relheight=0.07)

Application()
