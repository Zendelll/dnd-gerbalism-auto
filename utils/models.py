from pydantic import BaseModel
from random import randint
from enum import Enum
from typing import Optional
from typing_extensions import Literal


class RarityEnum(Enum):
    """Rarity of a Plant"""

    common = "common"
    uncommon = "uncommon"
    rare = "rare"
    very_rare = "very_rare"


class PotionTypeEnum(Enum):
    """Type of alchemy where Plant can be used"""

    potion = "potion"  # Ingredient can be used in potions
    poison = "poison"  # Ingredient can be used in poisons
    all = "all"  # Ingredient can be used in potions and poisons
    magic = "magic"  # Ingredient can be used only for magic potions


class EffectTypeEnum(Enum):
    """Effect type of the Plant when used in alchemy"""

    base = "base"  # Ingredient can be used as a base
    modifier = "modifier"  # Ingredient can be used as a modifier


class TerrainTypesEnum(Enum):
    """Types of Terrain where Plants are growing"""

    common = "common"
    arctic = "arctic"
    water = "water"
    coastal = "coastal"
    desert = "desert"
    forest = "forest"
    grasslands = "grasslands"
    hills = "hills"
    mountain = "mountain"
    swamp = "swamp"
    underdark = "underdark"


class Plant(BaseModel):
    """Plant object. Describes an alchemic plant and its effects."""

    name: str
    description: str
    rarity: Literal[
        RarityEnum.common, RarityEnum.uncommon, RarityEnum.rare, RarityEnum.very_rare
    ]
    potion_type: Literal[
        PotionTypeEnum.potion,
        PotionTypeEnum.poison,
        PotionTypeEnum.all,
        PotionTypeEnum.magic,
    ]
    effect_type: Literal[
        EffectTypeEnum.base,
        EffectTypeEnum.modifier,
    ]
    effect_description: str
    difficulty_modifier: int
    terrain_types: list[
        Literal[
            TerrainTypesEnum.common,
            TerrainTypesEnum.arctic,
            TerrainTypesEnum.water,
            TerrainTypesEnum.coastal,
            TerrainTypesEnum.desert,
            TerrainTypesEnum.forest,
            TerrainTypesEnum.grasslands,
            TerrainTypesEnum.hills,
            TerrainTypesEnum.mountain,
            TerrainTypesEnum.swamp,
            TerrainTypesEnum.underdark,
        ]
    ]


class TerrainRollTable(BaseModel):
    terrain_type: Literal[
        TerrainTypesEnum.common,
        TerrainTypesEnum.arctic,
        TerrainTypesEnum.coastal,
        TerrainTypesEnum.water,
        TerrainTypesEnum.coastal,
        TerrainTypesEnum.desert,
        TerrainTypesEnum.forest,
        TerrainTypesEnum.grasslands,
        TerrainTypesEnum.hills,
        TerrainTypesEnum.mountain,
        TerrainTypesEnum.swamp,
        TerrainTypesEnum.underdark,
    ]
    roll: dict[int, RolledPlant]

    def roll_plant(self, elemental_water: Plant) -> RolledPlant:
        """Get plant based on 2d6 roll"""
        rolled_number = randint(1, 6) + randint(1, 6)

        # If we rolled 2-4 or 10-12 we roll d100 and on 75-100 we return elemental water
        if (rolled_number <= 4 or rolled_number >= 10) and randint(1, 100) >= 75:
            return RolledPlant(
                plant=elemental_water,
                quantity=2,
                additional_info="2 порции равняются 1 сосуду",
            )

        rolled_plant = self.roll[rolled_number]

        # If we rolled "common" terrain instead of plant, we need to roll it
        if isinstance(rolled_plant.plant, TerrainRollTable):
            rolled_plant = rolled_plant.plant.roll_plant(elemental_water)

        # We guarantee that RolledPlant.plant is instanse of Plant
        return rolled_plant


class RolledPlant(BaseModel):
    plant: Plant | TerrainRollTable
    quantity: int
    additional_info: Optional[str] = None
