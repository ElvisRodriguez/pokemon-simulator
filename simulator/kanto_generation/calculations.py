from constants import ExperienceGroup


def get_experience(
        experience_group: ExperienceGroup, level: int
    ) -> int:
    """
    Get the experience at the level of a pokemon in their experience group.
    """
    experience = 0

    if level == 1:
        return experience

    if experience_group == ExperienceGroup.SLOW:
        experience = 5 * pow(level, 3) / 4

    if experience_group == ExperienceGroup.MEDIUM_SLOW:
        experience = ((6 / 5) * pow(level, 3) - 15 * pow(level, 2) + 100 * level - 140)

    if experience_group == ExperienceGroup.MEDIUM_FAST:
        experience = pow(level, 3)

    if experience_group == ExperienceGroup.FAST:
        experience = 4 * pow(level, 3) / 5

    if experience_group == ExperienceGroup.ERRATIC:
        if level in range(98, 100):
            experience = pow(level, 3) * (160 - level) / 100
        if level in range(68, 98):
            experience = pow(level, 3) * int((1911 - 10 * level) / 3) / 500
        if level in range(50, 68):
            experience = pow(level, 3) * (150 - level) / 100
        if level < 50:
            experience = pow(level, 3) * (100 - level) / 50

    if experience_group == ExperienceGroup.FLUCTUATING:
        if level in range(36, 100):
            experience = pow(level, 3) * (level // 2 + 32) / 50
        if level in range(15, 36):
            experience = pow(level, 3) * (level + 14) / 50
        if level < 15:
            experience = pow(level, 3) * int(((level + 1) / 3) + 24) / 50

    return experience