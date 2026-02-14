import random

from calculations import calculate_damage
from constants import (
    Gender,
    MoveAction,
    MoveClass,
    Status,
    Technique,
    Type,
)
from Pokemon import Pokemon


ABSORB = Technique(
    name="Absorb",
    power=20,
    accuracy=100,
    power_points=25,
    move_class=MoveClass.SPECIAL,
    move_type=Type.GRASS,
    move_action=MoveAction,
    priority=0,
    turns=0,
)
def absorb(ABSORB: Technique, attacker: Pokemon, defender: Pokemon) -> None:
    damage: float = calculate_damage(ABSORB, attacker, defender)
    recoverable: int = damage // 2
    if attacker.stats.HP + recoverable > attacker.max_hp:
        attacker.stats.HP = attacker.max_hp
    else:
        attacker.stats.HP += recoverable
    ABSORB.power_points -= 1
    return damage
ABSORB.move_action = absorb


ACID = Technique(
    name="Acid",
    power=40,
    accuracy=100,
    power_points=30,
    move_class=MoveClass.SPECIAL,
    move_type=Type.POISON,
    move_action=MoveAction,
    priority=0,
    turns=0,
)
def acid(ACID: Technique, attacker: Pokemon, defender: Pokemon) -> None:
    damage: float = calculate_damage(ACID, attacker, defender)
    if random.random() < 1/10:
        if defender.stat_stages.SpecialDefense > -6:
            defender.stat_stages.SpecialDefense -= 1
    ACID.power_points -= 1
    return damage
ACID.move_action = acid


ACID_ARMOR = Technique(
    name="Acid Armor",
    power=0,
    accuracy=100,
    power_points=20,
    move_class=MoveClass.STATUS,
    move_type=Type.POISON,
    move_action=MoveAction,
    priority=0,
    turns=0,
)
def acid_armor(
        ACID_ARMOR: Technique,
        attacker: Pokemon,
        defender: Pokemon
    ) -> None:
    if attacker.stat_stages.Defense < 6:
        attacker.stat_stages.Defense += 2
    if attacker.stat_stages.Defense > 6:
        attacker.stat_stages.Defense = 6
    ACID_ARMOR.power_points -= 1
ACID_ARMOR.move_action = acid_armor


AGILITY = Technique(
    name="Agility",
    power=0,
    accuracy=100,
    power_points=30,
    move_class=MoveClass.STATUS,
    move_type=Type.PSYCHIC,
    move_action=MoveAction,
    priority=0,
    turns=0,
)
def agility(AGILITY: Technique, attacker: Pokemon, defender: Pokemon) -> None:
    if attacker.stat_stages.Speed < 6:
        attacker.stat_stages.Speed += 2
    if attacker.stat_stages.Speed > 6:
        attacker.stat_stages.Speed = 6
    AGILITY.power_points -= 1
AGILITY.move_action = agility


AMNESIA = Technique(
    name="Amnesia",
    power=0,
    accuracy=100,
    power_points=20,
    move_class=MoveClass.STATUS,
    move_type=Type.PSYCHIC,
    move_action=MoveAction,
    priority=0,
    turns=0,
)
def amnesia(AMNESIA: Technique, attacker: Pokemon, defender: Pokemon) -> None:
    if attacker.stat_stages.SpecialDefense < 6:
        attacker.stat_stages.SpecialDefense += 2
    if attacker.stat_stages.SpecialDefense > 6:
        attacker.stat_stages.SpecialDefense = 6
    AMNESIA.power_points -= 1
AMNESIA.move_action = amnesia


AURORA_BEAM = Technique(
    name="Aurora Beam",
    power=65,
    accuracy=100,
    power_points=20,
    move_class=MoveClass.SPECIAL,
    move_type=Type.ICE,
    move_action=MoveAction,
    priority=0,
    turns=0,
)
def aurora_beam(
        AURORA_BEAM: Technique,
        attacker: Pokemon,
        defender: Pokemon
    ) -> None:
    damage: float = calculate_damage(AURORA_BEAM, attacker, defender)
    if random.random() < 1/10:
        if defender.stat_stages.Attack > -6:
            defender.stat_stages.Attack -= 1
    AURORA_BEAM.power_points -= 1
    return damage
AURORA_BEAM.move_action = aurora_beam


BARRAGE = Technique(
    name="Barrage",
    power=15,
    accuracy=85,
    power_points=20,
    move_class=MoveClass.PHYSICAL,
    move_type=Type.NORMAL,
    move_action=MoveAction,
    priority=0,
    turns=0,
)
def barrage(BARRAGE: Technique, attacker: Pokemon, defender: Pokemon) -> None:
    damage: float = 0
    if random.random() < 85/100:
        damage += calculate_damage(BARRAGE, attacker, defender)
        damage += calculate_damage(BARRAGE, attacker, defender)
        if random.random() < 3/8:
            damage += calculate_damage(BARRAGE, attacker, defender)
            if random.random() < 1/8:
                damage += calculate_damage(BARRAGE, attacker, defender)
                if random.random() < 1/8:
                    damage += calculate_damage(BARRAGE, attacker, defender)
    BARRAGE.power_points -= 1
    return damage
