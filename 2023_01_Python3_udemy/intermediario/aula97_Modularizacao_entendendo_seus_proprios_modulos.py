'''
Entendendo os seus próprios módulos Python
o primeiro módulo executado chama-se __main__
Você pode importar outro módulo inteiro ou parte do módulo
O python conhece a pasta onde o __main__ está e as pastas abaixo dele.
Ele não reconhece pastas e módulos acima do __main__ por padrão
O python conhece todos os módulos e pacotes presentes nos 
caminhos de sys.path
'''
# import sys
import aula97_m
from aula97_m import variavel_modulo,soma

# print('Este módulo se chama', __name__)
# print(*sys.path, sep='\n')

print(aula97_m.variavel_modulo)
print(soma(5, 6))