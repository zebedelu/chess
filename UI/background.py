import pygame, copy, time

class Background(pygame.sprite.Sprite):
    def __init__(self, game, white_space_color=(255,255,255)):
        self.game = game
        self.image = pygame.Surface(self.game.telasize)
        self.white_space_color = white_space_color
        
        self.last_move_piece_position = None

        self.selecionado = None
        self.AllPoints = []

        self.pointsToMoveRect = []
        self.pointsToAttackRect = []

        self.reset()

        self.rect = self.image.get_rect()
        
    def draw(self):
        if self.last_move_piece_position:
            pygame.draw.rect(self.image, (255,255,150), (*[x*self.game.size_per_space for x in self.last_move_piece_position], self.game.size_per_space, self.game.size_per_space))

        if pygame.key.get_pressed()[pygame.K_f]:
            self.game.mover_pessa_esta_permitido = False
            self.game.tela.blit(pygame.transform.flip(self.image, False, True), (0,0))
        else:
            self.game.mover_pessa_esta_permitido = True
            self.game.tela.blit(self.image, (0,0))

    def MarkPoints(self, all_points_list, bypassotherpieces, piece):
        self.AllPoints = []

        linha_permitida = True
        for point in all_points_list:
            # print(point)
            # if point != "#":
            #     pygame.draw.rect(self.image, (0,255,0), (*[n*self.game.size_per_space for n in point], 80,80))
            #     self.draw()
            #     pygame.display.update()
            # time.sleep(0.2)

            if point == '#':
                linha_permitida = True
                continue

            if linha_permitida == False:
                continue

            render = True
            if tuple(point) in self.game.pessas:
                render = False

                if self.game.pessas[tuple(point)].team != piece.team:
                    render = True
                    
                if not bypassotherpieces:
                    linha_permitida = False
            
            if render:
                # p = pygame.draw.rect(self.image, (150,232,150), (*[n*self.game.size_per_space for n in point], self.game.size_per_space, self.game.size_per_space))
                # self.AllPoints.add(p)
                if tuple(point) not in self.AllPoints:
                    self.AllPoints.append(tuple(point))
            else:
                linha_permitida = False

        attack_points = [piece.GetFromRelativePoint(*point) for point in piece.get_attack_points()]
        relative_points = [piece.GetFromRelativePoint(*point) for point in piece.get_relative_points()]

        self.AllPoints = set(self.AllPoints)

        for ponto in list(self.AllPoints-set(attack_points)):
            p = pygame.draw.rect(self.image, (150,232,150), (*[n*self.game.size_per_space for n in ponto], self.game.size_per_space, self.game.size_per_space))
            self.pointsToMoveRect.append(p)

        for ponto in list(self.AllPoints-set(relative_points)):
            p = pygame.draw.rect(self.image, (232,150,150), (*[n*self.game.size_per_space for n in ponto], self.game.size_per_space, self.game.size_per_space))
            self.pointsToAttackRect.append(p)

        if not set(self.AllPoints)-set(attack_points) and not set(self.AllPoints)-set(relative_points):
            for ponto in list(self.AllPoints):
                p = pygame.draw.rect(self.image, (232,150,150), (*[n*self.game.size_per_space for n in ponto], self.game.size_per_space, self.game.size_per_space))
                self.pointsToAttackRect.append(p)
                p = pygame.draw.rect(self.image, (150,232,150), (*[n*self.game.size_per_space for n in ponto], self.game.size_per_space, self.game.size_per_space))
                self.pointsToMoveRect.append(p)

    def reset(self):
        self.image.fill((0,0,0))

        for x in range(4):
            for y in range(4):
                pygame.draw.rect(self.image, self.white_space_color, (x*2*self.game.size_per_space, y*2*self.game.size_per_space, self.game.size_per_space, self.game.size_per_space))
        
        for x in range(4):
            for y in range(4):
                pygame.draw.rect(self.image, self.white_space_color, (x*2*self.game.size_per_space+self.game.size_per_space, y*2*self.game.size_per_space+self.game.size_per_space, self.game.size_per_space, self.game.size_per_space))

    def update(self):
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.selecionado = None
            self.pointsToMoveRect = []
            self.pointsToAttackRect = []
            self.reset()

        mouse = pygame.mouse
        if mouse.get_just_pressed()[0] and self.game.mover_pessa_esta_permitido:
            posicao_atual_mouse = tuple([n//self.game.size_per_space for n in mouse.get_pos()])

            for point in self.pointsToMoveRect:
                if point.collidepoint(mouse.get_pos()):
                    if self.selecionado and not posicao_atual_mouse in self.game.pessas:
                        self.selecionado.move(*posicao_atual_mouse)
                        self.selecionado = None
                        
                        self.pointsToMoveRect = []
                        self.reset()

            for point in self.pointsToAttackRect:
                if point.collidepoint(mouse.get_pos()):
                    if self.selecionado and posicao_atual_mouse in self.game.pessas and self.game.pessas[posicao_atual_mouse].team != self.selecionado.team:
                        self.selecionado.move(*posicao_atual_mouse)
                        self.selecionado = None

                        self.pointsToAttackRect = []
                        self.reset()

                        # pessa_selecionada = self.game.pessas.get(posicao_atual_mouse, None)
                        # pessa_selecionada.DrawPaths()

            pessa_selecionada = self.game.pessas.get(posicao_atual_mouse, None)

            if pessa_selecionada and pessa_selecionada.team == self.game.timeJogando and self.game.mover_pessa_esta_permitido:
                self.pointsToMoveRect = []
                self.pointsToAttackRect = []
                self.selecionado = pessa_selecionada
                if pessa_selecionada: pessa_selecionada.DrawPaths()