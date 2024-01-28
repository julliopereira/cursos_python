# isinstance() - para saber se objeto é de determinado tipo

lista = ['a',1,1.1,True,[0,1,2],(1,2),{0,1},{'nome': 'Julio'}]

for obj in lista:
    if isinstance(obj, set):
        obj.add(7)
        print(obj)

    if isinstance(obj, str):
        print(obj.upper())

    if isinstance(obj, (int,float)):
        print(obj * 5)

        