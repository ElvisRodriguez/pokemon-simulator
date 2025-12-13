from dataclasses import dataclass
from enum import Enum
import random
from typing import NamedTuple


class Status(Enum):
    """(str) Current status of a pokemon's condition."""

    HEALTHY = "healthy"
    BURN = "burned"
    SLEEP = "sleeping"
    POISON = "poisoned"
    FROZEN = "frozen"
    PARALYSIS = "paralyzed"


class MoveClass(Enum):
    """(str) Determines which (if any) stats are used during damage calculation."""

    PHYSICAL = "physical"
    SPECIAL = "special"
    STATUS = "status"


class Type(Enum):
    """(str) Elemental type of a pokemon and/or its moves."""

    NORMAL = "normal"
    FIGHTING = "fighting"
    FLYING = "flying"
    POISON = "poison"
    GROUND = "ground"
    ROCK = "rock"
    BUG = "bug"
    GHOST = "ghost"
    STEEL = "steel"
    FIRE = "fire"
    WATER = "water"
    GRASS = "grass"
    ELECTRIC = "electric"
    PSYCHIC = "psychic"
    ICE = "ice"
    DRAGON = "dragon"
    DARK = "dark"
    FAIRY = "fairy"


class ExperienceGroup(Enum):
    """(str) Rate at which a pokemon levels up."""

    SLOW = "slow"
    MEDIUM_SLOW = "medium slow"
    MEDIUM_FAST = "medium fast"
    FAST = "fast"
    ERRATIC = "erratic"
    FLUCTUATING = "fluctuating"


class Stat(Enum):
    """(str) Statistics of a pokemon."""

    HP = "HP"
    ATTACK = "Attack"
    DEFENSE = "Defense"
    SPECIAL_ATTACK = "SpecialAttack"
    SPECIAL_DEFENSE = "SpecialDefense"
    SPEED = "Speed"


class Subscriptable:
    """Base Class to make cohesion between dataclasses easier."""

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, item, value):
        return setattr(self, item, value)


@dataclass(frozen=True)
class BaseStats(Subscriptable):
    """(int) Base statistics used in part to calculate current stats of a pokemon."""

    HP: int
    Attack: int
    Defense: int
    SpecialAttack: int
    SpecialDefense: int
    Speed: int


@dataclass
class Stats(Subscriptable):
    """Statistics of a pokemon."""

    HP: int
    Attack: int
    Defense: int
    SpecialAttack: int
    SpecialDefense: int
    Speed: int


@dataclass(frozen=True)
class DynamicValues(Subscriptable):
    """
    (int) Values (0 to 15 inclusive) used to calculate current stats of a pokemon.
    Calculated at creation of a pokemon and do not change.
    """

    HP: int = random.randint(0, 15)
    Attack: int = random.randint(0, 15)
    Defense: int = random.randint(0, 15)
    SpecialAttack: int = random.randint(0, 15)
    SpecialDefense: int = random.randint(0, 15)
    Speed: int = random.randint(0, 15)


@dataclass(frozen=True)
class IndividualValues(Subscriptable):
    """
    (int) Values (0 to 31 inclusive) used to calculate current stats of a pokemon.
    Calculated at creation of a pokemon and do not change (without use of special items).
    """

    HP: int = random.randint(0, 31)
    Attack: int = random.randint(0, 31)
    Defense: int = random.randint(0, 31)
    SpecialAttack: int = random.randint(0, 31)
    SpecialDefense: int = random.randint(0, 31)
    Speed: int = random.randint(0, 31)


@dataclass
class EffortValues(Subscriptable):
    """(int) Values gained through experience/items that affect stat growth."""

    HP: int = 0
    Attack: int = 0
    Defense: int = 0
    SpecialAttack: int = 0
    SpecialDefense: int = 0
    Speed: int = 0


class Types(NamedTuple):
    """(NamedTuple) Elemental type(s) of a pokemon. May only have type_a."""

    type_a: Type
    type_b: Type


class MoveAction():
    def action(*args, **kwargs):
        pass


MAX_LEVEL = 100


