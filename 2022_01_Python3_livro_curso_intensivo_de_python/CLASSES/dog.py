

class Dog():
    """Uma tentativa de modelar um cachorro"""
    def __init__(self,name, age):                   # ATRIBUTOS
        """Inicializa os atributos name e age."""
        self.name = name
        self.age = age

    def sit(self):                                  # METODO
        """Simula cachorro sentando"""
        print(f'{self.name.title()} sentar!')

    def roll_over(self):                            # METODO
        """Simula cachorro rolando"""
        print(f'{self.name.title()} rolar!')

my_dog = Dog('wille', 14)                           # VARIAVEL NESTE CASO É UMA > INSTANCIA
print(f'Meu cachorro é o {my_dog.name.title()} e tem a idade de {my_dog.age} anos.')
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 3)                           # VARIAVEL NESTE CASO É UMA > INSTANCIA
print(f'\nSua calinha {your_dog.name.title()} tem {your_dog.age} anos. ')
your_dog.sit()
your_dog.roll_over()

