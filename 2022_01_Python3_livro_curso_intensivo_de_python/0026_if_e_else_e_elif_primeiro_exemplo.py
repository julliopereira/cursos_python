### CONDICIONAL if e else

from cairo import CairoError


carros = ['audi', 'bmw', 'subaru', 'toyota']        # LISTA

for carro in carros:                                # PARA CARRO EM CARROS
    if carro == 'bmw':                              # SE CARRO IGUAL BMW
        print(carro.upper())                        # MOSTRE BMW COM TODAS AS LETRAS MAIUSCULAS
    else:                                           # SE NÃO ...
        print(carro.title())                        # MOSTRE A LISTA COM PRIMEIRA LETRA MAIUSCULA


### CONDICIONAL if , elif 
print('-'*50)
carros = ['audi', 'bmw', 'subaru', 'toyota']        # LISTA

for carro in carros:                                # PARA CARRO EM CARROS
    if carro == 'bmw':                              # SE CARRO IGUAL BMW
        print(carro.upper())                        # MOSTRE BMW COM TODAS AS LETRAS MAIUSCULAS
    elif carro == 'audi':                           
        print(carro.title()) 
    elif carro == 'subaru':                                          
        print(carro.title())   


### CONDICIONAL if , elif e else
print('-'*50)
carros = ['audi', 'bmw', 'subaru', 'toyota']        # LISTA

for carro in carros:                                # PARA CARRO EM CARROS
    if carro == 'bmw':                              # SE CARRO IGUAL BMW
        print(carro.upper())                        # MOSTRE BMW COM TODAS AS LETRAS MAIUSCULAS
    elif carro == 'audi':                           
        print(carro.title()) 
    elif carro == 'subaru':                                          
        print(carro.title()) 
    else:                                           # SE NENHUM VALOR ACIMA FOR ATENDIDO ENTAO MOSTRE O VALOR NA VARIAVEL carro
        print(carro.title())                      