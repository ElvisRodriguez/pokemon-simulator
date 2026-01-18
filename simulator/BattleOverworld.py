class BattleOverworld:
    def __init__(self):
        self._rain_dance = 0
        self._rollout = 0
        self._sunny_day = 0
    
    @property
    def rain_dance(self) -> int:
        return self._rain_dance
    
    @property
    def rollout(self) -> int:
        return self._rollout
    
    @property
    def sunny_day(self) -> int:
        return self._sunny_day