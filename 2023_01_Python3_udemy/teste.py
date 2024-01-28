
# import os
# import subprocess as sp

# # print(os.name)
# # print(os.getpgrp())
# # print(os.uname())

# if os.name == 'posix':
#     retorno_ping = os.system('ping -c 1 -i 0.2 -W 1 10.0.2.58 > /dev/null')
#     hostname = sp.check_output('hostnamectl').decode('utf-8')

#     if retorno_ping == 0:
#         print('Ping OK !')
#     else:
#         print('Não pinga !')

#     linhas = hostname.split('\n')
#     for linha in linhas:
#         if 'hostname' in linha:
#             linha = linha.split()
#             print(linha[-1])

#     hostname2 = sp.check_output('hostname').decode('utf-8')
#     print(f'Hostname é: {hostname2}')

#-------------------------------------

# from tkinter import *
# from tkinter import ttk

# root = Tk()
# root.title('teste')
# frm = ttk.Frame(root, padding=20)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
# root.mainloop()

#-------------------------------------
# import requests

# def pega_cotacao():
#     requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#     requisicao_dic = requisicao.json()

#     cotacao_dolar = requisicao_dic['USDBRL']['bid']
#     cotacao_euro = requisicao_dic['EURBRL']['bid']
#     cotacao_btc = requisicao_dic['BTCBRL']['bid']

#     texto = f'''
#     Dólar: {cotacao_dolar}
#     Euro: {cotacao_euro}
#     BTC: {cotacao_btc}
#     '''

#     print(texto)

# pega_cotacao()

#-------------------------------------
# import tkinter as tk

# def submit_form():
#     ipv4 = ipv4_entry.get()
#     ipv6 = ipv6_entry.get()
#     result_text.insert(tk.END, f"{ipv4}\n")
#     result_text.insert(tk.END, f"{ipv6}\n")

# root = tk.Tk()
# root.title("Formulário de Endereços IP")

# # Label e Entry para o endereço IPv4
# ipv4_label = tk.Label(root, text="IPv4:")
# ipv4_label.pack()
# ipv4_entry = tk.Entry(root)
# ipv4_entry.pack()

# # Label e Entry para o endereço IPv6
# ipv6_label = tk.Label(root, text="IPv6:")
# ipv6_label.pack()
# ipv6_entry = tk.Entry(root)
# ipv6_entry.pack()

# # Botão de envio do formulário
# submit_button = tk.Button(root, text="Enviar", command=submit_form)
# submit_button.pack()

# # Campo de texto para exibir o resultado
# result_text = tk.Text(root, height=15, width=50)
# result_text.pack()

# root.mainloop()

#-------------------------------------

# dicionários:

# Criando um dicionário vazio
# anel = {
#     'anel1': ['um', 'dois', 'tres'],
#     'anel2': ['quatro', 'cinco', 'seis'] 
# }

# for ky, val in anel.items():
#     print(f'item: {ky} :')
#     for v in enumerate(val):
#         print(f'\tvalor: {v}')

#-------------------------------------

# agregadores:

# asr9k = {
#     'EQUIPAMENT1K001': {'anel001': 'Ten0/0/0/1'},
#     'EQUIPAMENT1K002': {'anel001': 'Ten0/0/0/1'},
#     'EQUIPAMENT2K001': {'anel002': 'Ten0/0/0/2'},
#     'EQUIPAMENT2K002': {'anel002': 'Ten0/0/0/2'}
# }

# for equipamento, anel in asr9k.items():
#     print(f'equipamento: {equipamento}')
#     for nome, interface in anel.items():
#         print(f'\tanel: {nome}')
#         print(f'\t\tinterface: {interface}')

# import sys as s
# import math as mtm

# lista = (n for n in range(20000))
# print(s.getsizeof(lista))
# for n in lista:
#     print(n)
# print(f'pi: {mtm.pi:.2f}')


# import sys
# print(sys.platform)

# arquivo = 'arquivo.txt'
# with open(arquivo, "r", encoding='utf-8') as arq:
#     lista = arq.readlines()
#     print(lista)
#     for linha in lista:
#         print(linha.strip())        # remove \n da linha qeue estava na lista