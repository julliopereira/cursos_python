### A FUNÇÃO input() É UTILIZADA PARA SOLICATAR UMA ENTRADA DO USUÁRIO
### UTILIZAMOS UMA VARIÁVEL PARA GUARDAR O VALOR DIGITADO PELO USUÁRIO

variavel = input('Digite qualquer coisa: ')             # SOLICITA AO USUARIO UMA ENTRADA E GUARDA NA VARIAVEL variavel
print(type(variavel))

### A FUNÇÃO input() COLETA O A ENTRADA DO USUARIO SEMPRE EM STRING srt() E PARA TRANSFORMAR EM NUMERO USAMOS int() 
print('-'*50)

variavel1 = int(input('Digite variavel 1: '))           # UMA FORMA DE UTILIZAR É ASSOCIAR A VARIVEL NA ENTRADA
print(type(variavel1))                                  # FUNÇÃO type() MOSTRA O TIPO DA VARIAVEL str ou int ou float etc...

variavel2 = input('Digite variavel2: ')                 
print(int(variavel2))                                   # OUTRA FORMA É ALTERAR NA SAÍDA

if variavel >= 0:                                      # COMO ESTÁ COMPARANDO NUMEROS E O VALOR DE variavel É STRING VAMOS TER UM ERRO DE TYPEERR7
    print(variavel)                                     # PARA ARRUMAR ISSO VÁ EM IF E ALTERE PARA int(variavel) >= 10