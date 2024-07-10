from dataclasses import dataclass


@dataclass
class Control:
    move_left: bool = False
    move_right: bool = False
    jump: bool = False
    attack: bool = False
