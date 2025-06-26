import google.generativeai as genai
from gtts import gTTS
import re
import streamlit as st

# Load API key from Streamlit secrets
genai.configure(api_key=st.secrets["AIzaSyDaMv5ixTtfaS8HCHPa87GeKk5B798WCAI"])
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_roast(name, bio):
    prompt = f"""
    You're a sarcastic, witty stand-up comedian.
    Roast this person in a light-hearted, funny way.
    Avoid anything offensive. Be clever and creative.

    Name: {name}
    Description: {bio}
    """
    response = model.generate_content(prompt)
    return response.text.strip()

def roast_to_speech(text, audio_path):
    cleaned_text = re.sub(r"[\(\[\{].*?[\)\]\}]", "", text)
    tts = gTTS(text=cleaned_text.strip(), lang='en', slow=False)
    tts.save(audio_path)
