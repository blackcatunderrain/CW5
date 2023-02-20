from dataclasses import dataclass

from skills import WarriorSkill, ThiefSkill, Skill


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass("Воин", 50, 40, 10, 5, 15, WarriorSkill)

ThiefClass = UnitClass("Вор", 30, 30, 40, 15, 5, ThiefSkill)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
