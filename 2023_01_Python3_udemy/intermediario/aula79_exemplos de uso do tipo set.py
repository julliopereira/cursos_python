# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra)                           #adiciona letra digitada em letras

    if 'l' in letras:
        print(f'Você acertou a letra (l)')      #mostra mensagem para usuario que acertou letra l e finaliza
        break
        
    print(letras)