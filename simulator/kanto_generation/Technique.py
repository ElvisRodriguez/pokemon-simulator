from dataclasses import dataclass

from simulator.constants import MoveClass, Type


@dataclass
class Technique:
    name: str
    power: int
    power_points = int
    accuracy = float
    move_class: MoveClass
    move_type: Type
