"""while/else"""
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]
    print(letra)
    i += 1
else:
    print('O else foi executado.')      # quando o laço é finalizado o else é mostrado
                                        # se o laço for interrompido com break (exemplo) o else
                                        # nao é mostrado
print('fora do while')
