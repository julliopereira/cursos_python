
'''
Assuntos:

append
insert
del
pop
remove
'''

#from numpy import append


#from numpy import insert


motorcycles = []                                            # CRIANDO LISTA SEM VALORES
print(motorcycles)

print('-'*50) #---------------------------------------------------
motorcycles.append('honda')                                 # ADICIONA PRIMEIRO VALOR À LISTA
motorcycles.append('yamaha')                                # ADICIONA SEGUNDO VALOR À LISTA
motorcycles.append('suzuki')                                # ADICIONA TERCEIRO VALOR À LISTA                              
print(motorcycles)

print('-'*50) #---------------------------------------------------
motorcycles[0] = 'ducati'                                   # TROCANDO O PRIMEIRO VALOR DA LISTA NA POSIÇÃO 0 PARA ducati
print(motorcycles)

print('-'*50) #---------------------------------------------------
motorcycles.append('honda')                                 # ADICIONANDO O VALOR honda NO FINAL DA LISTA
print(motorcycles)

print('-'*50) #---------------------------------------------------
motorcycles.insert(0, 'bmw')                                # INSERE O VALOR bmw NO NA POSICAO 0 DESLOCANDO O RESTANTE DE VALORES 
print(motorcycles)

print('-'*50) #---------------------------------------------------
del motorcycles[0]                                          # REMOVENDO VALOR DA LISTA NA POSICAO 0 
print(motorcycles)

print('-'*50) #---------------------------------------------------
poped_motorcycles = motorcycles.pop()                       # FAZEMOS POP DE UM ITEM DA LISTA (REMOVE DA LISTA) E ARMAZENAMOS O VALOR RETIRADO NA VARIAVEL 
print(motorcycles)
print(poped_motorcycles)

print('-'*50) #---------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
ultimo_dono = motorcycles.pop()
print('Ultima moto que eu tive foi ' + ultimo_dono.title() + '.')
print(motorcycles)
motorcycles.append(ultimo_dono)
print(motorcycles)

print('-'*50) #---------------------------------------------------
moto = motorcycles.pop(0)                                   # REMOVENDO VALOR NA POSIÇÃO 0 E ADICIONANDO NA VARIAVEL moto
print('A primeira moto que tive foi ' + moto.title() + '!.')
motorcycles.append(moto)
print(motorcycles)

print('-'*50) #---------------------------------------------------
motorcycles.append('ducatti')
print(motorcycles)
motorcycles.remove('ducatti')                               # REMOVER ITEM PELO NOME (remove apenas a primeira ocorrencia que achar)
print(motorcycles)
