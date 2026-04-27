from pieces.piece import Piece
import copy

class Rei(Piece):
    def __init__(self, game, pos:list, team:int):
        super().__init__(game, pos, team, "rei")

        self.relative_points = [
            (0,1),"#",(0,-1),"#",
            (1,0),"#",(-1,0),"#",
            (1,1),"#",(-1,-1),"#",
            (1,-1),"#",(-1,1)
        ]
        self.is_king = True
        self.attack_points = copy.deepcopy(self.relative_points)