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
)
def absorb(ABSORB: Technique, attacker: Pokemon, defender: Pokemon):
    damage = calculate_damage(ABSORB, attacker, defender)
    recoverable = damage // 2
    if attacker.stats.HP + recoverable > attacker.max_hp:
        attacker.stats.HP = attacker.max_hp
    else:
        attacker.stats.HP += recoverable
ABSORB.move_action = absorb


ACID = Technique(
    name="Acid",
    power=40,
    accuracy=100,
    power_points=30,
    move_class=MoveClass.SPECIAL,
    move_type=Type.POISON,
    move_action=MoveAction,
)
def acid(ACID: Technique, attacker: Pokemon, defender: Pokemon):
    calculate_damage(ACID, attacker, defender)
    if random.random < 1/10:
        if defender.stat_stages.SpecialDefense > -6:
            defender.stat_stages.SpecialDefense -= 1
ACID.move_action = acid


ACID_ARMOR = Technique(
    name="Acid Armor",
    power=0,
    accuracy=100,
    power_points=20,
    move_class=MoveClass.STATUS,
    move_type=Type.POISON,
    move_action=MoveAction,
)
def acid_armor(ACID_ARMOR: Technique, attacker: Pokemon, defender: Pokemon):
    if attacker.stat_stages.Defense < 6:
        attacker.stat_stages.Defense += 2
    if attacker.stat_stages.Defense > 6:
        attacker.stat_stages.Defense = 6
ACID_ARMOR.move_action = acid_armor


AGILITY = Technique(
    name="Agility",
    power=0,
    accuracy=100,
    power_points=30,
    move_class=MoveClass.STATUS,
    move_type=Type.PSYCHIC,
    move_action=MoveAction,
)
def agility(AGILITY: Technique, attacker: Pokemon, defender: Pokemon):
    if attacker.stat_stages.Speed < 6:
        attacker.stat_stages.Speed += 2
    if attacker.stat_stages.Speed > 6:
        attacker.stat_stages.Speed = 6
AGILITY.move_action = agility


AMNESIA = Technique(
    name="Amnesia",
    power=0,
    accuracy=100,
    power_points=20,
    move_class=MoveClass.STATUS,
    move_type=Type.PSYCHIC,
    move_action=MoveAction,
)
def amnesia(AMNESIA: Technique, attacker: Pokemon, defender: Pokemon):
    if attacker.stat_stages.SpecialDefense < 6:
        attacker.stat_stages.SpecialDefense += 2
    if attacker.stat_stages.SpecialDefense > 6:
        attacker.stat_stages.SpecialDefense = 6
AMNESIA.move_action = amnesia


AURORA_BEAM = Technique(
    name="Aurora Beam",
    power=65,
    accuracy=100,
    power_points=20,
    move_class=MoveClass.SPECIAL,
    move_type=Type.ICE,
    move_action=MoveAction,
)
def aurora_beam(AURORA_BEAM: Technique, attacker: Pokemon, defender: Pokemon):
    calculate_damage(AURORA_BEAM, attacker, defender)
    if random.random < 1/10:
        if defender.stat_stages.Attack > -6:
            defender.stat_stages.Attack -= 1
AURORA_BEAM.move_action = aurora_beam


###-------------------------------Gen 2 Moves-------------------------------###
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