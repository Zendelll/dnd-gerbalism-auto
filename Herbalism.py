import streamlit as st
from utils.utils import Data, Sidebar, write_plant_info
import utils.constans as c
from utils.models import (
    TerrainTypesEnum,
    RolledPlant,
)

st.set_page_config(
    page_title="Herbalism",
    page_icon="🌱",
)
DATA = Data()
Sidebar(DATA.translation)
KEY_WORDS = DATA.translation["key_words"]
TERRAIN_TEXT = DATA.translation["key_words"]["terrain"]


def short_rules_block():
    st.markdown(
        f'<details><summary>{DATA.translation["buttons"]["short_rules"]}</summary>'
        + DATA.translation["text"]["herbalism_rule"]
        + "</details>",
        unsafe_allow_html=True,
    )


def write_plant(rolled_plant: RolledPlant):
    plant = rolled_plant.plant
    # Rolled plant base info
    st.warning(
        f"**{plant.name}**"
        + (
            f" -- {rolled_plant.quantity} {KEY_WORDS['units']}"
            if rolled_plant.quantity > 1
            else ""
        )
        + (
            f" -- *{rolled_plant.additional_info}*"
            if rolled_plant.additional_info
            else ""
        )
    )
    write_plant_info(plant, KEY_WORDS)


if __name__ == "__main__":

    st.header(DATA.translation["pages"]["herbalism"])
    short_rules_block()

    # Terrain Selector
    selected_terrain = st.selectbox(
        label=TERRAIN_TEXT["terrain"],
        options=[
            terrain
            for terrain in DATA.terrain_tables
            if terrain.terrain_type != TerrainTypesEnum.common
        ],
        format_func=lambda terrain: TERRAIN_TEXT[terrain.terrain_type.value],
    )

    # Roll Button
    if st.button(DATA.translation["buttons"]["roll"]):
        write_plant(selected_terrain.roll_plant(DATA.plants[c.ELEMENTAL_WATER]))
