import random

from constants import (
    BaseStats,
    DynamicValues,
    EffortValues,
    ExperienceGroup,
    MoveClass,
    Stat,
    Stats,
    TYPE_CHART,
)
from Pokemon import Pokemon
from Technique import Technique


def calculate_damage(
        move: Technique,
        attacker: Pokemon,
        defender: Pokemon,
        critical_hit_modifier: float,
    ):
    if move.move_class == MoveClass.PHYSICAL:
        numerator = (
            (2 * attacker.level) * 
            move.power * 
            attacker.stats.Attack / defender.stats.Defense
        )
    elif move.move_class == MoveClass.SPECIAL:
        numerator = (
            (2 * attacker.level / 5 + 2) * 
            move.power * 
            attacker.stats.SpecialAttack / defender.stats.SpecialDefense
        )
    denominator = 50
    item = 1
    critical = 1
    if random.random <= (1/16 * critical_hit_modifier):
        critical = 2
    #(TODO): Implement for triple kick.
    triple_kick = 1
    #(TODO): Implement for weather effects.
    weather = 1
    #(TODO): Implement badge boosts
    badge = 1
    stab = 1
    if move.move_type == attacker.types.type_a or move.move_type == attacker.types.type_b:
        stab = 1.5
    first = TYPE_CHART[move.move_type, defender.types.type_a]
    second = TYPE_CHART[move.move_type, defender.types.type_b]
    effectiveness = first * second
    #(TODO): Implement for rollout, fury cutter, and rage.
    move_mod = 1
    _random = random.randint(217, 255) / 255
    #(TODO): Implement for pursuit, stomp, gust/twister, earthquake/magnitude
    double_damage = 1
    damage = ((numerator/denominator) * item * critical + 2) * triple_kick * weather * badge * stab * effectiveness * move_mod * _random * double_damage
    defender.stats.HP -= damage


def get_experience(experience_group: ExperienceGroup, level: int) -> int:
    """
    Get the experience at the level of a pokemon in their experience group.
    """
    experience = 0

    if level == 1:
        return experience

    if experience_group == ExperienceGroup.SLOW:
        experience = 5 * pow(level, 3) / 4

    if experience_group == ExperienceGroup.MEDIUM_SLOW:
        experience = (6 / 5) * pow(level, 3) - 15 * pow(level, 2) + 100 * level - 140

    if experience_group == ExperienceGroup.MEDIUM_FAST:
        experience = pow(level, 3)

    if experience_group == ExperienceGroup.FAST:
        experience = 4 * pow(level, 3) / 5

    if experience_group == ExperienceGroup.ERRATIC:
        if level in range(98, 101):
            experience = pow(level, 3) * (160 - level) / 100
        if level in range(68, 98):
            experience = pow(level, 3) * int((1911 - 10 * level) / 3) / 500
        if level in range(50, 68):
            experience = pow(level, 3) * (150 - level) / 100
        if level < 50:
            experience = pow(level, 3) * (100 - level) / 50

    if experience_group == ExperienceGroup.FLUCTUATING:
        if level in range(36, 101):
            experience = pow(level, 3) * (level // 2 + 32) / 50
        if level in range(15, 36):
            experience = pow(level, 3) * (level + 14) / 50
        if level < 15:
            experience = pow(level, 3) * int(((level + 1) / 3) + 24) / 50

    return int(experience)


def calculate_stat(
    base_stat: int,
    dynamic_value: int,
    effort_value: int,
    level: int,
    is_hp: bool = False,
) -> int:
    """Calculate an individual stat based on its base stat, DV, and EV."""
    partial_calculation = int(
        ((base_stat + dynamic_value) * 2 + int(effort_value / 4)) * level / 100
    )
    if is_hp:
        return partial_calculation + level + 10
    return partial_calculation + 5


def calculate_stats(
    base_stats: BaseStats,
    dynamic_values: DynamicValues,
    effort_values: EffortValues,
    level: int,
) -> Stats:
    """Calculate stats based on a pokemon's base stats, DVs, and EVs."""
    stat_names = list(Stat)
    stats = []
    for stat_name in stat_names:
        stat = stat_name.value
        is_hp = stat_name == Stat.HP
        stats.append(
            calculate_stat(
                base_stats[stat],
                dynamic_values[stat],
                effort_values[stat],
                level,
                is_hp=is_hp,
            )
        )
    return Stats(*stats)


def calculate_effort_value_given(base_stats: BaseStats, stage: int):
    """Calculate which stat the pokemon gives effort values in.S"""
    largest_stat = None
    stat_names = list(Stat)
    for stat_name in stat_names:
        stat = stat_name.value
        if largest_stat is None:
            largest_stat = (stat, base_stats[stat])
        else:
            if largest_stat[1] < base_stats[stat]:
                largest_stat = (stat, base_stats[stat])
    effort_value = (largest_stat[0], stage)
    return effort_value
    