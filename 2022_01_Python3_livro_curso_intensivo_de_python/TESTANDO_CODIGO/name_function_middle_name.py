# PROGRAMA SIMPLES QUE MOSTRA UM NOME E SOBRENOME DE FORMA ELEGANTE

def get_formatted_name(first, last, middle=''):                    # NOME DO MEIO OPCIONAL (SE NAO OPCIONAL O CODIGO DÁ ERRO)
    """Gera um nome completo formatado de forma elegante"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()


