import calculations
from constants import (
    BaseStats,
    DynamicValues,
    EffortValues,
    ExperienceGroup,
    Item,
    Gender,
    MAX_LEVEL,
    Stat,
    StatStages,
    Status,
    Technique,
    Types,
)


class Pokemon:
    def __init__(
        self,
        base_stats: BaseStats,
        dynamic_values: DynamicValues,
        effort_values: EffortValues,
        experience_group: ExperienceGroup,
        item: Item,
        level: int,
        gender: Gender,
        moves: list[Technique],
        moveset: dict[int, Technique],
        name: str,
        stage: int,
        stat_stages: StatStages,
        status: Status,
        types: Types,
    ) -> None:
        # Input Args
        self._base_stats = base_stats
        self._dynamic_values = dynamic_values
        self._effort_value_given = calculations.calculate_effort_value_given(
            base_stats, stage
        )
        self._effort_values = effort_values
        self._experience_group = experience_group
        self._item = item
        self._gender = gender
        self._level = level
        self._moves = moves
        self._moveset = moveset
        self._name = name
        self._stage = stage
        self._stat_stages = stat_stages
        self._status = status
        self._types = types
        # Non input Args
        self._experience = calculations.get_experience(experience_group, level)
        self._stats = calculations.calculate_stats(
            base_stats, dynamic_values, effort_values, level
        )
        self._max_hp = self._stats.HP

    def __eq__(self, pokemon):
        if isinstance(pokemon, self.__class__):
            if (
                self._name == pokemon.name and
                self._stage == pokemon.stage and
                self._types.type_a == pokemon.types.type_a and
                self._types.type_b == pokemon.types.type_b
            ):
                return True
            return False

    @property
    def base_stats(self) -> BaseStats:
        return self._base_stats

    @property
    def dynamic_values(self) -> DynamicValues:
        return self._dynamic_values

    @property
    def effort_values(self) -> EffortValues:
        return self._effort_values

    @effort_values.setter
    def effort_values(self, stat: Stat, effort_value_points: int) -> None:
        self._effort_values[stat.name] += effort_value_points
    
    @property
    def effort_value_given(self) -> tuple:
        return self._effort_value_given

    @property
    def experience_group(self) -> ExperienceGroup:
        return self._experience_group
    
    @property
    def item(self) -> Item:
        return self._item
    
    @property
    def gender(self) -> Gender:
        return self._gender

    @property
    def level(self) -> int:
        return self._level

    @property
    def moves(self) -> list[Technique]:
        return self._moves

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def stage(self) -> int:
        return self._stage
    
    @property
    def stat_stages(self) -> StatStages:
        return self._stat_stages

    @property
    def status(self) -> Status:
        return self._status

    @status.setter
    def status(self, new_status: Status) -> None:
        self._status = new_status

    @property
    def types(self) -> Types:
        return self._types

    @property
    def experience(self) -> int:
        return self._experience

    @experience.setter
    def experience(self, _experience: int) -> None:
        if self._level < MAX_LEVEL:
            self._experience += _experience
            next_level_experience = calculations.get_experience(
                self._experience_group, self._level + 1
            )
            while next_level_experience < self._experience:
                self._level += 1
                next_level_experience = calculations.get_experience(
                    self._experience_group, self._level
                )
            self._level = min(self._level, MAX_LEVEL)

    @property
    def stats(self):
        return self._stats
    
    @property.getter
    def max_hp(self):
        return self._max_hp


if __name__ == "__main__":
    pass