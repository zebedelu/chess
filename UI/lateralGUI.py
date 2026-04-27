import pygame, random

class GUI(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game

        self.image = pygame.Surface((self.game.telasize[0]-self.game.telasize[1],self.game.telasize[1]))

        perfis_imagens = ["player1.png", "player2.png", "player3.png", "player4.png"]
        random.shuffle(perfis_imagens)
        self.perfil1_nome_arquivo = perfis_imagens[1]
        self.perfil2_nome_arquivo = perfis_imagens[0]

    def update(self):
        self.image.fill((185, 122, 87))

        # Degrade (para o jogador que está na vez)
        self.degrade = pygame.Surface((100,800), pygame.SRCALPHA)
        
        if self.game.timeJogando == 1:
            for y in range(800,200,-1):
                pygame.draw.rect(self.degrade, (100,255,100, max(200-((800-y)/2.3), 0)), (0,y,100,1))
        else:
            for y in range(0,600):
                pygame.draw.rect(self.degrade, (100,255,100, max(200-(y/2.3), 0)), (0,y,100,1))

        self.image.blit(self.degrade, (0,0))

        # Parte dos textos (Nomes)
        fonte = pygame.font.SysFont("Arial", 25, True)
        player1_texto_nome = pygame.Font.render(fonte, "player2", False, (0,0,0))
        player2_texto_nome = pygame.Font.render(fonte, "player1", False, (0,0,0))
        self.image.blit(player1_texto_nome, (7,10))
        self.image.blit(player2_texto_nome, (7,745))

        # Parte das imagens de perfil
        image1 = pygame.image.load("assets/profiles/"+self.perfil1_nome_arquivo).convert_alpha()
        image2 = pygame.image.load("assets/profiles/"+self.perfil2_nome_arquivo).convert_alpha()
        self.image.blit(image1, (18,50))
        self.image.blit(image2, (18,670))
    
    def draw(self):
        self.game.tela.blit(self.image, (800,0))