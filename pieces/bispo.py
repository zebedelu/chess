from pieces.piece import Piece
import copy

class Bispo(Piece):
    def __init__(self, game, pos:list, team:int):
        super().__init__(game, pos, team, "bispo")

        self.relative_points = [
            *[(n,n) for n in range(1,8)],
            "#",
            *[(-n,-n) for n in range(1,8)],
            "#",
            *[(n,-n) for n in range(1,8)],
            "#",
            *[(-n,n) for n in range(1,8)],
            "#"
        ]
        self.attack_points = copy.deepcopy(self.relative_points)