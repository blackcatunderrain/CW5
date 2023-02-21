from dataclasses import dataclass
import random
from typing import List
import marshmallow
import marshmallow_dataclass
import json


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def random_damage(self) -> float:
        return random.uniform(self.min_damage, self.max_damage)


def random_damage(min_damage: float, max_damage: float) -> float:
    return random.uniform(min_damage, max_damage)


WeaponSchema = marshmallow_dataclass.class_schema(Weapon)


@dataclass
class EquipmentData:
    weapons: list[Weapon]
    armors: list[Armor]

    class Meta:
        unkwnown = marshmallow.EXCLUDE


EquipmentDataSchema = marshmallow_dataclass.class_schema(EquipmentData)


class Equipment():
    def __init__(self):
        self._get_equipmentdata_class()

    def _get_equipmentdata_class(self) -> List[EquipmentData]:
        try:
            with open("data/equipment.json", "r", encoding="utf-8") as f:
                result = EquipmentDataSchema().load(json.load(f))
                return result
        except:
            raise "ошибка в открытие файла "

    def get_weapon(self, name_weapon: str) -> [Weapon, str]:
        result = [weapon for weapon in self._get_equipmentdata_class().weapons if name_weapon in weapon.name]
        if not result:
            return f"{name_weapon} не найдено"
        return result[0]

    def get_armor(self, name_armor: str) -> [Armor, str]:
        result = [armor for armor in self._get_equipmentdata_class().armors if name_armor in armor.name]
        if not result:
            return f"{name_armor} не найдено"
        return result[0]

    def get_weapon_names(self) -> list:
        list = [weapon for weapon in self._get_equipmentdata_class().weapons]
        results = [weapon.name for weapon in list]

        return results

    def get_armors_names(self) -> list:
        list = [armor for armor in self._get_equipmentdata_class().armors]
        results = [armor.name for armor in list]

        return results
