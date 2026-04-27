import pygame, random

class Piece(pygame.sprite.Sprite):
    def __init__(self, game, pos:list, team:int, image_file:str):
        self.game = game

        self.pos = pos
        self.game_pos = [n * self.game.size_per_space for n in self.pos]

        self.image = pygame.image.load(f"assets/img/{image_file}.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=self.game_pos)
        self.team = team
        self.bypassotherpieces = False

        self.game_pos[0] += random.randint(-10,10)
        self.game_pos[1] += random.randint(-10,10)
        
        if self.team == -1:
            self.image.fill((255,255,255), special_flags=pygame.BLEND_RGB_SUB)
            self.image.fill((100,100,100), special_flags=pygame.BLEND_RGB_ADD)

        self.game.pessas[pos] = self

        self.relative_points = []
        self.attack_points = []
        
        self.is_king = False

    def UpdatePaths(self):
        pass

    def draw(self):
        self.game.background.image.blit(self.image, self.game_pos)

    def DrawPaths(self):
        self.game.background.reset()

        Allpoints = []
        for r_point in self.relative_points+self.attack_points:
            if r_point == "#":
                Allpoints.append("#")
                continue
        
            real_pos = self.GetFromRelativePoint(*r_point)
            Allpoints.append(real_pos)

        self.game.background.MarkPoints(Allpoints, self.bypassotherpieces, self)

    def update(self):
        self.game_pos = [n * self.game.size_per_space for n in self.pos]

    def move(self, x, y):

        self.game.background.last_move_piece_position = self.pos

        if (x, y) in self.game.pessas and self.game.pessas[(x, y)].team != self.team:
            self.game.pessas[(x, y)].kill()
            
        pos_antiga = self.pos[:]
        self.pos = (x, y)
        self.game.pessas[self.pos] = self
        del self.game.pessas[tuple(pos_antiga)]

        self.game.timeJogando = -self.game.timeJogando
        
        self.UpdatePaths()

    def kill(self):
        del self.game.pessas[tuple(self.pos)]
        self.game.objetos.remove(self)
        del self

    def GetFromRelativePoint(self, x,y):
        pos = list(self.pos[:])
        pos[0] += x * self.team
        pos[1] += y * self.team

        return tuple(pos)
    
    def get_relative_points(self):
        copy = self.relative_points[:]
        while "#" in copy:
            copy.remove("#")

        return copy

    def get_attack_points(self):
        copy = self.attack_points[:]
        while "#" in copy:
            copy.remove("#")

        return copy