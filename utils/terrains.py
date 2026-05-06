from random import randint
from utils import constans as c
from utils.models import (
    Plant,
    TerrainTypesEnum,
    TerrainRollTable,
    RolledPlant,
)


def load_terrain_tables(plants: dict[str, Plant]) -> list[TerrainRollTable]:
    terrain_tables = []
    common_roll_table = TerrainRollTable(
        terrain_type=TerrainTypesEnum.common,
        roll={
            2: RolledPlant(plant=plants[c.MANDRAKE_ROOT], quantity=1),
            3: RolledPlant(plant=plants[c.QUICKSILVER_LICHEN], quantity=1),
            4: RolledPlant(plant=plants[c.QUICKSILVER_LICHEN], quantity=1),
            5: RolledPlant(plant=plants[c.WILD_SAGEROOT], quantity=1),
            6: RolledPlant(plant=plants[c.WILD_SAGEROOT], quantity=1),
            7: RolledPlant(plant=plants[c.BLOODGRASS], quantity=1),
            8: RolledPlant(plant=plants[c.WYRMTONGUE_PETALS], quantity=1),
            9: RolledPlant(plant=plants[c.WYRMTONGUE_PETALS], quantity=1),
            10: RolledPlant(plant=plants[c.MILKWEED_SEEDS], quantity=1),
            11: RolledPlant(plant=plants[c.MILKWEED_SEEDS], quantity=1),
            12: RolledPlant(plant=plants[c.MANDRAKE_ROOT], quantity=1),
        },
    )
    terrain_tables.append(common_roll_table)
    terrain_tables.append(
        TerrainRollTable(
            terrain_type=TerrainTypesEnum.arctic,
            roll={
                2: RolledPlant(plant=plants[c.SILVER_HIBISCUS], quantity=1),
                3: RolledPlant(plant=plants[c.MORTFLESH_POWDER], quantity=1),
                4: RolledPlant(plant=plants[c.IRONWOOD_HEART], quantity=1),
                5: RolledPlant(plant=plants[c.FROZEN_SEEDLINGS], quantity=2),
                6: RolledPlant(plant=common_roll_table, quantity=1),
                7: RolledPlant(plant=common_roll_table, quantity=1),
                8: RolledPlant(plant=common_roll_table, quantity=1),
                9: RolledPlant(plant=plants[c.ARCTIC_CREEPER], quantity=2),
                10: RolledPlant(plant=plants[c.FENNEL_SILK], quantity=1),
                11: RolledPlant(plant=plants[c.FIENDS_IVY], quantity=1),
                12: RolledPlant(plant=plants[c.VOIDROOT], quantity=1),
            },
        )
    )

    terrain_tables.append(
        TerrainRollTable(
            terrain_type=TerrainTypesEnum.water,
            roll={
                2: RolledPlant(plant=plants[c.HYDRATHISTLE], quantity=randint(1, 2)),
                3: RolledPlant(plant=plants[c.HYANCINTH_NECTAR], quantity=1),
                4: RolledPlant(plant=plants[c.HYANCINTH_NECTAR], quantity=1),
                5: RolledPlant(plant=plants[c.CHROMUS_SLIME], quantity=randint(1, 2)),
                6: RolledPlant(plant=common_roll_table, quantity=1),
                7: RolledPlant(plant=common_roll_table, quantity=1),
                8: RolledPlant(plant=common_roll_table, quantity=1),
                9: RolledPlant(plant=common_roll_table, quantity=1),
                10: RolledPlant(plant=common_roll_table, quantity=1),
                11: RolledPlant(plant=plants[c.WRACKWORT_BULBS], quantity=1),
                12: RolledPlant(plant=plants[c.COSMOS_GLOND], quantity=1),
            },
        )
    )

    terrain_tables.append(
        TerrainRollTable(
            terrain_type=TerrainTypesEnum.coastal,
            roll={
                2: RolledPlant(plant=plants[c.HYDRATHISTLE], quantity=randint(1, 2)),
                3: RolledPlant(plant=plants[c.AMANITA_CAP], quantity=1),
                4: RolledPlant(plant=plants[c.HYANCINTH_NECTAR], quantity=1),
                5: RolledPlant(plant=plants[c.CHROMUS_SLIME], quantity=randint(1, 2)),
                6: RolledPlant(plant=common_roll_table, quantity=1),
                7: RolledPlant(plant=common_roll_table, quantity=1),
                8: RolledPlant(plant=common_roll_table, quantity=1),
                9: RolledPlant(plant=plants[c.LAVENDER_SPRIG], quantity=1),
                10: RolledPlant(plant=plants[c.BLUE_TOADSHADE], quantity=1),
                11: RolledPlant(plant=plants[c.WRACKWORT_BULBS], quantity=1),
                12: RolledPlant(plant=plants[c.COSMOS_GLOND], quantity=1),
            },
        )
    )

    terrain_tables.append(
        TerrainRollTable(
            terrain_type=TerrainTypesEnum.desert,
            roll={
                2: RolledPlant(plant=plants[c.COSMOS_GLOND], quantity=1),
                3: RolledPlant(plant=plants[c.ARROW_ROOT], quantity=1),
                4: RolledPlant(plant=plants[c.DRIED_EPHEDRA], quantity=1),
                5: RolledPlant(plant=plants[c.CACTUS_JUICE], quantity=2),
                6: RolledPlant(plant=common_roll_table, quantity=1),
                7: RolledPlant(plant=common_roll_table, quantity=1),
                8: RolledPlant(plant=common_roll_table, quantity=1),
                9: RolledPlant(plant=plants[c.DRAKUS_FLOWER], quantity=1),
                10: RolledPlant(plant=plants[c.SCILLIA_BEANS], quantity=1),
                11: RolledPlant(plant=plants[c.SPINEFLOWER_BERRIES], quantity=1),
                12: RolledPlant(
                    plant=plants[c.VOIDROOT],
                    quantity=1,
                    additional_info=f"+ 1 roll={plants[c.VOIDROOT].name}",
                ),
            },
        )
    )

    terrain_tables.append(
        TerrainRollTable(
            terrain_type=TerrainTypesEnum.forest,
            roll={
                2: RolledPlant(plant=plants[c.HARRADA_LEAF], quantity=1),
                3: RolledPlant(plant=plants[c.NIGHTSHADE_BERRIES], quantity=1),
                4: RolledPlant(plant=plants[c.EMETIC_WAX], quantity=1),
                5: RolledPlant(plant=plants[c.VERDANT_NETTLE], quantity=1),
                6: RolledPlant(plant=common_roll_table, quantity=1),
                7: RolledPlant(plant=common_roll_table, quantity=1),
                8: RolledPlant(plant=common_roll_table, quantity=1),
                9: RolledPlant(plant=plants[c.ARROW_ROOT], quantity=1),
                10: RolledPlant(plant=plants[c.IRONWOOD_HEART], quantity=1),
                11: RolledPlant(plant=plants[c.BLUE_TOADSHADE], quantity=1),
                12: RolledPlant(
                    plant=plants[c.WISP_STALKS],
                    quantity=2,
                    additional_info="Днем перебросить",
                ),
            },
        )
    )

    terrain_tables.append(
        TerrainRollTable(
            terrain_type=TerrainTypesEnum.grasslands,
            roll={
                2: RolledPlant(plant=plants[c.HARRADA_LEAF], quantity=1),
                3: RolledPlant(plant=plants[c.DRAKUS_FLOWER], quantity=1),
                4: RolledPlant(plant=plants[c.LAVENDER_SPRIG], quantity=2),
                5: RolledPlant(plant=plants[c.ARROW_ROOT], quantity=1),
                6: RolledPlant(plant=common_roll_table, quantity=1),
                7: RolledPlant(plant=common_roll_table, quantity=1),
                8: RolledPlant(plant=common_roll_table, quantity=1),
                9: RolledPlant(plant=plants[c.SCILLIA_BEANS], quantity=2),
                10: RolledPlant(plant=plants[c.CACTUS_JUICE], quantity=1),
                11: RolledPlant(plant=plants[c.TAIL_LEAF], quantity=1),
                12: RolledPlant(plant=plants[c.HYANCINTH_NECTAR], quantity=1),
            },
        )
    )

    terrain_tables.append(
        TerrainRollTable(
            terrain_type=TerrainTypesEnum.hills,
            roll={
                2: RolledPlant(plant=plants[c.DEVILS_BLOODLEAF], quantity=1),
                3: RolledPlant(plant=plants[c.NIGHTSHADE_BERRIES], quantity=1),
                4: RolledPlant(plant=plants[c.TAIL_LEAF], quantity=2),
                5: RolledPlant(plant=plants[c.LAVENDER_SPRIG], quantity=1),
                6: RolledPlant(plant=common_roll_table, quantity=1),
                7: RolledPlant(plant=common_roll_table, quantity=1),
                8: RolledPlant(plant=common_roll_table, quantity=1),
                9: RolledPlant(plant=plants[c.IRONWOOD_HEART], quantity=1),
                10: RolledPlant(plant=plants[c.GENGKO_BRUSH], quantity=1),
                11: RolledPlant(plant=plants[c.ROCK_VINE], quantity=2),
                12: RolledPlant(plant=plants[c.HARRADA_LEAF], quantity=1),
            },
        )
    )

    terrain_tables.append(
        TerrainRollTable(
            terrain_type=TerrainTypesEnum.mountain,
            roll={
                2: RolledPlant(plant=plants[c.BASILISK_BREATH], quantity=1),
                3: RolledPlant(plant=plants[c.FROZEN_SEEDLINGS], quantity=2),
                4: RolledPlant(plant=plants[c.ARCTIC_CREEPER], quantity=2),
                5: RolledPlant(plant=plants[c.DRIED_EPHEDRA], quantity=1),
                6: RolledPlant(plant=common_roll_table, quantity=1),
                7: RolledPlant(plant=common_roll_table, quantity=1),
                8: RolledPlant(plant=common_roll_table, quantity=1),
                9: RolledPlant(plant=plants[c.DRAKUS_FLOWER], quantity=1),
                10: RolledPlant(
                    plant=plants[c.LUMINOUS_CAP_DUST],
                    quantity=1,
                    additional_info="2 штуки в пещерах",
                ),
                11: RolledPlant(plant=plants[c.ROCK_VINE], quantity=1),
                12: RolledPlant(plant=plants[c.PRIMORDIAL_BALM], quantity=1),
            },
        )
    )

    terrain_tables.append(
        TerrainRollTable(
            terrain_type=TerrainTypesEnum.swamp,
            roll={
                2: RolledPlant(plant=plants[c.DEVILS_BLOODLEAF], quantity=1),
                3: RolledPlant(plant=plants[c.SPINEFLOWER_BERRIES], quantity=1),
                4: RolledPlant(plant=plants[c.EMETIC_WAX], quantity=1),
                5: RolledPlant(plant=plants[c.AMANITA_CAP], quantity=2),
                6: RolledPlant(plant=common_roll_table, quantity=1),
                7: RolledPlant(plant=common_roll_table, quantity=1),
                8: RolledPlant(plant=common_roll_table, quantity=1),
                9: RolledPlant(plant=plants[c.BLUE_TOADSHADE], quantity=2),
                10: RolledPlant(plant=plants[c.WRACKWORT_BULBS], quantity=1),
                11: RolledPlant(
                    plant=plants[c.HYDRATHISTLE],
                    quantity=1,
                    additional_info="2 штуки в дождь",
                ),
                12: RolledPlant(plant=plants[c.PRIMORDIAL_BALM], quantity=1),
            },
        )
    )

    terrain_tables.append(
        TerrainRollTable(
            terrain_type=TerrainTypesEnum.underdark,
            roll={
                2: RolledPlant(plant=plants[c.PRIMORDIAL_BALM], quantity=2),
                3: RolledPlant(plant=plants[c.SILVER_HIBISCUS], quantity=1),
                4: RolledPlant(plant=plants[c.DEVILS_BLOODLEAF], quantity=1),
                5: RolledPlant(plant=plants[c.CHROMUS_SLIME], quantity=1),
                6: RolledPlant(plant=plants[c.MORTFLESH_POWDER], quantity=2),
                7: RolledPlant(plant=plants[c.FENNEL_SILK], quantity=1),
                8: RolledPlant(plant=plants[c.FIENDS_IVY], quantity=1),
                9: RolledPlant(plant=plants[c.GENGKO_BRUSH], quantity=1),
                10: RolledPlant(plant=plants[c.LUMINOUS_CAP_DUST], quantity=2),
                11: RolledPlant(plant=plants[c.RADIANT_SYNTHSEED], quantity=1),
                12: RolledPlant(plant=plants[c.WISP_STALKS], quantity=1),
            },
        )
    )
    return terrain_tables
