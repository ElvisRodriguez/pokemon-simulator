from dataclasses import dataclass

from constants import MoveAction, MoveClass, Type


@dataclass
class Technique:
    """Attributes of a pokemon's move."""
    name: str
    power: int
    accuracy: int
    power_points = int
    accuracy = int
    move_class: MoveClass
    move_type: Type
    move_action: MoveAction
