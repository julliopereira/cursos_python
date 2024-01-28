### SOLICITA NOME DO PARTICIPANTE E UMA RESPOSTA ; USAR FLAG 


responses = {}

polling_active = True

while polling_active:                                                   # ENQUANTO VERDADEIRO
    nome = input('\nQual é o seu nome? : ')
    response = input('você gostaria de escalar qual montanha? : ')
    responses[nome] = response                                          # ADICIONA A RESPOSTA (value) NA CHAVE (key) NOME
    repeat = input('\nVocê quer que outra pessoa responda? [si/no]')
    if repeat == 'no':
        polling_active = False

print('\n--- POOL RESULTS ---')
for k, v in responses.items():                                          
    print(k.title() + ' gostaria de escalar o ' + v.title())