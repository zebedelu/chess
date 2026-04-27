from pieces.piece import Piece

class Peao(Piece):
    def __init__(self, game, pos:list, team:int):
        super().__init__(game, pos, team, "peao")
        self.moves = 0

        self.relative_points = [
            "#",
            (0,-1),
            (0,-2),
            "#"
        ]
        self.attack_points = [
            (-1,-1),
            "#",
            (1,-1),
            "#"
        ]

    def UpdatePaths(self):
        if (0, -2) in self.relative_points:
            self.relative_points.remove((0, -2))