import streamlit as st
from roast_utils import generate_roast, roast_to_speech
import os

st.set_page_config(page_title="RoastMe.AI 😎", layout="centered")

st.title("🔥 RoastMe.AI 🔥")
st.subheader("Give us your vibe, we'll roast you alive... humorously 😈")

name = st.text_input("Your Name")
bio = st.text_area("Something About You (funny/weird stuff encouraged!)")

if st.button("🔥 Roast Me"):
    if not name or not bio:
        st.warning("Tell us something to roast you about!")
    else:
        with st.spinner("Cooking up a roast..."):
            roast_text = generate_roast(name, bio)

            st.success("Here's your roast:")
            st.markdown(f"**{roast_text}**")

            audio_path = "roast.mp3"
            roast_to_speech(roast_text, audio_path)

            st.audio(audio_path, format="audio/mp3")
