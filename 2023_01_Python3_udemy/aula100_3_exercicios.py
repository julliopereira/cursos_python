# Exercicios
# 1. Aumente os preços dos produtos a seguir em 10%
# 2. Gere novos produtos por deep copy (cópia profunda)
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90}, 
]

# 3. Ordene os produtos por nome decrescente (do maior para o menor)
# 4. Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# 5. Ordene os produtos por preco crescente (do menor para o maior)
# 6. Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


# 1
produtos[0]['preco'] = int(produtos[0]['preco'] * 1.10)
#print(*produtos, sep='\n')

# 2
novos_produtos = [copy.deepcopy(produto) for produto in produtos]
novos_produtos[0]['nome'] = 'Produto 6'
novos_produtos[0]['preco'] = 15.00
novos_produtos[1]['nome'] = 'Produto 7'
novos_produtos[1]['preco'] = 21.00
novos_produtos[2]['nome'] = 'Produto 8'
novos_produtos[2]['preco'] = 21.55
novos_produtos[3]['nome'] = 'Produto 9'
novos_produtos[3]['preco'] = 17.00
novos_produtos[4]['nome'] = 'Produto 10'
novos_produtos[4]['preco'] = 18.00
#print(*novos_produtos, sep='\n')

# 3
lista_ordenada_crescente = sorted(produtos, key=lambda x: x['nome'])
# print(*lista_ordenada_crescente, sep='\n')
produtos_ordenados_por_nome = [copy.deepcopy(produto) for produto in lista_ordenada_crescente]



lista_ordenada_decrescente = sorted(produtos, key=lambda x: x['preco'], reverse=True)
#print(*lista_ordenada_decrescente, sep='\n')
produtos_ordenados_por_preco = [copy.deepcopy(produto) for produto in lista_ordenada_decrescente]


print(*produtos_ordenados_por_nome, sep='\n')
print(*produtos_ordenados_por_preco, sep='\n')