TYPE_CHART = {
    (Type.NORMAL, Type.NORMAL): 1,
    (Type.NORMAL, Type.FIGHTING): 1,
    (Type.NORMAL, Type.FLYING): 1,
    (Type.NORMAL, Type.POISON): 1,
    (Type.NORMAL, Type.GROUND): 1,
    (Type.NORMAL, Type.ROCK): 0.5,
    (Type.NORMAL, Type.BUG): 1,
    (Type.NORMAL, Type.GHOST): 0,
    (Type.NORMAL, Type.STEEL): 0.5,
    (Type.NORMAL, Type.FIRE): 1,
    (Type.NORMAL, Type.WATER): 1,
    (Type.NORMAL, Type.GRASS): 1,
    (Type.NORMAL, Type.ELECTRIC): 1,
    (Type.NORMAL, Type.PSYCHIC): 1,
    (Type.NORMAL, Type.ICE): 1,
    (Type.NORMAL, Type.DRAGON): 1,
    (Type.NORMAL, Type.DARK): 1,
    (Type.NORMAL, Type.FAIRY): 1,
    (Type.FIGHTING, Type.NORMAL): 2,
    (Type.FIGHTING, Type.FIGHTING): 1,
    (Type.FIGHTING, Type.FLYING): 0.5,
    (Type.FIGHTING, Type.POISON): 0.5,
    (Type.FIGHTING, Type.GROUND): 1,
    (Type.FIGHTING, Type.ROCK): 2,
    (Type.FIGHTING, Type.BUG): 0.5,
    (Type.FIGHTING, Type.GHOST): 0,
    (Type.FIGHTING, Type.STEEL): 2,
    (Type.FIGHTING, Type.FIRE): 1,
    (Type.FIGHTING, Type.WATER): 1,
    (Type.FIGHTING, Type.GRASS): 1,
    (Type.FIGHTING, Type.ELECTRIC): 1,
    (Type.FIGHTING, Type.PSYCHIC): 0.5,
    (Type.FIGHTING, Type.ICE): 2,
    (Type.FIGHTING, Type.DRAGON): 1,
    (Type.FIGHTING, Type.DARK): 2,
    (Type.FIGHTING, Type.FAIRY): 0.5,
    (Type.FLYING, Type.NORMAL): 1,
    (Type.FLYING, Type.FIGHTING): 2,
    (Type.FLYING, Type.FLYING): 1,
    (Type.FLYING, Type.POISON): 1,
    (Type.FLYING, Type.GROUND): 1,
    (Type.FLYING, Type.ROCK): 0.5,
    (Type.FLYING, Type.BUG): 2,
    (Type.FLYING, Type.GHOST): 1,
    (Type.FLYING, Type.STEEL): 0.5,
    (Type.FLYING, Type.FIRE): 1,
    (Type.FLYING, Type.WATER): 1,
    (Type.FLYING, Type.GRASS): 2,
    (Type.FLYING, Type.ELECTRIC): 0.5,
    (Type.FLYING, Type.PSYCHIC): 1,
    (Type.FLYING, Type.ICE): 1,
    (Type.FLYING, Type.DRAGON): 1,
    (Type.FLYING, Type.DARK): 1,
    (Type.FLYING, Type.FAIRY): 1,
    (Type.POISON, Type.NORMAL): 1,
    (Type.POISON, Type.FIGHTING): 1,
    (Type.POISON, Type.FLYING): 1,
    (Type.POISON, Type.POISON): 0.5,
    (Type.POISON, Type.GROUND): 0.5,
    (Type.POISON, Type.ROCK): 0.5,
    (Type.POISON, Type.BUG): 1,
    (Type.POISON, Type.GHOST): 0.5,
    (Type.POISON, Type.STEEL): 0,
    (Type.POISON, Type.FIRE): 1,
    (Type.POISON, Type.WATER): 1,
    (Type.POISON, Type.GRASS): 2,
    (Type.POISON, Type.ELECTRIC): 1,
    (Type.POISON, Type.PSYCHIC): 1,
    (Type.POISON, Type.ICE): 1,
    (Type.POISON, Type.DRAGON): 1,
    (Type.POISON, Type.DARK): 1,
    (Type.POISON, Type.FAIRY): 2,
    (Type.GROUND, Type.NORMAL): 1,
    (Type.GROUND, Type.FIGHTING): 1,
    (Type.GROUND, Type.FLYING): 0,
    (Type.GROUND, Type.POISON): 2,
    (Type.GROUND, Type.GROUND): 1,
    (Type.GROUND, Type.ROCK): 2,
    (Type.GROUND, Type.BUG): 0.5,
    (Type.GROUND, Type.GHOST): 1,
    (Type.GROUND, Type.STEEL): 2,
    (Type.GROUND, Type.FIRE): 2,
    (Type.GROUND, Type.WATER): 1,
    (Type.GROUND, Type.GRASS): 0.5,
    (Type.GROUND, Type.ELECTRIC): 2,
    (Type.GROUND, Type.PSYCHIC): 1,
    (Type.GROUND, Type.ICE): 1,
    (Type.GROUND, Type.DRAGON): 1,
    (Type.GROUND, Type.DARK): 1,
    (Type.GROUND, Type.FAIRY): 1,
    (Type.ROCK, Type.NORMAL): 1,
    (Type.ROCK, Type.FIGHTING): 0.5,
    (Type.ROCK, Type.FLYING): 2,
    (Type.ROCK, Type.POISON): 1,
    (Type.ROCK, Type.GROUND): 0.5,
    (Type.ROCK, Type.ROCK): 1,
    (Type.ROCK, Type.BUG): 2,
    (Type.ROCK, Type.GHOST): 1,
    (Type.ROCK, Type.STEEL): 0.5,
    (Type.ROCK, Type.FIRE): 2,
    (Type.ROCK, Type.WATER): 1,
    (Type.ROCK, Type.GRASS): 1,
    (Type.ROCK, Type.ELECTRIC): 1,
    (Type.ROCK, Type.PSYCHIC): 1,
    (Type.ROCK, Type.ICE): 2,
    (Type.ROCK, Type.DRAGON): 1,
    (Type.ROCK, Type.DARK): 1,
    (Type.ROCK, Type.FAIRY): 1,
    (Type.BUG, Type.NORMAL): 1,
    (Type.BUG, Type.FIGHTING): 0.5,
    (Type.BUG, Type.FLYING): 0.5,
    (Type.BUG, Type.POISON): 0.5,
    (Type.BUG, Type.GROUND): 1,
    (Type.BUG, Type.ROCK): 1,
    (Type.BUG, Type.BUG): 1,
    (Type.BUG, Type.GHOST): 0.5,
    (Type.BUG, Type.STEEL): 0.5,
    (Type.BUG, Type.FIRE): 0.5,
    (Type.BUG, Type.WATER): 1,
    (Type.BUG, Type.GRASS): 2,
    (Type.BUG, Type.ELECTRIC): 1,
    (Type.BUG, Type.PSYCHIC): 2,
    (Type.BUG, Type.ICE): 1,
    (Type.BUG, Type.DRAGON): 1,
    (Type.BUG, Type.DARK): 2,
    (Type.BUG, Type.FAIRY): 0.5,
    (Type.GHOST, Type.NORMAL): 0,
    (Type.GHOST, Type.FIGHTING): 1,
    (Type.GHOST, Type.FLYING): 1,
    (Type.GHOST, Type.POISON): 1,
    (Type.GHOST, Type.GROUND): 1,
    (Type.GHOST, Type.ROCK): 1,
    (Type.GHOST, Type.BUG): 1,
    (Type.GHOST, Type.GHOST): 2,
    (Type.GHOST, Type.STEEL): 1,
    (Type.GHOST, Type.FIRE): 1,
    (Type.GHOST, Type.WATER): 1,
    (Type.GHOST, Type.GRASS): 1,
    (Type.GHOST, Type.ELECTRIC): 1,
    (Type.GHOST, Type.PSYCHIC): 2,
    (Type.GHOST, Type.ICE): 1,
    (Type.GHOST, Type.DRAGON): 1,
    (Type.GHOST, Type.DARK): 0.5,
    (Type.GHOST, Type.FAIRY): 1,
    (Type.STEEL, Type.NORMAL): 1,
    (Type.STEEL, Type.FIGHTING): 1,
    (Type.STEEL, Type.FLYING): 1,
    (Type.STEEL, Type.POISON): 1,
    (Type.STEEL, Type.GROUND): 1,
    (Type.STEEL, Type.ROCK): 2,
    (Type.STEEL, Type.BUG): 1,
    (Type.STEEL, Type.GHOST): 1,
    (Type.STEEL, Type.STEEL): 0.5,
    (Type.STEEL, Type.FIRE): 0.5,
    (Type.STEEL, Type.WATER): 0.5,
    (Type.STEEL, Type.GRASS): 1,
    (Type.STEEL, Type.ELECTRIC): 0.5,
    (Type.STEEL, Type.PSYCHIC): 1,
    (Type.STEEL, Type.ICE): 2,
    (Type.STEEL, Type.DRAGON): 1,
    (Type.STEEL, Type.DARK): 1,
    (Type.STEEL, Type.FAIRY): 2,
    (Type.FIRE, Type.NORMAL): 1,
    (Type.FIRE, Type.FIGHTING): 1,
    (Type.FIRE, Type.FLYING): 1,
    (Type.FIRE, Type.POISON): 1,
    (Type.FIRE, Type.GROUND): 1,
    (Type.FIRE, Type.ROCK): 0.5,
    (Type.FIRE, Type.BUG): 2,
    (Type.FIRE, Type.GHOST): 1,
    (Type.FIRE, Type.STEEL): 2,
    (Type.FIRE, Type.FIRE): 0.5,
    (Type.FIRE, Type.WATER): 0.5,
    (Type.FIRE, Type.GRASS): 2,
    (Type.FIRE, Type.ELECTRIC): 1,
    (Type.FIRE, Type.PSYCHIC): 1,
    (Type.FIRE, Type.ICE): 2,
    (Type.FIRE, Type.DRAGON): 0.5,
    (Type.FIRE, Type.DARK): 1,
    (Type.FIRE, Type.FAIRY): 1,
    (Type.WATER, Type.NORMAL): 1,
    (Type.WATER, Type.FIGHTING): 1,
    (Type.WATER, Type.FLYING): 1,
    (Type.WATER, Type.POISON): 1,
    (Type.WATER, Type.GROUND): 2,
    (Type.WATER, Type.ROCK): 2,
    (Type.WATER, Type.BUG): 1,
    (Type.WATER, Type.GHOST): 1,
    (Type.WATER, Type.STEEL): 1,
    (Type.WATER, Type.FIRE): 2,
    (Type.WATER, Type.WATER): 0.5,
    (Type.WATER, Type.GRASS): 0.5,
    (Type.WATER, Type.ELECTRIC): 1,
    (Type.WATER, Type.PSYCHIC): 1,
    (Type.WATER, Type.ICE): 1,
    (Type.WATER, Type.DRAGON): 0.5,
    (Type.WATER, Type.DARK): 1,
    (Type.WATER, Type.FAIRY): 1,
    (Type.GRASS, Type.NORMAL): 1,
    (Type.GRASS, Type.FIGHTING): 1,
    (Type.GRASS, Type.FLYING): 0.5,
    (Type.GRASS, Type.POISON): 0.5,
    (Type.GRASS, Type.GROUND): 2,
    (Type.GRASS, Type.ROCK): 2,
    (Type.GRASS, Type.BUG): 0.5,
    (Type.GRASS, Type.GHOST): 0,
    (Type.GRASS, Type.STEEL): 0.5,
    (Type.GRASS, Type.FIRE): 0.5,
    (Type.GRASS, Type.WATER): 2,
    (Type.GRASS, Type.GRASS): 0.5,
    (Type.GRASS, Type.ELECTRIC): 1,
    (Type.GRASS, Type.PSYCHIC): 1,
    (Type.GRASS, Type.ICE): 1,
    (Type.GRASS, Type.DRAGON): 0.5,
    (Type.GRASS, Type.DARK): 1,
    (Type.GRASS, Type.FAIRY): 1,
    (Type.ELECTRIC, Type.NORMAL): 1,
    (Type.ELECTRIC, Type.FIGHTING): 1,
    (Type.ELECTRIC, Type.FLYING): 2,
    (Type.ELECTRIC, Type.POISON): 1,
    (Type.ELECTRIC, Type.GROUND): 0,
    (Type.ELECTRIC, Type.ROCK): 1,
    (Type.ELECTRIC, Type.BUG): 1,
    (Type.ELECTRIC, Type.GHOST): 1,
    (Type.ELECTRIC, Type.STEEL): 1,
    (Type.ELECTRIC, Type.FIRE): 1,
    (Type.ELECTRIC, Type.WATER): 2,
    (Type.ELECTRIC, Type.GRASS): 0.5,
    (Type.ELECTRIC, Type.ELECTRIC): 0.5,
    (Type.ELECTRIC, Type.PSYCHIC): 1,
    (Type.ELECTRIC, Type.ICE): 1,
    (Type.ELECTRIC, Type.DRAGON): 0.5,
    (Type.ELECTRIC, Type.DARK): 1,
    (Type.ELECTRIC, Type.FAIRY): 1,
    (Type.PSYCHIC, Type.NORMAL): 1,
    (Type.PSYCHIC, Type.FIGHTING): 2,
    (Type.PSYCHIC, Type.FLYING): 1,
    (Type.PSYCHIC, Type.POISON): 2,
    (Type.PSYCHIC, Type.GROUND): 1,
    (Type.PSYCHIC, Type.ROCK): 1,
    (Type.PSYCHIC, Type.BUG): 1,
    (Type.PSYCHIC, Type.GHOST): 1,
    (Type.PSYCHIC, Type.STEEL): 0.5,
    (Type.PSYCHIC, Type.FIRE): 1,
    (Type.PSYCHIC, Type.WATER): 1,
    (Type.PSYCHIC, Type.GRASS): 1,
    (Type.PSYCHIC, Type.ELECTRIC): 1,
    (Type.PSYCHIC, Type.PSYCHIC): 0.5,
    (Type.PSYCHIC, Type.ICE): 1,
    (Type.PSYCHIC, Type.DRAGON): 1,
    (Type.PSYCHIC, Type.DARK): 0,
    (Type.PSYCHIC, Type.FAIRY): 1,
    (Type.ICE, Type.NORMAL): 1,
    (Type.ICE, Type.FIGHTING): 1,
    (Type.ICE, Type.FLYING): 2,
    (Type.ICE, Type.POISON): 1,
    (Type.ICE, Type.GROUND): 2,
    (Type.ICE, Type.ROCK): 1,
    (Type.ICE, Type.BUG): 1,
    (Type.ICE, Type.GHOST): 1,
    (Type.ICE, Type.STEEL): 0.5,
    (Type.ICE, Type.FIRE): 0.5,
    (Type.ICE, Type.WATER): 0.5,
    (Type.ICE, Type.GRASS): 2,
    (Type.ICE, Type.ELECTRIC): 1,
    (Type.ICE, Type.PSYCHIC): 1,
    (Type.ICE, Type.ICE): 0.5,
    (Type.ICE, Type.DRAGON): 2,
    (Type.ICE, Type.DARK): 1,
    (Type.ICE, Type.FAIRY): 1,
    (Type.DRAGON, Type.NORMAL): 1,
    (Type.DRAGON, Type.FIGHTING): 1,
    (Type.DRAGON, Type.FLYING): 1,
    (Type.DRAGON, Type.POISON): 1,
    (Type.DRAGON, Type.GROUND): 1,
    (Type.DRAGON, Type.ROCK): 1,
    (Type.DRAGON, Type.BUG): 1,
    (Type.DRAGON, Type.GHOST): 1,
    (Type.DRAGON, Type.STEEL): 0.5,
    (Type.DRAGON, Type.FIRE): 1,
    (Type.DRAGON, Type.WATER): 1,
    (Type.DRAGON, Type.GRASS): 1,
    (Type.DRAGON, Type.ELECTRIC): 1,
    (Type.DRAGON, Type.PSYCHIC): 1,
    (Type.DRAGON, Type.ICE): 1,
    (Type.DRAGON, Type.DRAGON): 2,
    (Type.DRAGON, Type.DARK): 1,
    (Type.DRAGON, Type.FAIRY): 0,
    (Type.DARK, Type.NORMAL): 1,
    (Type.DARK, Type.FIGHTING): 0.5,
    (Type.DARK, Type.FLYING): 1,
    (Type.DARK, Type.POISON): 0.5,
    (Type.DARK, Type.GROUND): 1,
    (Type.DARK, Type.ROCK): 1,
    (Type.DARK, Type.BUG): 1,
    (Type.DARK, Type.GHOST): 2,
    (Type.DARK, Type.STEEL): 1,
    (Type.DARK, Type.FIRE): 1,
    (Type.DARK, Type.WATER): 1,
    (Type.DARK, Type.GRASS): 1,
    (Type.DARK, Type.ELECTRIC): 1,
    (Type.DARK, Type.PSYCHIC): 2,
    (Type.DARK, Type.ICE): 1,
    (Type.DARK, Type.DRAGON): 1,
    (Type.DARK, Type.DARK): 0.5,
    (Type.DARK, Type.FAIRY): 0.5,
    (Type.FAIRY, Type.NORMAL): 1,
    (Type.FAIRY, Type.FIGHTING): 2,
    (Type.FAIRY, Type.FLYING): 1,
    (Type.FAIRY, Type.POISON): 0.5,
    (Type.FAIRY, Type.GROUND): 1,
    (Type.FAIRY, Type.ROCK): 1,
    (Type.FAIRY, Type.BUG): 1,
    (Type.FAIRY, Type.GHOST): 1,
    (Type.FAIRY, Type.STEEL): 0.5,
    (Type.FAIRY, Type.FIRE): 0.5,
    (Type.FAIRY, Type.WATER): 1,
    (Type.FAIRY, Type.GRASS): 1,
    (Type.FAIRY, Type.ELECTRIC): 1,
    (Type.FAIRY, Type.PSYCHIC): 1,
    (Type.FAIRY, Type.ICE): 1,
    (Type.FAIRY, Type.DRAGON): 2,
    (Type.FAIRY, Type.DARK): 2,
    (Type.FAIRY, Type.FAIRY): 1,
}
