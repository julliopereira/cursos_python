### INCREMENTANDO VALOR DE ATRIBUTO COM MÉTODO

class Car:
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

"""
meu_novo_carro = Car('hynday', 'hb20', 2013)
meu_novo_carro.nome_adaptado()
meu_novo_carro.ler_odometro()                               # ALTERAMOS O VALOR DA KILOMETRAGEM DO CARRO AO SAIR DA CONCESSIONARIA 

meu_novo_carro.kilometragem_atualizada(43)                  # VAMOS ALTERAR AGORA A KILOMETRAGEM DO CARRO PARA 43 KM
meu_novo_carro.ler_odometro()                               # E MOSTRAR NOVAMENTE COM VALOR ATUALIZADO

meu_novo_carro.kilometragem_atualizada(23)                  # VAMOS TENTAR BAIXAR AGORA A KILOMETRAGEM DO CARRO PARA 23 KM
meu_novo_carro.ler_odometro()                               # E MOSTRAR NOVAMENTE COM VALOR 
"""
