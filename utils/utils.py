import streamlit as st
import json
from utils.models import Plant, TerrainRollTable, PotionTypeEnum
from utils.terrains import load_terrain_tables
from utils.plants import load_plants


class Data:
    translation: dict[str, dict] = {}
    plants: dict[str, Plant] = {}
    terrain_tables: list[TerrainRollTable] = []

    def __init__(self):
        self.language_selector()
        self.load_translation(st.session_state["lang"])
        self.plants = load_plants(self.translation["plants"])
        self.terrain_tables = load_terrain_tables(self.plants)

    def language_selector(self):
        if "lang" not in st.session_state:
            st.session_state["lang"] = "ru"
        with st.sidebar:
            col1, col2 = st.columns(2)
            if col1.button("Ru"):
                st.session_state["lang"] = "ru"
                st.rerun()
            if col2.button("En"):
                st.session_state["lang"] = "en"
                st.rerun()

    def load_translation(self, lang):
        with open("translation.json", "r") as j:
            self.translation = json.load(j)[lang]


class Sidebar:
    links = {
        "herbalism": "Herbalism.py",
        "alchemy": "pages/Alchemy.py",
        "plant_library": "pages/Plant_library.py",
        "potion_randomizer": "pages/Potion_randomizer.py",
        "feedback": "pages/feedback.py",
    }

    def __init__(self, translation: dict):
        self.sidebar_pages(translation)

    def sidebar_pages(self, translation: dict):
        st.markdown(
            """<style>div[data-testid="stSidebarNav"] {display: none;}</style>""",
            unsafe_allow_html=True,
        )
        pages_names = translation["pages"]
        with st.sidebar:
            for name, link in self.links.items():
                st.page_link(link, label=pages_names[name])


def write_plant_info(plant: Plant, key_words_translation: dict):
    potion_type_to_color_map = {
        PotionTypeEnum.all: "orange",
        PotionTypeEnum.magic: "blue",
        PotionTypeEnum.poison: "green",
        PotionTypeEnum.potion: "red",
    }
    # Plant potion type
    st.write(
        f":{potion_type_to_color_map[plant.potion_type]}[{key_words_translation["potion_type"][plant.potion_type.value]}]"
    )
    # Effect description and flavor description
    st.success(plant.description)
    st.error(plant.effect_description)
    # Difficulty, rarity and terrain info
    st.code(f"""{key_words_translation["difficulty"]}: {plant.difficulty_modifier}
{key_words_translation["rarity"]["rarity"]}: {key_words_translation["rarity"][plant.rarity.value]}
{key_words_translation["terrain"]["terrain"]}: {", ".join([key_words_translation["terrain"][terrain.value] for terrain in plant.terrain_types])}
""")
