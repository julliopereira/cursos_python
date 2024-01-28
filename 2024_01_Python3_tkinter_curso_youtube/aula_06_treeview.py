import tkinter as tk
from tkinter import ttk 

# iniciando uma janela tkinter
root = tk.Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_de_tela()
        self.widgets_frame1()
        self.lista_frame2()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de clientes")     # nome da janela
        self.root.configure(background='#FFFFFF')   # cor de fundo
        self.root.geometry("700x568")               # tamanho da janela
        self.root.resizable(True, True)             # impedir aumento eixo X ou Y
        self.root.maxsize(width=900, height=700)    # limites max X e Y
        self.root.minsize(width=580, height=450)    # limites min X e Y

    def frames_de_tela(self):
        self.frame_1 = tk.Frame(self.root, bd=4, bg='#0E5AE5', 
                                highlightbackground='#AAAAAA', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = tk.Frame(self.root, bd=4, bg='#0E5AE5', 
                                highlightbackground='#AAAAAA', highlightthickness=3)        
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        # Criação de botoes
        self.bt_limpar = tk.Button(self.frame_1, text='limpar', bd=3, bg='#C581EA',
                                    fg='white', font=('verdana', 8, 'bold'))    # botao dentro do frame_1
        self.bt_limpar.place(relx=0.18, rely=0.09 , relwidth=0.1, relheight=0.1)

        self.bt_buscar = tk.Button(self.frame_1, text='buscar', bd=3, bg='#C581EA',
                                    fg='white', font=('verdana', 8, 'bold'))    # botao dentro do frame_1
        self.bt_buscar.place(relx=0.31, rely=0.09 , relwidth=0.1, relheight=0.1)

        self.bt_novo = tk.Button(self.frame_1, text='novo', bd=3, bg='#C581EA',
                                    fg='white', font=('verdana', 8, 'bold'))    # botao dentro do frame_1
        self.bt_novo.place(relx=0.60, rely=0.09, relwidth=0.1, relheight=0.1)

        self.bt_alterar = tk.Button(self.frame_1, text='alterar', bd=3, bg='#C581EA',
                                    fg='white', font=('verdana', 8, 'bold'))    # botao dentro do frame_1
        self.bt_alterar.place(relx=0.73, rely=0.09 , relwidth=0.1, relheight=0.1)

        self.bt_apagar = tk.Button(self.frame_1, text='apagar', bd=3, bg='#C581EA',
                                    fg='white', font=('verdana', 8, 'bold'))    # botao dentro do frame_1
        self.bt_apagar.place(relx=0.86, rely=0.09 , relwidth=0.1, relheight=0.1)

        # Criação da label e entrada do codigo
        self.lb_codigo = tk.Label(self.frame_1, text="Código",
                                   bg='#0E5AE5', fg='white', font=('verdana', 9, 'bold'))
        self.lb_codigo.place(relx=0.02, rely=0.0003)

        self.cod_entry = tk.Entry(self.frame_1, bg='lightgray')
        self.cod_entry.place(relx=0.02, rely=0.09, relwidth=0.14, relheight=0.1)

        # Criação da label e entrada do codigo
        self.lb_nome = tk.Label(self.frame_1, text="Nome",
                                   bg='#0E5AE5', fg='white', font=('verdana', 9, 'bold'))
        self.lb_nome.place(relx=0.02, rely=0.3)

        self.nom_entry = tk.Entry(self.frame_1)
        self.nom_entry.place(relx=0.02, rely=0.4, relwidth=0.88, relheight=0.1)

        # Criação da label e entrada do telefone
        self.lb_telefone = tk.Label(self.frame_1, text="Telefone",
                                   bg='#0E5AE5', fg='white', font=('verdana', 9, 'bold'))
        self.lb_telefone.place(relx=0.02, rely=0.55)

        self.tel_entry = tk.Entry(self.frame_1)
        self.tel_entry.place(relx=0.02, rely=0.65, relwidth=0.4, relheight=0.1)

        # Criação da label e entrada da cidade
        self.lb_cidade = tk.Label(self.frame_1, text="Cidade",
                                   bg='#0E5AE5', fg='white', font=('verdana', 9, 'bold'))
        self.lb_cidade.place(relx=0.5, rely=0.55)

        self.cid_entry = tk.Entry(self.frame_1)
        self.cid_entry.place(relx=0.5, rely=0.65, relwidth=0.4, relheight=0.1)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, 
                                     height=3, 
                                     columns=('col1','col2','col3','col4'))    # lista clientes
        self.listaCli.heading('#0', text="")
        self.listaCli.heading('#1', text="Código")
        self.listaCli.heading('#2', text="Nome")
        self.listaCli.heading('#3', text="Telefone")
        self.listaCli.heading('#4', text="Cidade")

        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=125)
        self.listaCli.column('#4', width=125)

        self.listaCli.place(relx=0.01, rely=0.03, relwidth=0.98, relheight=0.93)

        self.scrollLista = ttk.Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.95, rely=0.03, relwidth=0.05, relheight=0.93)
Application()
