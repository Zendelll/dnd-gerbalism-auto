import streamlit as st
from utils.utils import Data, Sidebar
import utils.constans as c
from utils.models import (
    Plant,
    PotionTypeEnum,
    EffectTypeEnum,
)

st.set_page_config(page_title="Alchemy", page_icon="⚗️")
DATA = Data()
Sidebar(DATA.translation)
TRANSLATION = DATA.translation
KEY_WORDS = TRANSLATION["key_words"]
STARTER_ALCHEMY_DIFFICULTY = 10


def clear_modifier_selectors(starting_index: int = 0):
    for i in range(starting_index, 3):
        st.session_state[f"mod{i}"] = False


if __name__ == "__main__":
    st.header(TRANSLATION["pages"]["alchemy"])

    # Alchemy type selector
    alchemy_type = st.selectbox(
        label=TRANSLATION["text"]["potion_type_selector"],
        options=[
            potion_type
            for potion_type in PotionTypeEnum
            if potion_type != PotionTypeEnum.all
        ],
        format_func=lambda potion_type: KEY_WORDS["potion_type"][potion_type.value],
    )

    # Plants with selected alchemy type
    # We not want bloodgrass here, because it handled separately
    related_plants = [
        plant
        for plant in DATA.plants.values()
        if (
            plant.potion_type == alchemy_type
            or (
                alchemy_type != PotionTypeEnum.magic
                and plant.potion_type == PotionTypeEnum.all
            )
        )
        and plant != DATA.plants[c.BLOODGRASS]
    ]

    # Unique plant that can be used as a second base in a potion
    bloodgrass = None
    if alchemy_type == PotionTypeEnum.potion:
        bloodgrass = st.checkbox(DATA.plants[c.BLOODGRASS].name)

    # Base plant selector
    modifiers = []
    base = st.selectbox(
        label=TRANSLATION["text"]["potion_base_ingredient_selector"],
        options=[""]
        + sorted(
            [
                plant
                for plant in related_plants
                if plant.effect_type == EffectTypeEnum.base
            ],
            key=lambda plant: plant.name,
        ),
        format_func=lambda plant: plant.name if isinstance(plant, Plant) else plant,
        on_change=clear_modifier_selectors,
    )

    # Modifiers selectors. 1 for magic potions, 3 for regular potions and poisons
    # Only Milkweed seeds and Quicksilver lichen can stack
    for mod_count in range(0, 3 if alchemy_type != PotionTypeEnum.magic else 1):
        modifiers.append(
            st.selectbox(
                label=f"{TRANSLATION["text"]["modifier_selector"]} {mod_count+1}:",
                options=[""]
                + sorted(
                    [
                        plant
                        for plant in related_plants
                        if plant.effect_type == EffectTypeEnum.modifier
                        and (
                            plant not in modifiers
                            or plant == DATA.plants[c.MILKWEED_SEEDS]
                            or plant == DATA.plants[c.QUICKSILVER_LICHEN]
                        )
                    ],
                    key=lambda plant: plant.name,
                ),
                format_func=lambda plant: (
                    plant.name if isinstance(plant, Plant) else plant
                ),
                disabled=not isinstance(base, Plant)
                or (
                    len(modifiers) > 0
                    and not isinstance(modifiers[len(modifiers) - 1], Plant)
                ),
                key=f"mod{mod_count}",
                on_change=clear_modifier_selectors,
                kwargs={"starting_index": mod_count + 1},
            )
        )

    difficulty = STARTER_ALCHEMY_DIFFICULTY

    # Write info of a base and potentonally bloodgrass
    if isinstance(base, Plant):
        st.success(base.effect_description)
        difficulty += base.difficulty_modifier
    if bloodgrass:
        st.success(DATA.plants[c.BLOODGRASS].effect_description)

    # Write info of every selected modifier
    for modifier in modifiers:
        if isinstance(modifier, Plant):
            st.warning(modifier.effect_description)
            difficulty += modifier.difficulty_modifier

    # Write resulting DC
    if isinstance(base, Plant):
        st.error(TRANSLATION["text"]["alchemy_dc"] + str(difficulty))
