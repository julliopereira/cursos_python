### MODICIFICAÇÃO DE VALORES

from ctypes import alignment


alien_0 = {'cor': 'verde'}
print('O alien é ' + alien_0['cor'] + '. \n')

alien_0 = {'cor': 'amarelo'}
print('O alien AGORA é ' + alien_0['cor'] + '. \n')

### ---------------------------------------------------------------------------------
### MONITORANDO POSIÇÃO DO ALIENIGENA
print('-'*50)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}        # SOBREESCREVER O DICIONÁRIO ANTERIOR alien_0

print('Posição original ' + str(alien_0['x_position']) + '. \n' )       # MOVE ALIENIGENA PARA DIREITA DE ACORDO COM VELOCIDADE

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

### A NOVA POSIÇÃO É A POSIÇÃO ANTIGA SOMADA AO INCREMENTO

alien_0['x_position'] = alien_0['x_position'] + x_increment 

print('Nova posição: ' + str(alien_0['x_position']) + '. \n')

### VAMOS ALTERAR O VALOR DA VELOCIDADE
print('-'*50)

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment 

print('Nova posição: ' + str(alien_0['x_position']) + '. \n')



### REMOVENDO PAREDE chave-valor
print('-'*50)

print(alien_0)
del alien_0['x_position']                       # REMOVENDO A CHAVE x_position
print(alien_0,'\n')