BARRAGE.move_action = barrage


BARRIER = Technique(
    name="Barrier",
    power=0,
    accuracy=100,
    power_points=20,
    move_class=MoveClass.STATUS,
    move_type=Type.PSYCHIC,
    move_action=MoveAction,
    priority=0,
    turns=0,
)
def barrier(BARRIER: Technique, attacker: Pokemon, defender: Pokemon) -> None:
    if attacker.stat_stages.Defense < 6:
        attacker.stat_stages.Defense += 2
    if attacker.stat_stages.Defense > 6:
        attacker.stat_stages.Defense = 6
    BARRIER.power_points -= 1
BARRIER.move_action = barrier


BIDE = Technique(
    name="Bide",
    power=0,
    accuracy=100,
    power_points=10,
    move_class=MoveClass.PHYSICAL,
    move_type=Type.NORMAL,
    move_action=MoveAction,
    priority=0,
    turns=0,
)
def bide(
        BIDE: Technique,
        attacker: Pokemon, 
        defender: Pokemon,
        damage_taken: float,
    ) -> None:
    damage: float = 0
    if BIDE.turns < 2:
        BIDE.power += damage_taken
    elif BIDE.turns == 2:
        damage = BIDE.power
        defender.HP -= BIDE.power
        BIDE.power = 0
        BIDE.turns = 0
    return damage
BIDE.move_action = bide


###-------------------------------Gen 2 Moves-------------------------------###
AEROBLAST = Technique(
    name="Aeroblast",
    power=100,
    accuracy=95,
    power_points= 5,
    move_class=MoveClass.SPECIAL,
    move_type=Type.FLYING,
    move_action=MoveAction,
    priority=0,
    turns=0,
)
def aeroblast(
        AEROBLAST: Technique,
        attacker: Pokemon,
        defender: Pokemon
    ) -> int:
    damage: float = 0
    if random.random() < AEROBLAST.accuracy / 100:
        critical_hit_modifier: int = 2
        damage = calculate_damage(
            AEROBLAST, attacker, defender, critical_hit_modifier
        )
    AEROBLAST.power_points -= 1
    return damage
AEROBLAST.move_action = aeroblast


ANCIENT_POWER = Technique(
    name="Ancient Power",
    power=60,
    accuracy=100,
    power_points=5,
    move_class=MoveClass.SPECIAL,
    move_type=Type.ROCK,
    move_action=MoveAction,
    priority=0,
    turns=0,
)
def ancient_power(
        ANCIENT_POWER: Technique,
        attacker: Pokemon,
        defender: Pokemon
    ) -> int:
    damage: float = calculate_damage(ANCIENT_POWER, attacker, defender)
    if random.random() < 1/10:
        attacker.stat_stages.Attack += 1
        attacker.stat_stages.Defense += 1
        attacker.stat_stages.SpecialAttack += 1
        attacker.stat_stages.SpecialDefense += 1
        attacker.stat_stages.Speed += 1
    ANCIENT_POWER.power_points -= 1
    return damage
ANCIENT_POWER.move_action = ancient_power


ATTRACT = Technique(
    name="Attract",
    power=0,
    accuracy=100,
    power_points= 15,
    move_class=MoveClass.STATUS,
    move_type=Type.NORMAL,
    move_action=MoveAction,
    priority=0,
    turns=0,
)
def attract(ATTRACT: Technique, attacker: Pokemon, defender: Pokemon) -> None:
    if (
        (attacker.gender == Gender.MALE and
         defender.gender == Gender.FEMALE) or
         (attacker.gender == Gender.FEMALE and
         defender.gender == Gender.MALE)
    ):
        defender.status = Status.INFATUATED
    ATTRACT.power_points -= 1
ATTRACT.move_action = attract


STEEL_WING = Technique(
    name="Steel Wing",
    power=70,
    accuracy=90,
    power_points=25,
    move_class=MoveClass.PHYSICAL,
    move_type=Type.STEEL,
    move_action=MoveAction,
    priority=0,
    turns=0,
)
def steel_wing(
        STEEL_WING: Technique,
        attacker: Pokemon,
        defender: Pokemon
    ) -> None:
    damage: float = 0
    if random.random() < STEEL_WING.accuracy / 100:
        damage = calculate_damage(STEEL_WING, attacker, defender)
        if random.random() <= 1/10:
            attacker.stat_stages.Defense += 1
    STEEL_WING.power_points -= 1
    return damage
STEEL_WING.move_action = steel_wing


if __name__ == "__main__":
    pass