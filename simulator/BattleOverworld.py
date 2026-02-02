from constants import Technique

class BattleOverworld:
    def __init__(self):
        self._fire_spin = ("FIRE_SPIN", 0)
        self._fury_cutter = ("FURY_CUTTER", 0)
        self._rage = ("RAGE", 0)
        self._rain_dance = ("RAIN_DANCE", 0)
        self._rollout = ("ROLLOUT", 0)
        self._sunny_day = ("SUNNY_DAY", 0)
        self._wrap = ("WRAP", 0)
        self.active_moves = []
        self.moves_used = []
    
    def reset(self):
        self._fire_spin = ("FIRE_SPIN", 0)
        self._fury_cutter = ("FURY_CUTTER", 0)
        self._rage = ("RAGE", 0)
        self._rain_dance = ("RAIN_DANCE", 0)
        self._rollout = ("ROLLOUT", 0)
        self._sunny_day = ("SUNNY_DAY", 0)
        self._wrap = ("WRAP", 0)
        self.active_moves = []
        self.moves_used = []
    
    @property
    def fury_cutter(self) -> int:
        return self._fury_cutter

    @property
    def rage(self) -> int:
        return self._rage

    @property
    def rain_dance(self) -> int:
        return self._rain_dance
    
    @property
    def rollout(self) -> int:
        return self._rollout
    
    @property
    def sunny_day(self) -> int:
        return self._sunny_day
    
    @property
    def last_move_used(self) -> Technique:
        if len(self.moves_used) > 0:
            return self.moves_used[-1]
        return None