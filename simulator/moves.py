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


AEROBLAST = Technique(
    name="Aeroblast",
    power=100,
    accuracy=95,
    power_points= 5,
    move_class=MoveClass.SPECIAL,
    move_type=Type.FLYING,
    move_action=MoveAction,
)
def aeroblast(AEROBLAST: Technique, attacker: Pokemon, defender: Pokemon):
    if random.random < AEROBLAST.accuracy / 100:
        critical_hit_modifier = 2
        calculate_damage(AEROBLAST, attacker, defender, critical_hit_modifier)
AEROBLAST.move_action = aeroblast


ANCIENT_POWER = Technique(
    name="Ancient Power",
    power=60,
    accuracy=100,
    power_points=5,
    move_class=MoveClass.SPECIAL,
    move_type=Type.ROCK,
    move_action=MoveAction,
)
def ancient_power(ANCIENT_POWER: Technique, attacker: Pokemon, defender: Pokemon):
    calculate_damage(ANCIENT_POWER, attacker, defender)
    if random.random < 1/10:
        attacker.stat_stages.Attack += 1
        attacker.stat_stages.Defense += 1
        attacker.stat_stages.SpecialAttack += 1
        attacker.stat_stages.SpecialDefense += 1
        attacker.stat_stages.Speed += 1
ANCIENT_POWER.move_action = ancient_power


ATTRACT = Technique(
    name="Attract",
    power=0,
    accuracy=100,
    power_points= 15,
    move_class=MoveClass.STATUS,
    move_type=Type.NORMAL,
    move_action=MoveAction,
)
def attract(ATTRACT: Technique, attacker: Pokemon, defender: Pokemon):
    if (
        (attacker.gender == Gender.MALE and
         defender.gender == Gender.FEMALE) or
         (attacker.gender == Gender.FEMALE and
         defender.gender == Gender.MALE)
    ):
        defender.status = Status.INFATUATED
ATTRACT.move_action = attract


STEEL_WING = Technique(
    name="Steel Wing",
    power=70,
    accuracy=90,
    power_points=25,
    move_class=MoveClass.PHYSICAL,
    move_type=Type.STEEL,
    move_action=MoveAction,
)
def steel_wing(STEEL_WING: Technique, attacker: Pokemon, defender: Pokemon):
    if random.random < STEEL_WING.accuracy / 100:
        if random.random() <= 1/10:
            attacker.stat_stages.Defense += 1
        calculate_damage(STEEL_WING, attacker, defender)
STEEL_WING.move_action = steel_wing