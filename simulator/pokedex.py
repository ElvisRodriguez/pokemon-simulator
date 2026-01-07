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


def refresh_pokemon(pokemon: Pokemon) -> Pokemon:
    _pokemon = Pokemon(
        base_stats=pokemon.base_stats,
        dynamic_values=DynamicValues(),
        effort_values=pokemon.effort_values,
        experience_group=pokemon.experience_group,
        item=pokemon.item,
        level=pokemon.level,
        moveset=pokemon.moveset,
        name=pokemon.name,
        stage=pokemon.stage,
        stat_stages=pokemon.stat_stages,
        status=pokemon.status,
        types=pokemon.types,
    )
    return _pokemon


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