from constants import Technique

class BattleOverworld:
    def __init__(self):
        self._fury_cutter = 0
        self._rage = 0
        self._rain_dance = 0
        self._rollout = 0
        self._sunny_day = 0
        self._moves_used = []
    
    def reset(self):
        self._fury_cutter = 0
        self._rage = 0
        self._rain_dance = 0
        self._rollout = 0
        self._sunny_day = 0
        self._moves_used = []
    
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
    def moves_used(self) -> list:
        return self._moves_used
    
    @property
    def last_move_used(self) -> Technique:
        if len(self._moves_used) >= 1:
            return self._moves_used[-1]
        return None