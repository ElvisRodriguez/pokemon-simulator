from simulator.constants import (
    BaseStats,
    DynamicValues,
    EffortValues,
    ExperienceGroup,
    Stat,
    Stats,
)


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
    