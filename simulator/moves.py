import random

from calculations import calculate_damage
from constants import (
    MoveAction,
    MoveClass,
    Type,
)
from Pokemon import Pokemon
from Technique import Technique


STEEL_WING = Technique(
    name="Steel Wing",
    power=70,
    move_class=MoveClass.PHYSICAL,
    move_type=Type.STEEL,
    move_action=MoveAction,
)
def steel_wing(STEEL_WING: Technique, attacker: Pokemon, defender: Pokemon):
    if random.random() <= 0.1:
        attacker.stat_stages.Defense += 1
    calculate_damage(STEEL_WING, attacker, defender)
STEEL_WING.move_action = steel_wing