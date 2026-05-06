import streamlit as st
from utils.utils import Data, Sidebar
from random import randint

st.set_page_config(page_title="Random Potion", page_icon="🧪")
DATA = Data()
Sidebar(DATA.translation)
TRANSLATION = DATA.translation
POTION_RANDOMIZER = TRANSLATION["potion_randomizer"]

if __name__ == "__main__":
    st.header(TRANSLATION["pages"]["potion_randomizer"])
    st.markdown(
        f"[{DATA.translation["text"]["source"]}](https://tentaculus.ru/archive/tables/random_potions.html)"
    )

    roll_button = st.button(DATA.translation["buttons"]["roll"])
    if roll_button:
        text = str(POTION_RANDOMIZER["description"])
        text = text.replace(
            "|form|", POTION_RANDOMIZER["form"][str(randint(1, 12))]
        )  # Форма
        text = text.replace(
            "|material|", POTION_RANDOMIZER["material"][str(randint(1, 12))]
        )
        text = text.replace("|color|", POTION_RANDOMIZER["color"][str(randint(1, 10))])
        text = text.replace("|cork|", POTION_RANDOMIZER["cork"][str(randint(1, 6))])
        text = text.replace(
            "|smell_intensity|",
            POTION_RANDOMIZER["smell_intensity"][str(randint(1, 10))],
        )
        text = text.replace("|smell|", POTION_RANDOMIZER["smell"][str(randint(1, 12))])
        text = text.replace("|taste|", POTION_RANDOMIZER["taste"][str(randint(1, 6))])
        text = text.replace(
            "|reaction|", POTION_RANDOMIZER["reaction"][str(randint(1, 20))]
        )

        for index in range(1, 4):
            ingredient_type = POTION_RANDOMIZER["ingredient_types"][str(randint(1, 8))]
            ingredient = POTION_RANDOMIZER[ingredient_type][
                str(randint(1, len(POTION_RANDOMIZER[ingredient_type])))
            ]
            text = text.replace(f"|ingredient{index}|", ingredient)

        st.success(text)
