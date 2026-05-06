import streamlit as st
from utils.utils import Data, Sidebar, write_plant_info

st.set_page_config(page_title="Library", page_icon="🌿")
DATA = Data()
Sidebar(DATA.translation)
TRANSLATION = DATA.translation
KEY_WORDS = TRANSLATION["key_words"]

if __name__ == "__main__":
    st.header(TRANSLATION["pages"]["plant_library"])
    selected_plant = st.selectbox(
        label=KEY_WORDS["plant"],
        options=sorted(
            DATA.plants.values(),
            key=lambda plant: plant.name,
        ),
        format_func=lambda plant: plant.name,
    )
    write_plant_info(selected_plant, KEY_WORDS)
