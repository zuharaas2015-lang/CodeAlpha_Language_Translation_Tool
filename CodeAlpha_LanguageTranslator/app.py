import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translation Tool")

text = st.text_area("Enter text to translate")

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Arabic": "ar",
    "French": "fr",
    "German": "de"
}

source_lang = st.selectbox("Source Language", list(languages.keys()))
target_lang = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):

    if text:

        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("Translation Completed ✅")
        st.write("### Translated Text:")
        st.write(translated)

    else:
        st.warning("Please enter text")