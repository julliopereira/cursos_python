### classe EletricCar

class Car():                                                                            # CLASSE PAI
    """Descrever um carro"""
    def __init__(self,fabrica,modelo,ano):
        """inicializa atributos que identificam um carro"""
        self.fabrica = fabrica
        self.modelo = modelo
        self.ano = ano
        self.odometro_lido = 0

    def nome_adaptado(self):
        """Exibe informações do meu novo carro"""
        print(f'{self.fabrica.title()} {self.modelo.title()} {self.ano}')

    def ler_odometro(self):
        """Exibe frase que mostra kilometragem do carro"""
        print(f'Este carro tem {self.odometro_lido} km.')

    def kilometragem_atualizada(self, kilometragem):
        """Incrementa valor da kilometragem"""
        if kilometragem >= self.odometro_lido:
            self.odometro_lido += kilometragem
        else:
            print(f'**Você não pode voltar a kilometragem')

class EletricCar(Car):                                                                 # CLASSE FILHA
    """Nova class para definição de carros elétricos"""
    def __init__(self, fabrica, modelo, ano):
        """Importar os atributos da classe pai Car utilizando o metrodo super()"""
        super().__init__(fabrica, modelo, ano)

#---------------------------------
"""
carro_eletrico = EletricCar('tesla', 'model s', 2017)
carro_eletrico.nome_adaptado()
"""