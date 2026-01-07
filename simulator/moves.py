import random

from calculations import calculate_damage
from constants import (
    MoveAction,
    MoveClass,
    Type,
)
from Pokemon import Pokemon
from Technique import Technique


AEROBLAST = Technique(
    name="Aeroblast",
    power=100,
    accuracy=95,
    move_class=MoveClass.SPECIAL,
    move_type=Type.FLYING,
    move_action=MoveAction,
)
def aeroblast(AEROBLAST: Technique, attacker: Pokemon, defender: Pokemon):
    if random.random < STEEL_WING.accuracy / 100:
        critical_hit_modifier = 2
        calculate_damage(AEROBLAST, attacker, defender, critical_hit_modifier)
AEROBLAST.move_action = aeroblast


STEEL_WING = Technique(
    name="Steel Wing",
    power=70,
    accuracy=90,
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