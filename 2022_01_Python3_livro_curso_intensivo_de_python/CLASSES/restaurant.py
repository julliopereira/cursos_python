class Restaurant():
    def __init__(self,restaurant_name,cousine_type,number_served=0):
        """Adiciona atributos para o metodo init"""
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
        self.number_served = number_served 

    def describe_restautant(self):
        """Mostra uma mensagem informando nome e tipo da cozinha do restaurante"""
        print(f'Você está no restaurante {self.restaurant_name.title()}')
        print(f'Servimos comida {self.cousine_type.title()}')

    def open_restaurant(self):
        print(f'o restaurante {self.restaurant_name.title()} está aberto!!!')

    def increment_served(self,served):
        """Incrementa pessoas a serem atendidas"""
        self.number_served += served
        

restaurant = Restaurant('bodão','fast food')                                            # VALORES COM RESTAURANTE ABRINDO
print(f'{restaurant.restaurant_name.title()} {restaurant.cousine_type.title()}')
restaurant.describe_restautant()
restaurant.open_restaurant()
print(f'Abrimos agora e temos "{restaurant.number_served}" pessoas atendidas até o momento.')

restaurant = Restaurant('bigburguer', 'hamburger', 34)                                  # 34 PESSOAS ATENDIDAS NESTE MOMENTO
print(f'Estamos servindo "{restaurant.number_served}" pessoas neste momento.')

restaurant.increment_served(2)                                                          # MAIS DUAS PESSOAS ENTRARAM PARA SEREM ATENDIDAS
print(f'Estamos servindo "{restaurant.number_served}" pessoas neste momento.')

