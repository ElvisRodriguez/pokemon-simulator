from constants import Technique
import moves
from Pokemon import Pokemon


class BattleOverworld:
    def __init__(self):
        self.active_moves = []
        self.moves_used = []
    
    def reset(self):
        self.active_moves = []
        self.moves_used = []
    
    @property
    def last_move_used(self) -> Technique:
        if len(self.moves_used) > 0:
            return self.moves_used[-1]
        return None
    
    def reset_pokemon(pokemon: Pokemon):
        pokemon.stats = pokemon._frozen_stats
        pokemon.stat_stages.reset()