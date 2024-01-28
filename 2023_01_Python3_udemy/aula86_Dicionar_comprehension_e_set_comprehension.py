# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Canela Azul',
    'preco': '2.5',
    'categora': 'Escritório',
}

dc = {
    chave: valor 
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor in produto.items()
}

print(dc)

