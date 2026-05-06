import streamlit as st
import streamlit.components.v1 as components
from utils.utils import Data, Sidebar

st.set_page_config(page_title="Feedback", page_icon="📖")
DATA = Data()
Sidebar(DATA.translation)

if __name__ == "__main__":
    st.header(DATA.translation["pages"]["feedback"])
    st.success(DATA.translation["text"]["feedback"])
    components.iframe(
        "https://forms.yandex.ru/u/6574f103d04688604bcc834d/",
        width=700,
        height=800,
        scrolling=True,
    )
