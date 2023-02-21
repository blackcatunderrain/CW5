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


WarriorClass = UnitClass("Воин", 200, 40, 4, 5, 15, WarriorSkill)

ThiefClass = UnitClass("Вор", 200, 30, 3, 15, 5, ThiefSkill)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
