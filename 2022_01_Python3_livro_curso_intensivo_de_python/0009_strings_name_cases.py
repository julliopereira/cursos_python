### ARMAZENE O NOME DA PESSOA EM VARIAVEL E MOSTRE O CONTEUDO. MENSAGEM SIMPLES.

mensagem = "Ola Maria, quer aprender a programar em Python ?"
print(f'"{mensagem}"')

print('-'*20)
### ARMAZENE NOME DA PESSOA E MOSTRE COM LETRAS MINUSCULAS, MAIUSCULAS E PRIMEIRA LETRA MAIUSCULA

nome = 'joão andrade pessoa'
print(nome.upper())
print(nome.lower())
print(nome.title())

print('-'*20)
### CITAÇÃO DE PESSOA QUE VOCÊ ADMIRA

citacao = 'Uma pessoa que nunca cometeu um erro jamais tentou nada novo'
print(f'Albert Einstein disse uma vez: "{citacao}"')

print('-'*20)
### CITAÇÃO DE PESSOA QUE VOCÊ ADMIRA NRO 2

citacao2 = 'Não vivo as palavras bonitas das pessoas, acordo todos para viver minhas atitudes'
print(f'Eu disse assim: "{citacao2}"')

print('-'*20)
### RETIRANDO ESPAÇOS E ADICIONANDO QUEBRA DE LINHA E TABULAÇÃO

texto1 = 'Aqui um texto de primeira linha                       '
texto2 = 'Aqui um texto de segunda linha              '
print(f'{texto1.rstrip()}\n\t{texto2.strip()}')
