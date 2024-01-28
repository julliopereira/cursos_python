import tkinter as tk


root = tk.Tk()


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_de_tela()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de clientes")     # nome da janela
        self.root.configure(background='#251024')   # cor de fundo
        self.root.geometry("700x568")               # tamanho da janela
        self.root.resizable(True, True)             # impedir aumento eixo X ou Y
        self.root.maxsize(width=900, height=700)    # limites max X e Y
        self.root.minsize(width=400, height=300)    # limites min X e Y

    def frames_de_tela(self):
        self.frame_1 = tk.Frame(self.root, bd=4, bg='gray', 
                                highlightbackground='#AAAAAA', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = tk.Frame(self.root, bd=4, bg='gray', 
                                highlightbackground='#AAAAAA', highlightthickness=3)        
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

Application()
