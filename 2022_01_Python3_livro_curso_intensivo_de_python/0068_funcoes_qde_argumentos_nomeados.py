### ADICIONA ATRIBUTOS OU INFORMACOES DIVERSAS DE TAMANHO INDEFINIDO

def build_profile(first, last, **user_info):                    # **user_info - CRIA UM DICIONARIO VAZIO 
    """Controi um dicionario com tudo o que sabemos do usuario"""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'eistein', local='alemanha', atuacao='fisico', descoberta='relatividade')
print(user_profile)