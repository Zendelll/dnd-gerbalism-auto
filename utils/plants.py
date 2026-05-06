import streamlit as st
from utils import constans as c
from utils.models import (
    RarityEnum,
    PotionTypeEnum,
    EffectTypeEnum,
    TerrainTypesEnum,
    Plant,
)


def load_plants(translation_plants) -> dict[str, Plant]:
    plants = {}

    plants[c.BLOODGRASS] = _create_plant(
        translation_plants[c.BLOODGRASS],
        RarityEnum.common,
        PotionTypeEnum.potion,
        EffectTypeEnum.base,
        0,
        [TerrainTypesEnum.common],
    )

    plants[c.CHROMUS_SLIME] = _create_plant(
        translation_plants[c.CHROMUS_SLIME],
        RarityEnum.rare,
        PotionTypeEnum.all,
        EffectTypeEnum.modifier,
        4,
        [TerrainTypesEnum.water, TerrainTypesEnum.coastal, TerrainTypesEnum.underdark],
    )

    plants[c.DRIED_EPHEDRA] = _create_plant(
        translation_plants[c.DRIED_EPHEDRA],
        RarityEnum.uncommon,
        PotionTypeEnum.potion,
        EffectTypeEnum.modifier,
        2,
        [TerrainTypesEnum.desert, TerrainTypesEnum.mountain],
    )

    plants[c.EMETIC_WAX] = _create_plant(
        translation_plants[c.EMETIC_WAX],
        RarityEnum.common,
        PotionTypeEnum.all,
        EffectTypeEnum.modifier,
        1,
        [TerrainTypesEnum.forest, TerrainTypesEnum.swamp],
    )

    plants[c.FENNEL_SILK] = _create_plant(
        translation_plants[c.FENNEL_SILK],
        RarityEnum.common,
        PotionTypeEnum.potion,
        EffectTypeEnum.base,
        2,
        [TerrainTypesEnum.arctic, TerrainTypesEnum.underdark],
    )

    plants[c.GENGKO_BRUSH] = _create_plant(
        translation_plants[c.GENGKO_BRUSH],
        RarityEnum.uncommon,
        PotionTypeEnum.potion,
        EffectTypeEnum.modifier,
        2,
        [TerrainTypesEnum.hills, TerrainTypesEnum.underdark],
    )

    plants[c.HYANCINTH_NECTAR] = _create_plant(
        translation_plants[c.HYANCINTH_NECTAR],
        RarityEnum.common,
        PotionTypeEnum.potion,
        EffectTypeEnum.base,
        1,
        [TerrainTypesEnum.water, TerrainTypesEnum.coastal, TerrainTypesEnum.grasslands],
    )

    plants[c.LAVENDER_SPRIG] = _create_plant(
        translation_plants[c.LAVENDER_SPRIG],
        RarityEnum.common,
        PotionTypeEnum.all,
        EffectTypeEnum.modifier,
        -2,
        [TerrainTypesEnum.coastal, TerrainTypesEnum.grasslands, TerrainTypesEnum.hills],
    )

    plants[c.MANDRAKE_ROOT] = _create_plant(
        translation_plants[c.MANDRAKE_ROOT],
        RarityEnum.common,
        PotionTypeEnum.potion,
        EffectTypeEnum.base,
        0,
        [TerrainTypesEnum.common],
    )

    plants[c.MILKWEED_SEEDS] = _create_plant(
        translation_plants[c.MILKWEED_SEEDS],
        RarityEnum.common,
        PotionTypeEnum.potion,
        EffectTypeEnum.modifier,
        2,
        [TerrainTypesEnum.common],
    )

    plants[c.WILD_SAGEROOT] = _create_plant(
        translation_plants[c.WILD_SAGEROOT],
        RarityEnum.common,
        PotionTypeEnum.potion,
        EffectTypeEnum.base,
        0,
        [TerrainTypesEnum.common],
    )

    plants[c.ARCTIC_CREEPER] = _create_plant(
        translation_plants[c.ARCTIC_CREEPER],
        RarityEnum.common,
        PotionTypeEnum.poison,
        EffectTypeEnum.modifier,
        2,
        [TerrainTypesEnum.arctic, TerrainTypesEnum.mountain],
    )

    plants[c.AMANITA_CAP] = _create_plant(
        translation_plants[c.AMANITA_CAP],
        RarityEnum.common,
        PotionTypeEnum.poison,
        EffectTypeEnum.modifier,
        1,
        [TerrainTypesEnum.swamp, TerrainTypesEnum.coastal],
    )

    plants[c.BASILISK_BREATH] = _create_plant(
        translation_plants[c.BASILISK_BREATH],
        RarityEnum.very_rare,
        PotionTypeEnum.poison,
        EffectTypeEnum.base,
        5,
        [TerrainTypesEnum.mountain],
    )

    plants[c.CACTUS_JUICE] = _create_plant(
        translation_plants[c.CACTUS_JUICE],
        RarityEnum.common,
        PotionTypeEnum.poison,
        EffectTypeEnum.modifier,
        2,
        [TerrainTypesEnum.desert, TerrainTypesEnum.grasslands],
    )

    plants[c.DRAKUS_FLOWER] = _create_plant(
        translation_plants[c.DRAKUS_FLOWER],
        RarityEnum.common,
        PotionTypeEnum.poison,
        EffectTypeEnum.modifier,
        2,
        [
            TerrainTypesEnum.desert,
            TerrainTypesEnum.grasslands,
            TerrainTypesEnum.mountain,
        ],
    )

    plants[c.FROZEN_SEEDLINGS] = _create_plant(
        translation_plants[c.FROZEN_SEEDLINGS],
        RarityEnum.rare,
        PotionTypeEnum.poison,
        EffectTypeEnum.modifier,
        4,
        [TerrainTypesEnum.arctic, TerrainTypesEnum.mountain],
    )

    plants[c.HARRADA_LEAF] = _create_plant(
        translation_plants[c.HARRADA_LEAF],
        RarityEnum.common,
        PotionTypeEnum.poison,
        EffectTypeEnum.modifier,
        1,
        [TerrainTypesEnum.forest],
    )

    plants[c.QUICKSILVER_LICHEN] = _create_plant(
        translation_plants[c.QUICKSILVER_LICHEN],
        RarityEnum.uncommon,
        PotionTypeEnum.poison,
        EffectTypeEnum.modifier,
        3,
        [TerrainTypesEnum.common],
    )

    plants[c.RADIANT_SYNTHSEED] = _create_plant(
        translation_plants[c.RADIANT_SYNTHSEED],
        RarityEnum.rare,
        PotionTypeEnum.poison,
        EffectTypeEnum.modifier,
        2,
        [TerrainTypesEnum.underdark],
    )

    plants[c.SPINEFLOWER_BERRIES] = _create_plant(
        translation_plants[c.SPINEFLOWER_BERRIES],
        RarityEnum.uncommon,
        PotionTypeEnum.poison,
        EffectTypeEnum.modifier,
        3,
        [TerrainTypesEnum.desert, TerrainTypesEnum.swamp],
    )

    plants[c.WYRMTONGUE_PETALS] = _create_plant(
        translation_plants[c.WYRMTONGUE_PETALS],
        RarityEnum.common,
        PotionTypeEnum.poison,
        EffectTypeEnum.base,
        0,
        [TerrainTypesEnum.common],
    )

    plants[c.ARROW_ROOT] = _create_plant(
        translation_plants[c.ARROW_ROOT],
        RarityEnum.uncommon,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        2,
        [TerrainTypesEnum.desert, TerrainTypesEnum.forest, TerrainTypesEnum.grasslands],
    )

    plants[c.BLUE_TOADSHADE] = _create_plant(
        translation_plants[c.BLUE_TOADSHADE],
        RarityEnum.rare,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        3,
        [TerrainTypesEnum.coastal, TerrainTypesEnum.forest, TerrainTypesEnum.swamp],
    )

    plants[c.COSMOS_GLOND] = _create_plant(
        translation_plants[c.COSMOS_GLOND],
        RarityEnum.rare,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        3,
        [TerrainTypesEnum.water, TerrainTypesEnum.coastal, TerrainTypesEnum.desert],
    )

    plants[c.DEVILS_BLOODLEAF] = _create_plant(
        translation_plants[c.DEVILS_BLOODLEAF],
        RarityEnum.very_rare,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        5,
        [TerrainTypesEnum.hills, TerrainTypesEnum.swamp, TerrainTypesEnum.underdark],
    )

    plants[c.ELEMENTAL_WATER] = _create_plant(
        translation_plants[c.ELEMENTAL_WATER],
        RarityEnum.rare,
        PotionTypeEnum.magic,
        EffectTypeEnum.base,
        3,
        [TerrainTypesEnum.common],
    )

    plants[c.FIENDS_IVY] = _create_plant(
        translation_plants[c.FIENDS_IVY],
        RarityEnum.rare,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        4,
        [TerrainTypesEnum.arctic, TerrainTypesEnum.underdark],
    )

    plants[c.HYDRATHISTLE] = _create_plant(
        translation_plants[c.HYDRATHISTLE],
        RarityEnum.uncommon,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        2,
        [TerrainTypesEnum.water, TerrainTypesEnum.coastal, TerrainTypesEnum.swamp],
    )

    plants[c.IRONWOOD_HEART] = _create_plant(
        translation_plants[c.IRONWOOD_HEART],
        RarityEnum.uncommon,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        3,
        [TerrainTypesEnum.arctic, TerrainTypesEnum.forest, TerrainTypesEnum.hills],
    )

    plants[c.LUMINOUS_CAP_DUST] = _create_plant(
        translation_plants[c.LUMINOUS_CAP_DUST],
        RarityEnum.rare,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        4,
        [TerrainTypesEnum.mountain, TerrainTypesEnum.underdark],
    )

    plants[c.MORTFLESH_POWDER] = _create_plant(
        translation_plants[c.MORTFLESH_POWDER],
        RarityEnum.very_rare,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        5,
        [TerrainTypesEnum.arctic, TerrainTypesEnum.underdark],
    )

    plants[c.NIGHTSHADE_BERRIES] = _create_plant(
        translation_plants[c.NIGHTSHADE_BERRIES],
        RarityEnum.uncommon,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        3,
        [TerrainTypesEnum.forest, TerrainTypesEnum.hills],
    )

    plants[c.PRIMORDIAL_BALM] = _create_plant(
        translation_plants[c.PRIMORDIAL_BALM],
        RarityEnum.rare,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        4,
        [TerrainTypesEnum.mountain, TerrainTypesEnum.swamp, TerrainTypesEnum.underdark],
    )

    plants[c.ROCK_VINE] = _create_plant(
        translation_plants[c.ROCK_VINE],
        RarityEnum.rare,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        4,
        [TerrainTypesEnum.hills, TerrainTypesEnum.mountain],
    )

    plants[c.SCILLIA_BEANS] = _create_plant(
        translation_plants[c.SCILLIA_BEANS],
        RarityEnum.common,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        1,
        [TerrainTypesEnum.desert, TerrainTypesEnum.grasslands],
    )

    plants[c.SILVER_HIBISCUS] = _create_plant(
        translation_plants[c.SILVER_HIBISCUS],
        RarityEnum.rare,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        4,
        [TerrainTypesEnum.arctic, TerrainTypesEnum.underdark],
    )

    plants[c.TAIL_LEAF] = _create_plant(
        translation_plants[c.TAIL_LEAF],
        RarityEnum.very_rare,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        5,
        [TerrainTypesEnum.grasslands, TerrainTypesEnum.hills],
    )

    plants[c.VERDANT_NETTLE] = _create_plant(
        translation_plants[c.VERDANT_NETTLE],
        RarityEnum.uncommon,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        2,
        [TerrainTypesEnum.forest],
    )

    plants[c.VOIDROOT] = _create_plant(
        translation_plants[c.VOIDROOT],
        RarityEnum.very_rare,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        5,
        [TerrainTypesEnum.arctic, TerrainTypesEnum.desert],
    )

    plants[c.WISP_STALKS] = _create_plant(
        translation_plants[c.WISP_STALKS],
        RarityEnum.very_rare,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        5,
        [TerrainTypesEnum.forest, TerrainTypesEnum.underdark],
    )

    plants[c.WRACKWORT_BULBS] = _create_plant(
        translation_plants[c.WRACKWORT_BULBS],
        RarityEnum.rare,
        PotionTypeEnum.magic,
        EffectTypeEnum.modifier,
        4,
        [TerrainTypesEnum.water, TerrainTypesEnum.coastal, TerrainTypesEnum.swamp],
    )

    return plants


def _create_plant(
    translation: dict[str, str],
    rarity: RarityEnum,
    potion_type: PotionTypeEnum,
    effect_type: EffectTypeEnum,
    difficulty_modifier: int,
    terrain_types: list[TerrainTypesEnum],
) -> Plant:
    return Plant(
        name=translation["name"],
        description=translation["description"],
        rarity=rarity,
        potion_type=potion_type,
        effect_type=effect_type,
        effect_description=translation["effect_description"],
        difficulty_modifier=difficulty_modifier,
        terrain_types=terrain_types,
    )
