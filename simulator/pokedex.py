from constants import (
    BaseStats,
    DynamicValues,
    EffortValues,
    ExperienceGroup,
    StatStages,
    Status,
    Type,
    Types,
)
import moves
from Pokemon import Pokemon


SCIZOR = Pokemon(
    base_stats=BaseStats(70, 130, 100, 55, 80, 65),
    dynamic_values=DynamicValues(),
    effort_values=EffortValues(),
    experience_group=ExperienceGroup.MEDIUM_FAST,
    item=None,
    level=50,
    moveset=[moves.STEEL_WING],
    name="Scizor",
    stage=2,
    stat_stages=StatStages,
    status=Status.HEALTHY,
    types=Types(Type.BUG, Type.STEEL),
)