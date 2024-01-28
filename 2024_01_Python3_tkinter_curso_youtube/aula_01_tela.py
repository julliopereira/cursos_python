import tkinter as tk

root = tk.Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de clientes")     # nome da janela
        self.root.configure(background='#251024')   # cor de fundo
        self.root.geometry("800x")               # tamanho da janela
        self.root.resizable(True, True)             # impedir aumento eixo X ou Y
        self.root.maxsize(width=900, height=1000)    # limites max X e Y
        self.root.minsize(width=400, height=400)    # limites min X e Y

Application()
