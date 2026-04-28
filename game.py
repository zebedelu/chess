import pygame
from pieces.peao import Peao
from pieces.torre import Torre
from pieces.bispo import Bispo
from pieces.cavalo import Cavalo
from pieces.rainha import Rainha
from pieces.rei import Rei
from UI.background import Background
from UI.lateralGUI import GUI

from rules.check import check

class Game:
    def __init__(self):
        pygame.init()

        self.telasize = (900,800)
        self.size_per_space = self.telasize[1]//8

        self.tela = pygame.display.set_mode(self.telasize)

        pygame.display.set_caption('Xadrez')
        self.background = Background(self, (255,255,200))
        self.ui = GUI(self)

        self.timeJogando = 1

        self.pessas = {}

        self.mover_pessa_esta_permitido = True

        self.objetos = [
            Torre(self, (0,7), 1),
            Torre(self, (7,7), 1),
            Cavalo(self, (1,7), 1),
            Cavalo(self, (6,7), 1),
            Bispo(self, (2,7), 1),
            Bispo(self, (5,7), 1),
            Rainha(self, (3,7), 1),
            Rei(self, (4,7), 1),
            
            Torre(self, (0,0), -1),
            Torre(self, (7,0), -1),
            Cavalo(self, (1,0), -1),
            Cavalo(self, (6,0), -1),
            Bispo(self, (2,0), -1),
            Bispo(self, (5,0), -1),
            Rainha(self, (3,0), -1),
            Rei(self, (4,0), -1),
            self.background,
            self.ui,
        ]

        for i in range(8):
            self.objetos.insert(0, Peao(self, (i,1), -1))
            
        for i in range(8):
            self.objetos.insert(0, Peao(self, (i,6), 1))

        self.game_rules = [
            check
        ]

        self.clock = pygame.Clock()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.rules()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.__init__()

    def draw(self):
        self.tela.fill((0,0,0))

        for obj in self.objetos:
            obj.draw()

        pygame.display.update()

    def update(self):
        for obj in self.objetos:
            obj.update()

        self.clock.tick(60)

    def rules(self):
        for rule in self.game_rules:
            rule(self)