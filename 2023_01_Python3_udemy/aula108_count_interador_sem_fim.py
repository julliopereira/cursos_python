# count é um interador sem fim 

from itertools import count

c1 = count()      # comecar no 10 colocar valor 10, step de 8 em 8 colocar count(10, 8)
r1 = range(100)

print('count')
for i in c1:
    if i >= 100:
        break

    print(i)

print('\n\nrange')
for i in r1:
    if i >= 100:
        break

    print(i)

