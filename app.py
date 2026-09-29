"""
CodeAlpha - Language Translation Tool
Task 1: AI Internship

A simple web app that lets a user type text, pick a source and target
language, and get an instant translation.

How it works (no ML training involved):
- deep_translator.MyMemoryTranslator sends the text to the MyMemory
  translation service (a free, no-API-key-required translation
  database/service) over the internet and returns the translated
  result. We switched to MyMemory instead of Google Translate because
  Google's free/unofficial endpoint aggressively rate-limits and
  blocks IPs on many networks - MyMemory is built for this kind of
  free, no-key usage and is much more reliable.
- Streamlit turns a plain Python script into a web page - each time the
  user interacts with a widget (button, dropdown), Streamlit re-runs this
  file top to bottom and redraws the UI with the new values.
"""

import streamlit as st
from deep_translator import MyMemoryTranslator

# ---------------------------------------------------------------------
# 1. Page setup
# ---------------------------------------------------------------------
st.set_page_config(page_title="CodeAlpha Language Translator", page_icon="🌐")
st.title("🌐 Language Translation Tool")
st.caption("CodeAlpha AI Internship - Task 1")

# ---------------------------------------------------------------------
# 2. Supported languages
# This dictionary is bundled locally with the library - looking it up
# does NOT make a network request, so it's safe to call on every rerun.
# {"english": "en-GB", "french": "fr-FR", ...}
# ---------------------------------------------------------------------
LANGUAGES = MyMemoryTranslator(source="english", target="french").get_supported_languages(
    as_dict=True
)

language_names = sorted(LANGUAGES.keys())

# ---------------------------------------------------------------------
# 3. User input widgets
# Note: MyMemory (unlike Google) requires an explicit source language -
# it doesn't support "auto-detect" - so we default to English instead.
# ---------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    default_source_index = language_names.index("english") if "english" in language_names else 0
    source_lang = st.selectbox(
        "Translate from",
        options=language_names,
        index=default_source_index,
    )

with col2:
    default_target_index = language_names.index("french") if "french" in language_names else 0
    target_lang = st.selectbox(
        "Translate to",
        options=language_names,
        index=default_target_index,
    )

text_input = st.text_area(
    "Enter text to translate",
    height=150,
    placeholder="Type or paste your text here...",
)

# ---------------------------------------------------------------------
# 4. Translate button + logic
# ---------------------------------------------------------------------
if st.button("Translate", type="primary"):
    if not text_input.strip():
        st.warning("Please enter some text first.")
    else:
        try:
            source_code = LANGUAGES[source_lang]
            target_code = LANGUAGES[target_lang]

            translated_text = MyMemoryTranslator(
                source=source_code, target=target_code
            ).translate(text_input)

            st.subheader("Translated Text")
            st.success(translated_text)

            # Optional feature from the task brief: a copy-friendly box
            st.text_area("Copy from here:", value=translated_text, height=100)

        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.divider()
st.caption("Built with Python, Streamlit, and deep-translator (MyMemory).")
