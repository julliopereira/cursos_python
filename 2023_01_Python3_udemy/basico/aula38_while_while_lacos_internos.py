"""
Repeticoes
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quanto um código não tem fim 
"""

qde_linhas = 5
qde_colunas = 5

linha = 1
while linha <= qde_linhas:
    coluna = 1


    while coluna <= qde_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1

    linha += 1

print('Acabou')