from pieces.piece import Piece
import copy

class Cavalo(Piece):
    def __init__(self, game, pos:list, team:int):
        super().__init__(game, pos, team, "cavalo")

        self.relative_points = [
            (2,1),"#",(2,-1),"#",
            (1,2),"#",(-1,2),"#",
            (-2,1),"#",(-2,-1),"#",
            (1,-2),"#",(-1,-2)
        ]
        self.attack_points = copy.deepcopy(self.relative_points)
        self.bypassotherpieces = True