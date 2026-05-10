import streamlit as st
import pandas as pd
from model import predict_mudra
from deep_translator import GoogleTranslator
import os

# -----------------------------
# 🪷 Page Config
# -----------------------------
st.set_page_config(
    page_title="Bharatanatyam Mudra Predictor",
    page_icon="🪷"
)

# -----------------------------
# 🎨 Header
# -----------------------------
st.markdown("""
<h1 style='text-align: center; color: #8B0000;'>
🪷 Mudra NLP
</h1>

<h3 style='text-align: center; color: #444;'>
Bharatanatyam Mudra Predictor
</h3>

<p style='text-align: center; font-size:18px; color: #555;'>
Describe a Bharatanatyam hand gesture in <b>any language</b> to predict its mudra.
</p>
""", unsafe_allow_html=True)

# -----------------------------
# 📂 Load Dataset
# -----------------------------
data = pd.read_csv("dataset.csv")

# -----------------------------
# 🌍 Mudra Name Translation
# -----------------------------
mudra_names_translation = {
    "Pataka": {"kn": "ಪತಾಕ", "hi": "पताका", "ta": "பதாகா"},
    "Tripataka": {"kn": "ತ್ರಿಪತಾಕ", "hi": "त्रिपताका", "ta": "திரிபதாகா"},
    "Ardhapataka": {"kn": "ಅರ್ಧಪತಾಕ", "hi": "अर्धपताका", "ta": "அர்த்தபதாகா"},
    "Kartarimukha": {"kn": "ಕರ್ತರಿಮುಖ", "hi": "कर्तरीमुख", "ta": "கர்த்தரிமுகா"},
    "Mayura": {"kn": "ಮಯೂರ", "hi": "मयूर", "ta": "மயூரா"},
    "Ardhachandra": {"kn": "ಅರ್ಧಚಂದ್ರ", "hi": "अर्धचंद्र", "ta": "அர்த்தசந்திரா"},
    "Arala": {"kn": "ಅರಾಳ", "hi": "अराल", "ta": "அராலா"},
    "Shukatunda": {"kn": "ಶುಕತುಂಡ", "hi": "शुकतुण्ड", "ta": "சுகதுண்டா"},
    "Mushti": {"kn": "ಮುಷ್ಟಿ", "hi": "मुष्टि", "ta": "முஷ்டி"},
    "Shikhara": {"kn": "ಶಿಖರ", "hi": "शिखर", "ta": "சிகரா"},
    "Hamsasya": {"kn": "ಹಂಸಾಸ್ಯ", "hi": "हंसस्य", "ta": "ஹம்சாச்யா"},
    "Suchi": {"kn": "ಸುಚಿ", "hi": "सूची", "ta": "சூசி"},
    "Chandrakala": {"kn": "ಚಂದ್ರಕಲಾ", "hi": "चन्द्रकला", "ta": "சந்திரகலா"},
    "Alapadma": {"kn": "ಅಲಪದ್ಮ", "hi": "अलपद्म", "ta": "அலபத்மா"},
    "Katakamukha": {"kn": "ಕಟಕಮುಖ", "hi": "कटकमुख", "ta": "கடகமுகா"},

    "Anjali": {"kn": "ಅಂಜಲಿ", "hi": "अंजलि", "ta": "அஞ்சலி"},
    "Kapota": {"kn": "ಕಪೋಟ", "hi": "कपोत", "ta": "கபோதா"},
    "Karkata": {"kn": "ಕರ್ಕಟ", "hi": "कर्कट", "ta": "கர்கடா"},
    "Swastika": {"kn": "ಸ್ವಸ್ತಿಕ", "hi": "स्वस्तिक", "ta": "ஸ்வஸ்திகா"},
    "Dola": {"kn": "ಡೋಲ", "hi": "डोल", "ta": "டோலா"},
    "Pushpaputa": {"kn": "ಪುಷ್ಪಪುಟ", "hi": "पुष्पपुट", "ta": "புஷ்பபுடா"},
    "Utsanga": {"kn": "ಉತ್ಸಂಗ", "hi": "उत्संग", "ta": "உத்சங்கா"},
    "Shivalinga": {"kn": "ಶಿವಲಿಂಗ", "hi": "शिवलिंग", "ta": "சிவலிங்கா"},
    "Katakavardhana": {"kn": "ಕಟಕವರ್ಧನ", "hi": "कटकवर्धन", "ta": "கடகவರ್ಧனா"},
    "Garuda": {"kn": "ಗರುಡ", "hi": "गरुड़", "ta": "கருடா"},
    "Nagabandha": {"kn": "ನಾಗಬಂಧ", "hi": "नागबन्ध", "ta": "நாகபந்தா"},
    "Matsya": {"kn": "ಮತ್ಸ್ಯ", "hi": "मत्स्य", "ta": "மத்ஸ்யா"},
    "Kurma": {"kn": "ಕುರ್ಮ", "hi": "कूर्म", "ta": "கூர்மா"},
    "Varaha": {"kn": "ವರಾಹ", "hi": "वराह", "ta": "வராஹா"}
}

# -----------------------------
# 🌐 Translation Function
# -----------------------------
def translate_text(text, target_lang):
    try:
        return GoogleTranslator(
            source='auto',
            target=target_lang
        ).translate(text)
    except:
        return text

# -----------------------------
# 🌍 Language Selection
# -----------------------------
lang_option = st.selectbox(
    "🌐 Select Output Language",
    ["en", "kn", "hi", "ta"]
)

# -----------------------------
# ✍️ User Input
# -----------------------------
user_input = st.text_input(
    "✍️ Enter Mudra Description:"
)

# -----------------------------
# 🔍 Prediction
# -----------------------------
if st.button("Predict Mudra"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter a description.")

    else:
        # Predict mudra
        result = predict_mudra(user_input)

        # Get translated mudra name
        if result in mudra_names_translation:
            translated_name = (
                mudra_names_translation[result]
                .get(lang_option, result)
            )
        else:
            translated_name = result

        # Success message
        st.success(
            f"✨ Predicted Mudra: {translated_name}"
        )

        # -----------------------------
        # Get details from dataset
        # -----------------------------
        mudra_data = (
            data[data["mudra"] == result]
            .iloc[0]
        )

        mudra_type = mudra_data["type"]
        mudra_meaning = mudra_data["meaning"]
        mudra_meaning = mudra_meaning.replace(" ", ", ")
        image_path = mudra_data["image"]

        # Translate details
        translated_type = translate_text(
            mudra_type,
            lang_option
        )

        translated_meaning = translate_text(
            mudra_meaning,
            lang_option
        )

        # -----------------------------
        # Mudra Details
        # -----------------------------
        with st.expander("📌 Mudra Details"):
            st.write(
                f"**Type:** {translated_type}"
            )
            st.write(
                f"**Meaning:** {translated_meaning}"
            )

        # -----------------------------
        # Display Image
        # -----------------------------
        if os.path.exists(image_path):

            st.image(
                image_path,
                caption=f"{translated_name} ({result})",
                width=280
            )

        else:
            st.warning(
                "⚠️ Image not found."
            )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.write(
    "💃 Bharatanatyam Learning System using NLP"
)