import calculations
import constants
from Technique import Technique


class Pokemon:
    def __init__(
        self,
        base_stats: constants.BaseStats,
        dynamic_values: constants.DynamicValues,
        effort_values: constants.EffortValues,
        experience_group: constants.ExperienceGroup,
        level: int,
        moveset: list[Technique],
        name: str,
        status: constants.Status,
        types: tuple[constants.Type],
    ) -> None:
        self._base_stats = base_stats
        self._dynamic_values = dynamic_values
        self._effort_values = effort_values
        self._experience_group = experience_group
        self._level = level
        self._moveset = moveset
        self._name = name
        self._status = status
        self._types = types
        self._experience = calculations.get_experience(experience_group, level)
    
    @property
    def base_stats(self) -> constants.BaseStats:
        return self._base_stats
    
    @property
    def dynamic_values(self) -> constants.DynamicValues:
        return self._dynamic_values
    
    @property
    def effort_values(self) -> constants.EffortValues:
        return self._effort_values
    
    @effort_values.setter
    def effort_values(self, stat: constants.Stat, experience_gained: int) -> None:
        pass

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def level(self) -> int:
        return self._level
    
    
    