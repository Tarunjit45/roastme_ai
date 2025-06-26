# roast_utils.py
import google.generativeai as genai
import pyttsx3
import re

# Configure your Gemini API key
genai.configure(api_key="AIzaSyDaMv5ixTtfaS8HCHPa87GeKk5B798WCAI")
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
    # Remove any side text like (..), [..], {..}
    cleaned_text = re.sub(r"[\(\[\{].*?[\)\]\}]", "", text)

    engine = pyttsx3.init()

    # Use a fun, chill-sounding voice if available
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'zira' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.setProperty('rate', 165)
    engine.setProperty('volume', 1.0)

    engine.save_to_file(cleaned_text.strip(), audio_path)
    engine.runAndWait()
