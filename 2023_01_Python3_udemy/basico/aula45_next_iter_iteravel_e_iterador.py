"""
Iterável -> str, range, etc   (__iter__)
Iterador -> quem sabe entregar um valor por vez
next     -> me entregue o próximo valor
iter     -> me entregue seu terador

---como o for funciona---

"""

# texto = iter('Luiz')    #__iter__()

# print(next(texto))          # mostra letra L
# print(next(texto))          # mostra letra u
# print(next(texto))          # mostra letra i

# print(next(texto))          # mostra letra z

# print('-'*10)


# for letra in texto 
texto = 'Julio'             # iteravel
iterador = iter(texto)      # iterador

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break