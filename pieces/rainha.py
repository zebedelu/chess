from pieces.piece import Piece
import copy

class Rainha(Piece):
    def __init__(self, game, pos:list, team:int):
        super().__init__(game, pos, team, "rainha")

        self.relative_points = [
            # Bispo
            *[(n,n) for n in range(1,8)],
            "#",
            *[(-n,-n) for n in range(1,8)],
            "#",
            *[(n,-n) for n in range(1,8)],
            "#",
            *[(-n,n) for n in range(1,8)],
            "#",

            #Torre
            *[(0,-n) for n in range(1,8)],
            "#",
            *[(0,n) for n in range(1,8)],
            "#",
            *[(n,0) for n in range(1,8)],
            "#",
            *[(-n,0) for n in range(1,8)],
            "#"
        ]
        self.attack_points = copy.deepcopy(self.relative_points)