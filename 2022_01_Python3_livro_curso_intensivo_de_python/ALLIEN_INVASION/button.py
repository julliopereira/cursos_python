class Button():
    def __init__(self,ai_settings,screen,msg):
        """Inicializa os atributos do botão"""
        self.screen = screenself.screen_rect = screen.get_rect()  
        # Define as dimensões e as propriedades do botão 
        self.width,self.height = 200,50
        self.button_color = (0,200,0)
        self.font = pygame.font.SysFont(None, 48)
        #Constrói o objeto rect do botão e o centraliza
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        # A mensagem do botão deve ser preparada apenas uma vez
        self.prep_msg(msg)
        