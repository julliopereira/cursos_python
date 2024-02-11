# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


# -------- SOLUCAO JULIO ------------
# lista = []

# def lista_de_tarefas(usuario):
#     # adiciona o que foi digitado na lista
#     lista.append(usuario)

#     if lista[-1] == 'listar':
#         lista.remove(usuario)  # remove ultima posicao da lista
#         if len(lista) == 0:
#             print('Vazio')
#         else:
#             print(*lista)  # mostre itens da lista

#     elif lista[-1] == 'desfazer':
#         lista.remove(usuario)  # remove ultima posicao da lista
#         if len(lista) == 0:
#             print('Vazio')   # se nao há itens então nada a fazer
#         else:
#             global removido
#             removido = lista.pop(-1) # se há itens remove o ultimo em seguida mostra o conteudo
#             print(*lista)

#     elif lista[-1] == 'refazer':
#         lista.remove(usuario)  # remove ultima posicao da lista
#         if "removido" in globals():
#             if removido == lista[-1]:
#                 print('Nada a fazer')
#             else:
#                 lista.append(removido)
#                 print(*lista)

#         else:
#             print('Vazio')
    
#     elif lista[-1] == 'sair':
#         return False    # retorna False para finalizar loop 
    
#     else:
#         print(*lista)   # mostra a lista como esta até este momento


# while True: 
#     result = lista_de_tarefas(input("Digite itens para lista ou: listar, desfazer, refazer ou sair: "))
#     if result == False:
#         break


# ------  SOLUÇÃO PROFESSOR -------------

import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('clear')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue
