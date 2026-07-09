import streamlit as st
import pyperclip

from utils.languages import LANGUAGES
from utils.translator import translate_text


st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌎",
    layout="centered"
)

st.title("🌎 AI Language Translation Tool")
st.markdown("### CodeAlpha Internship Project")

st.write("---")

input_text = st.text_area(
    "Enter Text",
    height=150,
    placeholder="Type text in any language..."
)

target_language = st.selectbox(
    "Translate To",
    list(LANGUAGES.keys())
)

if st.button("Translate", use_container_width=True):

    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:

        translated_text = translate_text(
            input_text,
            LANGUAGES[target_language]
        )

        st.success("Translation Completed!")

        st.text_area(
            "Translated Text",
            translated_text,
            height=150
        )

        if st.button("📋 Copy Translation"):
            pyperclip.copy(translated_text)
            st.success("Copied to clipboard!")