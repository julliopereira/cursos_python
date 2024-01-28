# UTILIZANDO NOTAÇÃO DE FATIAMENTO [:] PARA COPIAR UMA LISTA NÃO ALTERANDO A ORIGINAL

def print_models(unprinted_designs, completed_models):
    """Simula a impressão de cada design, até que não haja mais nenhum"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Imprimindo modelo: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Mostra todos os mmodelos impressos."""
    print("\nO seguinte modelo tem sido impresso:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:],completed_models)   ### UTILIZANDO FATIAMENTO DE unprinted_designs
show_completed_models(completed_models)

print(f'\nLISTA ORIGINAL {unprinted_designs}')