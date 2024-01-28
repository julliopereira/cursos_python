# LER O ARQUIVO pi_digits.txt

with open('pi_digits.txt') as file_object:      # ABRIR AQUIVO pi_digits.txt 
    contents = file_object.read()               # USAR O read() PARA LER O ARQ 
    print(contents)                             # MOSTRAR CONTEÚDO DE contents

print('=' * 30)
#------------------------------------------------------------------------
# LER O ARQUIVO pi_digits.txt REMOVENDO ESPAÇOS A DIREITA USANDO rstrip()

with open('pi_digits.txt') as file_object:      # ABRIR AQUIVO pi_digits.txt 
    contents = file_object.read()               # USAR O read() PARA LER O ARQ 
    print(contents.rstrip())                    # MOSTRAR CONTEÚDO DE contents




