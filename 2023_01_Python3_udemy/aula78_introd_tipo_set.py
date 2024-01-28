# Sets - Conjuntos em Python (tipo set)
# Conjuntos sáo ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas 
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

# s1 = set('')                # vazio
# print(s1, type(s1))

# s2 = {'Julio', 1, 2, 3}     # com dados
# print(s2)

# Sets são eficientes para remover valores duplicados 
# de iteráveis. 
# - eles náo tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)

# s1 = {1, 2, 3, 4, 5, 6, 6, 6, 6, 3, 3, 3, 1, 2}
# print(s1)

# Métodos úteis:
# add, update, clear, discard

# s1 = set()
# s1.add('Julio')
# s1.add(1)
# s1.update(('Olá mundo', 1, 2, 3, 4))
# # s1.clear
# s1.discard('Olá mundo')
# s1.discard('Julio')
# print(s1)

# Operadores úteis:
# união | uniao (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2            # unir
s3 = s1 & s2            # interseccao - presente em ambos
s3 = s1 - s2            # diferenca
s3 = s1 ^ s2            # nao estao em ambos
print(s3)
