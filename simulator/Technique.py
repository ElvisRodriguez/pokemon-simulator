from dataclasses import dataclass

from constants import MoveAction, MoveClass, Type


@dataclass
class Technique:
    name: str
    power: int
    power_points = int
    accuracy = int
    move_class: MoveClass
    move_type: Type
    move_action: MoveAction
