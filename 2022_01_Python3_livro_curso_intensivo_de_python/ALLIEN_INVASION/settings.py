class Settings():
    """Uma classe para armazenar todas as configurações da invasão alienigena."""
    def __init__(self):
        """Inicializa as configurações do jogo"""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        # Configuração da espeçonave
        self.ship_speed_factor = 3
        self.ship_limit = 3
        # Configurações dos projeteis
        self.bullet_speed_factor = 3
        self.bullet_width = 4
        self.bullet_height = 18
        self.bullet_color = 60, 60, 255
        self.bullets_allowed = 3
        # Configurações dos alienígenas
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
